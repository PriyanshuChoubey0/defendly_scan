import os

def update_modern_report():
    report_path = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\temp_reports_addon\reports\modern\report.html"
    logo_path = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\logo_base64.txt"

    try:
        with open(logo_path, "r") as f:
            logo_base64 = f.read().strip()
        
        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Replace Logo
        # The original code:
        # <!-- The ZAP Logo -->
        # <img th:src="${resources + '/zap32x32.png'}"
        #     src="resources/zap32x32.png" alt="ZAP" />
        
        old_logo_block = """<!-- The ZAP Logo -->
					<img th:src="${resources + '/zap32x32.png'}"
						src="resources/zap32x32.png" alt="ZAP" />"""
        
        new_logo_block = f"""<!-- The Defendly Logo -->
					<img src="data:image/png;base64,{logo_base64}" alt="Defendly" />"""
        
        if old_logo_block in content:
            content = content.replace(old_logo_block, new_logo_block)
            print("Replaced Logo block.")
        else:
            print("Warning: Logo block not found exactly as expected. Trying partial match or manual check needed.")
            # Fallback for potential whitespace differences
            # We can try to replace just the img tag if the comment is different
            pass

        # 2. Replace ZAP Version placeholder
        if ">ZAP Version</th:block>" in content:
            content = content.replace(">ZAP Version</th:block>", ">Defendly Version</th:block>")
            print("Replaced ZAP Version placeholder.")

        # 3. Replace Footer
        # <h4>
        #     ZAP by <a href="https://checkmarx.com/">Checkmarx</a>
        # </h4>
        
        old_footer = """<h4>
					ZAP by <a href="https://checkmarx.com/">Checkmarx</a>
				</h4>"""
        
        new_footer = """<h4>
					Defendly AI
				</h4>"""

        if old_footer in content:
            content = content.replace(old_footer, new_footer)
            print("Replaced Footer.")
        else:
             print("Warning: Footer block not found exactly as expected.")

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        print(f"Successfully updated {report_path}")

    except Exception as e:
        print(f"Error updating modern report: {e}")

if __name__ == "__main__":
    update_modern_report()
