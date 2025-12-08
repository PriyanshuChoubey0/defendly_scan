import urllib.request
import urllib.parse
import time
import os
import json

# Configuration
ZAP_URL = "http://localhost:8080"
TARGET_URL = "http://testphp.vulnweb.com"  # Safe test target
API_KEY = ""  # Usually not needed for local testing

def wait_for_defendly():
    print("Waiting for Defendly to start...")
    for i in range(60):
        try:
            with urllib.request.urlopen(ZAP_URL, timeout=5) as response:
                if response.status == 200:
                    print("✓ Defendly is running!")
                    return True
        except:
            time.sleep(2)
            print(f"  Waiting... ({i+1}/60)")
    print("✗ Timeout: Defendly is not reachable.")
    return False

def access_url(url):
    """Access a URL to add it to the site tree"""
    print(f"\n1. Accessing target URL: {url}")
    params = {'url': url}
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    try:
        req_url = f"{ZAP_URL}/JSON/core/action/accessUrl/?{query}"
        with urllib.request.urlopen(req_url) as response:
            result = json.loads(response.read().decode('utf-8'))
            print(f"✓ URL accessed: {result}")
            return True
    except Exception as e:
        print(f"✗ Error accessing URL: {e}")
        return False

def run_quick_spider(url):
    """Run a quick spider scan"""
    print(f"\n2. Running Spider scan on {url}...")
    params = {'url': url, 'maxChildren': '10', 'recurse': 'true'}
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    try:
        resp_url = f"{ZAP_URL}/JSON/spider/action/scan/?{query}"
        with urllib.request.urlopen(resp_url) as response:
            resp = json.loads(response.read().decode('utf-8'))
            
            if 'scan' in resp:
                scan_id = resp['scan']
                print(f"✓ Spider started (ID: {scan_id})")
                
                # Wait for spider to complete
                for i in range(30):
                    time.sleep(2)
                    status_url = f"{ZAP_URL}/JSON/spider/view/status/?scanId={scan_id}"
                    with urllib.request.urlopen(status_url) as status_response:
                        status_resp = json.loads(status_response.read().decode('utf-8'))
                        status = int(status_resp['status'])
                        print(f"  Spider progress: {status}%")
                        if status >= 100:
                            print("✓ Spider scan complete!")
                            return True
                return True
    except Exception as e:
        print(f"✗ Spider error: {e}")
        return False

def run_quick_scan(url):
    """Run a quick active scan"""
    print(f"\n3. Running Active Scan on {url}...")
    params = {'url': url, 'recurse': 'false'}
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    try:
        resp_url = f"{ZAP_URL}/JSON/ascan/action/scan/?{query}"
        with urllib.request.urlopen(resp_url) as response:
            resp = json.loads(response.read().decode('utf-8'))
            
            if 'scan' in resp:
                scan_id = resp['scan']
                print(f"✓ Active Scan started (ID: {scan_id})")
                
                # Wait a bit for some results
                for i in range(20):
                    time.sleep(3)
                    status_url = f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}"
                    with urllib.request.urlopen(status_url) as status_response:
                        status_resp = json.loads(status_response.read().decode('utf-8'))
                        status = int(status_resp['status'])
                        print(f"  Active Scan progress: {status}%")
                        if status >= 100:
                            print("✓ Active Scan complete!")
                            return True
                        if status > 20:  # Get some results, don't wait for full scan
                            print("✓ Stopping scan early (enough data for report)")
                            return True
                return True
    except Exception as e:
        print(f"✗ Active Scan error: {e}")
        return False

def generate_report(template_name="traditional-html"):
    """Generate a report"""
    print(f"\n4. Generating {template_name} Report...")
    report_file = f"defendly_test_report_{template_name.replace('-', '_')}.html"
    report_dir = os.getcwd()
    
    params = {
        "title": "Defendly Scanning Report - Test",
        "template": template_name,
        "reportFileName": report_file,
        "reportDir": report_dir
    }
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    try:
        url = f"{ZAP_URL}/JSON/reports/action/generate/?{query}"
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        if API_KEY: req.add_header("X-ZAP-API-Key", API_KEY)
        
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                full_path = os.path.join(report_dir, report_file)
                print(f"✓ Report generated: {full_path}")
                return full_path
            else:
                print(f"✗ Failed to generate report (status: {response.status})")
                return None
    except Exception as e:
        print(f"✗ Error generating report: {e}")
        return None

def main():
    print("="*60)
    print("Defendly Report Branding Verification Script")
    print("="*60)
    
    if not wait_for_defendly():
        print("\n⚠ Please start Defendly first!")
        return
    
    # Access the target URL
    if not access_url(TARGET_URL):
        print("\n⚠ Failed to access target URL")
        return
    
    # Run spider
    run_quick_spider(TARGET_URL)
    
    # Run active scan
    run_quick_scan(TARGET_URL)
    
    # Generate reports with different templates
    print("\n" + "="*60)
    print("Generating Reports with Different Templates")
    print("="*60)
    
    templates = ["traditional-html", "modern", "high-level-report"]
    generated_reports = []
    
    for template in templates:
        report_path = generate_report(template)
        if report_path:
            generated_reports.append(report_path)
        time.sleep(2)
    
    print("\n" + "="*60)
    print("VERIFICATION COMPLETE!")
    print("="*60)
    print("\nGenerated Reports:")
    for report in generated_reports:
        print(f"  • {report}")
    
    print("\n📋 Next Steps:")
    print("  1. Open each report in a browser")
    print("  2. Check for 'Defendly Scanning Report' in the title")
    print("  3. Verify 'Defendly Version' appears (not 'ZAP Version')")
    print("  4. Confirm no 'ZAP' or 'Checkmarx' branding anywhere")

if __name__ == "__main__":
    main()
