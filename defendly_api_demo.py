import urllib.request
import urllib.parse
import time
import os
import json
import sys

# Configuration
ZAP_URL = "http://localhost:8080"
TARGET_URL = "http://localhost:8080"  # Scanning itself as a safe example
API_KEY = ""  # REPLACE THIS WITH YOUR API KEY IF ENABLED

def make_request(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/json")
    if API_KEY:
        req.add_header("X-ZAP-API-Key", API_KEY)
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        if e.code == 401 or e.code == 403:
            print("API Key required or incorrect. Please set the API_KEY variable in this script.")
            print("You can find the API key in Defendly under Tools > Options > API.")
        return None
    except urllib.error.URLError as e:
        print(f"Connection Error: {e.reason}")
        return None

def wait_for_zap():
    print("Checking if Defendly is running...")
    for i in range(60):
        try:
            with urllib.request.urlopen(ZAP_URL, timeout=5) as response:
                if response.status == 200:
                    print("Defendly is reachable.")
                    return True
        except:
            time.sleep(1)
    print("Timeout: Defendly is not reachable. Please start it first using './gradlew :zap:run'.")
    return False

def run_spider():
    print(f"Starting Spider scan on {TARGET_URL}...")
    params = {'url': TARGET_URL}
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    resp = make_request(f"{ZAP_URL}/JSON/spider/action/scan/?{query}")
    
    if resp and 'scan' in resp:
        scan_id = resp['scan']
        print(f"Spider started with ID: {scan_id}")
        
        while True:
            time.sleep(2)
            status_resp = make_request(f"{ZAP_URL}/JSON/spider/view/status/?scanId={scan_id}")
            if status_resp:
                status = int(status_resp['status'])
                print(f"Spider progress: {status}%")
                if status >= 100:
                    print("Spider scan complete.")
                    break
            else:
                break
    else:
        print("Failed to start Spider scan.")

def run_active_scan():
    print(f"Starting Active Scan on {TARGET_URL}...")
    params = {'url': TARGET_URL}
    if API_KEY: params['apikey'] = API_KEY
    
    query = urllib.parse.urlencode(params)
    resp = make_request(f"{ZAP_URL}/JSON/ascan/action/scan/?{query}")
    
    if resp and 'scan' in resp:
        scan_id = resp['scan']
        print(f"Active Scan started with ID: {scan_id}")
        
        while True:
            time.sleep(5)
            status_resp = make_request(f"{ZAP_URL}/JSON/ascan/view/status/?scanId={scan_id}")
            if status_resp:
                status = int(status_resp['status'])
                print(f"Active Scan progress: {status}%")
                if status >= 100:
                    print("Active Scan complete.")
                    break
            else:
                break
    else:
        print("Failed to start Active Scan. (Note: Active Scan requires URLs to be in the site tree, usually populated by Spider)")

def generate_report():
    print("Generating HTML Report...")
    report_file = "defendly_demo_report.html"
    report_dir = os.getcwd()
    
    params = {
        "title": "Defendly Demo Scan Report",
        "template": "traditional-html",
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
                print(f"Report generated successfully at: {full_path}")
            else:
                print("Failed to generate report.")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error generating report: {e.code} {e.reason}")
    except Exception as e:
        print(f"Error generating report: {e}")

def main():
    if not wait_for_zap():
        sys.exit(1)
    
    run_spider()
    time.sleep(2)
    run_active_scan()
    generate_report()
    print("\nDemo complete!")

if __name__ == "__main__":
    main()
