# Script to update Messages.properties files inside the reports add-on ZIP

Write-Host "="*60
Write-Host "Updating Reports Add-on with Defendly Branding"
Write-Host "="*60

# Paths
$originalZip = "temp_reports.zip"
$tempExtract = "temp_reports_fixed"
$finalZip = "temp_dist_daily\Defendly_D-2025-12-05\plugin\reports-release-0.38.0.zap"

# Step 1: Extract the original ZIP
Write-Host "`n[1/4] Extracting original reports add-on..."
if (Test-Path $tempExtract) {
    Remove-Item $tempExtract -Recurse -Force
}
Expand-Archive -Path $originalZip -DestinationPath $tempExtract -Force
Write-Host "✓ Extracted to $tempExtract"

# Step 2: Update all Messages.properties files
Write-Host "`n[2/4] Updating Messages.properties files..."
$files = Get-ChildItem -Path "$tempExtract\org\zaproxy\addon\reports\resources\Messages_*.properties"
$count = 0

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Replace ZAP branding with Defendly
    $originalContent = $content
    $content = $content -replace 'reports\.report\.title = ZAP by Checkmarx Scanning Report', 'reports.report.title = Defendly Scanning Report'
    $content = $content -replace 'reports\.report\.title = ZAP por Informe de Escaneo Checkmarx', 'reports.report.title = Defendly Scanning Report'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP Version\\:', 'reports.report.zapVersion = Defendly Version:'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP Versión\\:', 'reports.report.zapVersion = Defendly Versión:'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP 版本：', 'reports.report.zapVersion = Defendly 版本：'
    
    if ($content -ne $originalContent) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        $count++
    }
}

# Also update the main Messages.properties
$mainFile = "$tempExtract\org\zaproxy\addon\reports\resources\Messages.properties"
if (Test-Path $mainFile) {
    $content = Get-Content $mainFile -Raw -Encoding UTF8
    $content = $content -replace 'reports\.report\.title = ZAP by Checkmarx Scanning Report', 'reports.report.title = Defendly Scanning Report'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP Version:', 'reports.report.zapVersion = Defendly Version:'
    [System.IO.File]::WriteAllText($mainFile, $content, [System.Text.Encoding]::UTF8)
    $count++
}

Write-Host "✓ Updated $count Messages.properties files"

# Step 3: Repackage as ZIP
Write-Host "`n[3/4] Repackaging add-on..."
if (Test-Path $finalZip) {
    Remove-Item $finalZip -Force
}
Compress-Archive -Path "$tempExtract\*" -DestinationPath $finalZip -Force
Write-Host "✓ Created $finalZip"

# Step 4: Cleanup
Write-Host "`n[4/4] Cleaning up..."
Remove-Item $tempExtract -Recurse -Force
Write-Host "✓ Cleanup complete"

Write-Host "`n" + "="*60
Write-Host "SUCCESS! Reports add-on updated with Defendly branding"
Write-Host "="*60
Write-Host "`nNext steps:"
Write-Host "1. Close Defendly if it's running"
Write-Host "2. Restart Defendly from: temp_dist_daily\Defendly_D-2025-12-05\"
Write-Host "3. Check that 'Report Generator' appears in Tools > Options > Extensions"
Write-Host "4. Generate a report to verify the branding"
