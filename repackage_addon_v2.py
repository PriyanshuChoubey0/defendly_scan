import zipfile
import os

def repackage_addon():
    source_dir = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\temp_reports_addon"
    # Update output filename to reflect new version
    output_zap = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\zap\src\main\dist\plugin\reports-release-0.38.1.zap"

    try:
        print(f"Repackaging from {source_dir} to {output_zap}...")
        with zipfile.ZipFile(output_zap, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Calculate relative path for the zip entry
                    rel_path = os.path.relpath(file_path, source_dir)
                    zipf.write(file_path, rel_path)
        print(f"Successfully repackaged add-on to {output_zap}")
        
        # Also remove the old version to avoid confusion
        old_zap = r"c:\Users\DELL\Desktop\R_Zap\defendly-tool\zap\src\main\dist\plugin\reports-release-0.38.0.zap"
        if os.path.exists(old_zap):
            os.remove(old_zap)
            print(f"Removed old version: {old_zap}")
            
    except Exception as e:
        print(f"Error repackaging add-on: {e}")

if __name__ == "__main__":
    repackage_addon()
