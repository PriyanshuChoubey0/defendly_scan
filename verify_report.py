import urllib.request
import urllib.parse
import time
import os
import json

def verify_report():
    zap_url = "http://localhost:8080"
    # Wait for ZAP to be ready
    print("Waiting for ZAP to be reachable...")
    for i in range(60):
        try:
            with urllib.request.urlopen(zap_url, timeout=5) as response:
                if response.status == 200:
                    print("ZAP is reachable.")
                    break
        except Exception as e:
            # print(f"Waiting... ({e})")
            time.sleep(2)
    else:
        print("Timeout waiting for ZAP.")
        return

    # Generate Report
    report_dir = os.getcwd()
    report_file = "defendly_report.html"
    
    # API: /JSON/reports/action/generate/
    params = {
        "title": "Defendly Scan Report",
        "template": "traditional-html",
        "reportFileName": report_file,
        "reportDir": report_dir
    }
    
    query_string = urllib.parse.urlencode(params)
    url = f"{zap_url}/JSON/reports/action/generate/?{query_string}"
    
    try:
        print(f"Generating report to {os.path.join(report_dir, report_file)}...")
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/json")
        
        with urllib.request.urlopen(req) as response:
            resp_text = response.read().decode('utf-8')
            print(f"Response: {response.status} {resp_text}")
            
            if response.status == 200:
                full_path = os.path.join(report_dir, report_file)
                # Give it a moment to write to disk
                time.sleep(2)
                
                if os.path.exists(full_path):
                    print(f"Report generated at {full_path}")
                    
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # Verification Checks
                    if "Defendly" in content:
                        print("PASS: 'Defendly' found in report.")
                    else:
                        print("FAIL: 'Defendly' NOT found in report.")
                    
                    if "OWASP ZAP" in content or "ZAP by Checkmarx" in content:
                        print("FAIL: ZAP branding found in report.")
                    else:
                        print("PASS: ZAP branding NOT found in report.")
                        
                    if "zap32x32.png" in content:
                         print("FAIL: ZAP logo reference found.")
                    else:
                         print("PASS: ZAP logo reference NOT found.")

                else:
                    print("Report file not found on disk.")
            else:
                print("Failed to generate report via API.")

    except Exception as e:
        print(f"Error verifying report: {e}")

if __name__ == "__main__":
    verify_report()
