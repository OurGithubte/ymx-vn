#Requires -RunAsAdministrator
<#
  Script nay giup chay website YMX Vietnam qua IIS (co san tren Windows),
  chay NGAM nhu mot dich vu he thong - khong can mo bat ky cua so nao,
  tu dong khoi dong lai cung Windows moi khi bat may.

  CACH CHAY:
  1. Bam chuot phai vao PowerShell -> "Run as Administrator"
  2. Chay lenh:  Set-ExecutionPolicy Bypass -Scope Process -Force
  3. Chay:  & "E:\YMX Websile\setup-iis.ps1"
  4. Doi vai phut de Windows cai dat tinh nang IIS (chi lan dau)
#>

$SiteName = "YMX-Website"
$SitePath = "E:\YMX Websile"
$Port     = 8080

Write-Host "===== CAI DAT WEBSITE YMX QUA IIS =====" -ForegroundColor Cyan

Write-Host "Buoc 1/4: Bat tinh nang IIS (neu chua co)..." -ForegroundColor Cyan
Enable-WindowsOptionalFeature -Online -NoRestart -All -FeatureName `
    IIS-WebServerRole, IIS-WebServer, IIS-CommonHttpFeatures, IIS-StaticContent, `
    IIS-DefaultDocument, IIS-WebServerManagementTools, IIS-ManagementConsole | Out-Null

Import-Module WebAdministration -ErrorAction Stop

Write-Host "Buoc 2/4: Tao / cap nhat website tro toi $SitePath ..." -ForegroundColor Cyan
if (Get-Website -Name $SiteName -ErrorAction SilentlyContinue) {
    Set-ItemProperty "IIS:\Sites\$SiteName" -Name physicalPath -Value $SitePath
    Write-Host "  -> Da cap nhat website co san '$SiteName'."
} else {
    New-Website -Name $SiteName -PhysicalPath $SitePath -Port $Port | Out-Null
    Write-Host "  -> Da tao website moi '$SiteName' tren port $Port."
}

Write-Host "Buoc 3/4: Dat index.html lam trang mac dinh..." -ForegroundColor Cyan
Add-WebConfiguration //defaultDocument/files -PSPath "IIS:\Sites\$SiteName" -Value @{value='index.html'} -ErrorAction SilentlyContinue | Out-Null

Write-Host "Buoc 4/4: Mo Firewall cho port $Port (chi trong mang noi bo)..." -ForegroundColor Cyan
if (-not (Get-NetFirewallRule -DisplayName "YMX Website LAN" -ErrorAction SilentlyContinue)) {
    New-NetFirewallRule -DisplayName "YMX Website LAN" -Direction Inbound -Protocol TCP -LocalPort $Port -Action Allow | Out-Null
}

Start-Website -Name $SiteName -ErrorAction SilentlyContinue

$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {
    $_.InterfaceAlias -notmatch "Loopback" -and $_.IPAddress -notlike "169.*"
} | Select-Object -First 1).IPAddress

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host " HOAN TAT! Website chay ngam qua IIS - khong can mo cua so nao ca." -ForegroundColor Green
Write-Host " Tu dong chay lai moi khi khoi dong Windows."
Write-Host ""
Write-Host " May nay xem tai:      http://localhost:$Port/"
Write-Host " May khac trong LAN:   http://$ip`:$Port/"
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Luu y: neu sau nay sua noi dung file trong '$SitePath', chi can luu lai"
Write-Host "va bam F5 tren trinh duyet - khong can chay lai script nay."
