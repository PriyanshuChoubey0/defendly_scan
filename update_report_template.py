import os
import re

def update_file(file_path, logo_base64):
    print(f"Processing {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace logo
    start_marker = 'src="data:image/png;base64,'
    start_index = content.find(start_marker)
    
    if start_index != -1:
        end_index = content.find('"', start_index + len(start_marker))
        if end_index != -1:
            old_src = content[start_index:end_index+1]
            new_src = 'src="data:image/png;base64,' + logo_base64 + '"'
            content = content.replace(old_src, new_src)
            print(f"Replaced logo in {file_path}")
        else:
            print(f"Could not find closing quote for logo in {file_path}")
    else:
        print(f"Could not find logo marker in {file_path}")

    # Replace footer text
    # ZAP by <a href="https://checkmarx.com/">Checkmarx</a>
    # to Defendly AI
    
    # Using regex to handle potential whitespace variations
    footer_pattern = r'ZAP\s+by\s+<a\s+href="https://checkmarx\.com/">Checkmarx</a>'
    if re.search(footer_pattern, content):
        content = re.sub(footer_pattern, 'Defendly AI', content)
        print(f"Replaced footer in {file_path}")
    else:
        print(f"Could not find footer in {file_path}")
        # Debug: print context around where footer should be
        idx = content.find("ZAP by")
        if idx != -1:
            print(f"Found 'ZAP by' at index {idx}: {content[idx:idx+100]}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    logo_file = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\logo_base64.txt"
    report_file = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\temp_reports_addon\reports\traditional-html\report.html"
    
    try:
        with open(logo_file, 'r', encoding='utf-8') as f:
            logo_base64 = f.read().strip()
    except Exception as e:
        print(f"Error reading logo file: {e}")
        return

    update_file(report_file, logo_base64)

if __name__ == "__main__":
    main()
