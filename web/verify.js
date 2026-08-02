import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dataPath = path.join(__dirname, 'data.json');

console.log('🔍 Running Wolfi OpenSSL FIPS Web Payload Verification...');

if (!fs.existsSync(dataPath)) {
  console.error('❌ Error: data.json not found in web/ directory!');
  process.exit(1);
}

try {
  const content = fs.readFileSync(dataPath, 'utf-8');
  const data = JSON.parse(content);
  
  if (!data.project_name) {
    throw new Error('Missing "project_name" field');
  }
  
  console.log('✅ Success: web/data.json is valid and contains standard metadata.');
} catch (e) {
  console.error('❌ Error parsing web/data.json:', e.message);
  process.exit(1);
}
