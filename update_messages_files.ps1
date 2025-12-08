$files = Get-ChildItem -Path "temp_reports_addon\org\zaproxy\addon\reports\resources\Messages_*.properties"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    
    # Replace ZAP branding with Defendly
    $content = $content -replace 'reports\.report\.title = ZAP by Checkmarx Scanning Report', 'reports.report.title = Defendly Scanning Report'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP Version\\:', 'reports.report.zapVersion = Defendly Version:'
    $content = $content -replace 'reports\.report\.zapVersion = ZAP 版本：', 'reports.report.zapVersion = Defendly 版本：'
    
    # Write back to file
    [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Updated: $($file.Name)"
}

Write-Host "`nAll Messages.properties files updated successfully!"
