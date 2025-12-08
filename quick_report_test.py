import urllib.request
import urllib.parse
import os
import json
import time

ZAP_URL = "http://localhost:8080"

print("Testing Defendly Connection...")
print("="*60)

# Test 1: Check if Defendly is running
try:
    with urllib.request.urlopen(ZAP_URL, timeout=10) as response:
        print("✓ Defendly is running on port 8080")
except Exception as e:
    print(f"✗ Cannot connect to Defendly: {e}")
    print("\nPlease ensure Defendly is running!")
    exit(1)

# Test 2: Get available templates
print("\nFetching available report templates...")
try:
    url = f"{ZAP_URL}/JSON/reports/view/templates/"
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        templates = data.get('templates', [])
        print(f"✓ Found {len(templates)} templates:")
        for template in templates:
            print(f"  • {template}")
except Exception as e:
    print(f"✗ Error fetching templates: {e}")

# Test 3: Generate a simple report (even with no scan data)
print("\n" + "="*60)
print("Generating Test Report...")
print("="*60)

report_file = "defendly_branding_test.html"
report_dir = os.getcwd()

params = {
    "title": "Defendly Branding Test",
    "template": "traditional-html",
    "reportFileName": report_file,
    "reportDir": report_dir,
    "display": "false"
}

query = urllib.parse.urlencode(params)
try:
    url = f"{ZAP_URL}/JSON/reports/action/generate/?{query}"
    print(f"\nRequest URL: {url}")
    
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"\nAPI Response: {result}")
        
        full_path = os.path.join(report_dir, report_file)
        if os.path.exists(full_path):
            print(f"\n✓ SUCCESS! Report generated at:")
            print(f"  {full_path}")
            
            # Read first few lines to check branding
            print("\n" + "="*60)
            print("Checking Report Content...")
            print("="*60)
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for Defendly branding
                if "Defendly Scanning Report" in content:
                    print("✓ Found 'Defendly Scanning Report' in report")
                else:
                    print("✗ 'Defendly Scanning Report' NOT found")
                
                if "Defendly Version" in content:
                    print("✓ Found 'Defendly Version' in report")
                else:
                    print("✗ 'Defendly Version' NOT found")
                
                # Check for old ZAP branding (should NOT exist)
                if "ZAP by Checkmarx" in content:
                    print("✗ WARNING: Still found 'ZAP by Checkmarx' branding!")
                else:
                    print("✓ No 'ZAP by Checkmarx' branding found")
                
                if "ZAP Version" in content and "Defendly Version" not in content:
                    print("✗ WARNING: Still found 'ZAP Version'!")
                else:
                    print("✓ No standalone 'ZAP Version' found")
            
            print("\n" + "="*60)
            print("VERIFICATION COMPLETE!")
            print("="*60)
            print(f"\n📄 Open the report to visually verify:")
            print(f"   {full_path}")
            
        else:
            print(f"\n✗ Report file not found at: {full_path}")
            
except urllib.error.HTTPError as e:
    print(f"\n✗ HTTP Error: {e.code} - {e.reason}")
    print(f"   Response: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"\n✗ Error generating report: {e}")
