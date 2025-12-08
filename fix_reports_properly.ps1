# Properly fix the reports add-on with Defendly branding

Write-Host "="*70
Write-Host "FIXING REPORTS ADD-ON - Defendly Branding Update"
Write-Host "="*70

# Paths
$originalZip = "temp_reports.zip"
$tempExtract = "temp_reports_FIXED_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
$finalZip = "reports-defendly-branded.zap"
$installPath = "temp_dist_daily\Defendly_D-2025-12-05\plugin\reports-release-0.38.0.zap"

# Step 1: Extract
Write-Host "`n[1/5] Extracting original add-on..."
if (Test-Path $tempExtract) {
    Remove-Item $tempExtract -Recurse -Force
}
Expand-Archive -Path $originalZip -DestinationPath $tempExtract -Force
Write-Host "✓ Extracted to: $tempExtract"

# Step 2: Update Messages.properties files
Write-Host "`n[2/5] Updating Messages.properties files..."
$resourcesPath = "$tempExtract\org\zaproxy\addon\reports\resources"
$allFiles = Get-ChildItem -Path $resourcesPath -Filter "Messages*.properties"
$updatedCount = 0

foreach ($file in $allFiles) {
    Write-Host "  Processing: $($file.Name)"
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $originalContent = $content
    
    # Replace all ZAP branding variations
    $content = $content -replace 'ZAP by Checkmarx Scanning Report', 'Defendly Scanning Report'
    $content = $content -replace 'ZAP por Informe de Escaneo Checkmarx', 'Defendly Scanning Report'
    $content = $content -replace 'ZAP Version\\:', 'Defendly Version:'
    $content = $content -replace 'ZAP Versión\\:', 'Defendly Versión:'
    $content = $content -replace 'ZAP 版本：', 'Defendly 版本：'
    $content = $content -replace 'reports\.report\.title = ZAP', 'reports.report.title = Defendly'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP', 'reports.report.zapVersion = Defendly'
    
    if ($content -ne $originalContent) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        $updatedCount++
        Write-Host "    ✓ Updated"
    }
    else {
        Write-Host "    - No changes needed"
    }
}

Write-Host "`n✓ Updated $updatedCount files"

# Step 3: Verify changes
Write-Host "`n[3/5] Verifying changes..."
$mainFile = "$resourcesPath\Messages.properties"
$content = Get-Content $mainFile -Raw
if ($content -match "Defendly Scanning Report" -and $content -match "Defendly Version") {
    Write-Host "✓ Main Messages.properties verified - contains Defendly branding"
}
else {
    Write-Host "✗ WARNING: Main Messages.properties may not be updated correctly"
}

# Step 4: Create new ZIP
Write-Host "`n[4/5] Creating new add-on ZIP..."
if (Test-Path $finalZip) {
    Remove-Item $finalZip -Force
}
Compress-Archive -Path "$tempExtract\*" -DestinationPath $finalZip -CompressionLevel Optimal -Force
Write-Host "✓ Created: $finalZip"

# Step 5: Install to Defendly
Write-Host "`n[5/5] Installing to Defendly..."
if (Test-Path $installPath) {
    $backup = "$installPath.backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
    Copy-Item $installPath $backup
    Write-Host "✓ Backed up original to: $backup"
}

Copy-Item $finalZip $installPath -Force
Write-Host "✓ Installed to: $installPath"

# Cleanup
Write-Host "`n[Cleanup] Removing temporary files..."
Remove-Item $tempExtract -Recurse -Force
Write-Host "✓ Cleanup complete"

# Final verification
Write-Host "`n" + "="*70
Write-Host "INSTALLATION COMPLETE!"
Write-Host "="*70
Write-Host "`nFile hashes:"
$newHash = (Get-FileHash $finalZip -Algorithm MD5).Hash
$installedHash = (Get-FileHash $installPath -Algorithm MD5).Hash
Write-Host "  New add-on:    $newHash"
Write-Host "  Installed:     $installedHash"

if ($newHash -eq $installedHash) {
    Write-Host "`n✓ Hashes match - installation successful!"
}
else {
    Write-Host "`n✗ WARNING: Hashes don't match!"
}

Write-Host "`n" + "="*70
Write-Host "NEXT STEPS - CRITICAL!"
Write-Host "="*70
Write-Host "1. CLOSE Defendly completely (close the window)"
Write-Host "2. Kill any remaining java.exe processes in Task Manager"
Write-Host "3. Wait 10 seconds"
Write-Host "4. Restart Defendly from: temp_dist_daily\Defendly_D-2025-12-05\"
Write-Host "5. Generate a NEW report"
Write-Host "6. Verify it shows 'Defendly Scanning Report'"
Write-Host "`nThe old report you're looking at was generated with the old add-on!"
Write-Host "="*70
