import urllib.request
import urllib.parse
import os

# Configuration
ZAP_URL = "http://localhost:8080"
API_KEY = "0bio028fq95ucc9f6e6779ihdi"  # From your screenshot

print("="*60)
print("Generating Defendly Report via API")
print("="*60)

# Step 1: Get available templates
print("\n[1/2] Fetching available templates...")
try:
    url = f"{ZAP_URL}/JSON/reports/view/templates/"
    req = urllib.request.Request(url)
    req.add_header("X-ZAP-API-Key", API_KEY)
    
    with urllib.request.urlopen(req) as response:
        import json
        data = json.loads(response.read().decode('utf-8'))
        templates = data.get('templates', [])
        print(f"✓ Available templates: {', '.join(templates)}")
except Exception as e:
    print(f"✗ Error: {e}")
    exit(1)

# Step 2: Generate report with correct template
print("\n[2/2] Generating report...")
report_dir = os.getcwd()
report_file = "defendly_test_report.html"

params = {
    "apikey": API_KEY,
    "title": "Defendly Test Report",
    "template": "traditional-html",  # Valid template name
    "reportFileName": report_file,
    "reportDir": report_dir,
    "display": "false"
}

query = urllib.parse.urlencode(params)
try:
    url = f"{ZAP_URL}/JSON/reports/action/generate/?{query}"
    print(f"\nRequest URL: {url[:100]}...")
    
    req = urllib.request.Request(url)
    req.add_header("X-ZAP-API-Key", API_KEY)
    
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))
        print(f"\n✓ API Response: {result}")
        
        full_path = os.path.join(report_dir, report_file)
        if os.path.exists(full_path):
            print(f"\n✓ SUCCESS! Report generated at:")
            print(f"  {full_path}")
            
            # Check branding
            print("\n" + "="*60)
            print("Checking Report Branding...")
            print("="*60)
            
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                # Check for Defendly branding
                defendly_title = "Defendly Scanning Report" in content
                defendly_version = "Defendly Version" in content
                no_zap_checkmarx = "ZAP by Checkmarx" not in content
                no_zap_version = content.count("ZAP Version") == 0 or "Defendly Version" in content
                
                print(f"\n{'✓' if defendly_title else '✗'} Defendly Scanning Report: {'FOUND' if defendly_title else 'NOT FOUND'}")
                print(f"{'✓' if defendly_version else '✗'} Defendly Version: {'FOUND' if defendly_version else 'NOT FOUND'}")
                print(f"{'✓' if no_zap_checkmarx else '✗'} No 'ZAP by Checkmarx': {'PASS' if no_zap_checkmarx else 'FAIL'}")
                print(f"{'✓' if no_zap_version else '✗'} No 'ZAP Version': {'PASS' if no_zap_version else 'FAIL'}")
                
                if defendly_title and defendly_version and no_zap_checkmarx:
                    print("\n" + "="*60)
                    print("🎉 SUCCESS! Defendly branding is working correctly!")
                    print("="*60)
                else:
                    print("\n" + "="*60)
                    print("⚠ WARNING: Some branding issues detected")
                    print("="*60)
                    
            print(f"\n📄 Open the report to verify visually:")
            print(f"   {full_path}")
        else:
            print(f"\n✗ Report file not found at: {full_path}")
            
except Exception as e:
    print(f"\n✗ Error generating report: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "="*60)
print("Done!")
print("="*60)
