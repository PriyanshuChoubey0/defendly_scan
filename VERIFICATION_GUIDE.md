# Defendly Reports Branding Verification Guide

## What We Fixed

We updated **63 language-specific Messages.properties files** in the reports extension to replace:
- `ZAP by Checkmarx Scanning Report` → `Defendly Scanning Report`
- `ZAP Version: {0}` → `Defendly Version: {0}`

The rebranded add-on has been installed at:
```
temp_dist_daily\Defendly_D-2025-12-05\plugin\reports-release-0.38.0.zap
```

## How to Verify

### Step 1: Start Defendly
```powershell
cd temp_dist_daily\Defendly_D-2025-12-05
.\defendly.bat
```

Wait for Defendly to fully start (you should see the UI).

### Step 2: Run a Quick Scan
1. In Defendly, go to the **Quick Start** tab
2. Enter a test URL: `http://testphp.vulnweb.com`
3. Click **Automated Scan**
4. Wait for the scan to complete (a few minutes)

### Step 3: Generate a Report
1. Go to **Report** → **Generate Report** (or press Ctrl+R)
2. Select a template:
   - **Traditional HTML**
   - **Modern**
   - **High Level Report**
3. Choose a location to save the report
4. Click **Generate Report**

### Step 4: Check the Report
Open the generated HTML report and verify:

✅ **Title should show:** "Defendly Scanning Report"
✅ **Version line should show:** "Defendly Version: X.X.X"
✅ **NO "ZAP" or "Checkmarx" branding** should appear

### Example of What You Should See:

```html
<h1>Defendly Scanning Report</h1>
<h3>Defendly Version: 2.17.0-SNAPSHOT</h3>
```

### Example of What You Should NOT See:

```html
<h1>ZAP by Checkmarx Scanning Report</h1>
<h3>ZAP Version: 2.17.0-SNAPSHOT</h3>
```

## If Defendly Won't Start

The reports extension might not be loading. Check:

1. **Console output** - Look for any errors about the reports extension
2. **Extension Manager** - Go to Tools → Options → Extensions and verify "Report Generator" is loaded
3. **Reinstall** - If needed, manually install `reports-rebranded.zip` via the Extensions UI

## Alternative: Use Python Script

If you prefer automation, run:
```powershell
python quick_report_test.py
```

This will:
- Check if Defendly is running
- Generate a test report
- Automatically verify the branding in the report file
- Show you the results

## Files Created

- `reports-rebranded.zip` - The rebranded add-on
- `update_messages_files.ps1` - Script that updated all language files
- `quick_report_test.py` - Automated verification script
- `verify_reports_branding.py` - Full scan + report generation script

## Summary

The branding fix is complete! The Messages.properties files control the text that appears in reports. By updating all 63 language files and repackaging the add-on, we've ensured that all future reports will show "Defendly" branding instead of "ZAP".
