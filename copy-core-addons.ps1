# PowerShell script to copy only CORE add-ons to plugin directory
# Core add-ons are marked with 'core: true' in main-add-ons.yml

$coreAddOns = @(
    "ascanrules",
    "bruteforce", 
    "callhome",
    "commonlib",
    "database",
    "diff",
    "gettingStarted",
    "help",
    "invoke",
    "network",
    "oast",
    "onlineMenu",
    "pscan",
    "pscanrules",
    "quickstart",
    "reports",
    "reveal",
    "scanpolicies",
    "spider",
    "tips"
)

$sourceDir = "c:\Users\DELL\Desktop\R_Zap\defendly-tool\zap\build\mainAddOns"
$destDir = "c:\Users\DELL\Desktop\R_Zap\defendly-tool\zap\src\main\dist\plugin"

Write-Host "Copying CORE add-ons to plugin directory..." -ForegroundColor Cyan
Write-Host ""

$copiedCount = 0
foreach ($addon in $coreAddOns) {
    $files = Get-ChildItem -Path $sourceDir -Filter "$addon-*.zap"
    
    if ($files.Count -gt 0) {
        foreach ($file in $files) {
            Copy-Item -Path $file.FullName -Destination $destDir -Force
            Write-Host "Copied: $($file.Name)" -ForegroundColor Green
            $copiedCount++
        }
    } else {
        Write-Host "Not found: $addon" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Copied $copiedCount core add-ons successfully!" -ForegroundColor Green
Write-Host ""

# List final plugin directory contents
Write-Host "Plugin directory now contains:" -ForegroundColor Cyan
Get-ChildItem -Path $destDir -Filter *.zap | Select-Object Name, @{Name='SizeMB';Expression={[math]::Round($_.Length / 1MB, 2)}} | Format-Table -AutoSize
