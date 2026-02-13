def test_26_hmac_key_length_enforcement(image_tag: str):
    category = "Key Strength Enforcement (HMAC-SHA256)"
    
    # 8 bytes key (64 bits) - MUST BE REJECTED (FIPS requires >= 112 bits)
    short_key_hex = "0102030405060708" 
    
    # نستخدم أمر 'mac' الحديث بدلاً من 'dgst' لضمان تفعيل الـ Provider validation
    args = ["mac", "-digest", "SHA256", "-macopt", f"hexkey:{short_key_hex}", "HMAC"]
    
    code, stdout, stderr = run_container_command(image_tag, args)
    error_msg = stderr.decode('utf-8', errors='ignore').lower()

    if code != 0 and any(x in error_msg for x in ["too short", "invalid", "low entropy", "error"]):
        log_success(
            26, category,
            "FIPS Provider strictly rejected a 64-bit HMAC key using the native MAC interface."
        )
    elif code == 0:
        log_failure(
            26, category,
            "Compliance Failure: System accepted a 64-bit HMAC key.",
            "The FIPS module is active but allowed a weak key on the native MAC interface."
        )