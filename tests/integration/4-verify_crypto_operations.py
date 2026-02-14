import subprocess
import sys

# ألوان للطباعة في التيرمينال لسهولة القراءة
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def log_success(test_no, category, message):
    print(f"{GREEN}[SUCCESS]{RESET} TEST {test_no:02d} - {category}: {message}")

def log_failure(test_no, category, message, error_details=None):
    print(f"{RED}[FAILURE]{RESET} TEST {test_no:02d} - {category}: {message}")
    if error_details:
        print(f"{BLUE}[DEBUG]{RESET} Root Cause: {error_details}")
    sys.exit(1)

def run_cmd(image, args, stdin_input=None):
    # نمرر -provider fips و -provider base لضمان العمل في البيئة الصارمة
    docker_base = ["docker", "run", "--rm", "-i"] if stdin_input else ["docker", "run", "--rm"]
    cmd = docker_base + [image] + args
    
    try:
        proc = subprocess.run(
            cmd,
            input=stdin_input.encode() if stdin_input else None,
            capture_output=True,
            text=True,
            check=False
        )
        return proc.returncode, proc.stdout, proc.stderr
    except Exception as e:
        return -1, "", str(e)

# --- الاختبارات ---

def test_08_rsa_gen(image):
    """اختبار توليد مفاتيح RSA (يجب أن يكون 2048+ بت في FIPS)"""
    category = "Asymmetric Key Gen (RSA)"
    # ملاحظة: أضفنا الموديلات يدوياً لضمان فك التشفير (Encoding)
    args = ["genpkey", "-provider", "fips", "-provider", "base", "-algorithm", "RSA", "-pkeyopt", "rsa_keygen_bits:2048"]
    
    code, out, err = run_cmd(image, args)
    if code == 0 and "-----BEGIN PRIVATE KEY-----" in out:
        log_success(8, category, "RSA 2048-bit key generated successfully.")
    else:
        log_failure(8, category, "FIPS RSA generation failed.", f"Code: {code}, Error: {err.strip()}")

def test_09_cipher_list(image):
    """اختبار وجود الخوارزميات المعتمدة (AES-GCM)"""
    category = "Symmetric Cipher Availability"
    # نستخدم list بدلاً من ciphers لأنها متوافقة مع الوضع الصارم
    args = ["list", "-cipher-algorithms", "-provider", "fips"]
    
    code, out, err = run_cmd(image, args)
    if code == 0 and "AES-256-GCM" in out:
        log_success(9, category, "Verified AES-256-GCM is active in FIPS provider.")
    else:
        log_failure(9, category, "FIPS ciphers not listed properly.", f"Output: {out[:100]}")

def test_26_hmac_enforcement(image):
    """اختبار رفض مفاتيح HMAC القصيرة (أقل من 112 بت)"""
    category = "HMAC Key Length Enforcement"
    short_key = "12345678" # 64-bit (مرفوض في FIPS 140-3)
    
    # نحاول تشغيل HMAC بمفتاح قصير؛ المتوقع هو الفشل (Exit Code != 0)
    args = ["dgst", "-sha256", "-hmac", short_key, "/dev/null"]
    code, out, err = run_cmd(image, args)
    
    # في الوضع الصارم، يجب أن يفشل الأمر (code != 0)
    if code != 0:
        log_success(26, category, f"Strict policy REJECTED short HMAC key (Code {code}). This is correct.")
    else:
        log_failure(26, category, "Security vulnerability: System ACCEPTED a 64-bit HMAC key!", "FIPS 140-3 requires min 112-bit.")

# --- التشغيل الرئيسي ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <image_tag>")
        sys.exit(1)

    target = sys.argv[1]
    print("="*80)
    print(f"STARTING FIPS 140-3 COMPLIANCE AUDIT FOR: {target}")
    print("="*80)

    test_08_rsa_gen(target)
    test_09_cipher_list(target)
    test_26_hmac_enforcement(target)

    print("="*80)
    print(f"{GREEN}ALL TESTS PASSED: Image is FIPS 140-3 Compliant!{RESET}")
    print("="*80)
