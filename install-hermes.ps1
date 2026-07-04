# Idesign -> Hermes Agent Windows 安装脚本
# 将 idesign 技能套件安装到 ~/.hermes/skills/design/

param(
    [string]$HermesRoot = "$env:USERPROFILE\.hermes\skills\design"
)

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "=== Idesign -> Hermes (Windows) ===" -ForegroundColor Cyan
Write-Host "Target: $HermesRoot" -ForegroundColor Gray
Write-Host ""

# Create category directory
New-Item -ItemType Directory -Force -Path $HermesRoot | Out-Null

# [1/6] Install idesign dispatcher
Write-Host "[1/6] Installing idesign dispatcher..."
New-Item -ItemType Directory -Force -Path "$HermesRoot\idesign" | Out-Null
Copy-Item -Force "$ScriptDir\idesign.md" -Destination "$HermesRoot\idesign\SKILL.md"
Write-Host "  OK idesign"

# [2/6] Install 5 sub-skills
Write-Host "[2/6] Installing sub-skills..."
$skills = @("web-design-engineer", "web-video-presentation", "gpt-image-2", "beautiful-article", "kb-retriever")
foreach ($skill in $skills) {
    $src = "$ScriptDir\skills\$skill"
    $dst = "$HermesRoot\$skill"
    if (Test-Path $src) {
        if (Test-Path $dst) { Remove-Item -Recurse -Force $dst }
        Copy-Item -Recurse -Force $src -Destination $dst
        Write-Host "  OK $skill"
    } else {
        Write-Host "  MISS $skill" -ForegroundColor Yellow
    }
}

# [3/6] Install shared resources
Write-Host "[3/6] Installing shared resources..."
if (Test-Path "$HermesRoot\idesign\shared") { Remove-Item -Recurse -Force "$HermesRoot\idesign\shared" }
Copy-Item -Recurse -Force "$ScriptDir\shared" -Destination "$HermesRoot\idesign\shared"
Write-Host "  OK shared/ (refs + assets + SFX + BGM)"

# [4/6] Install scripts
Write-Host "[4/6] Installing scripts..."
if (Test-Path "$HermesRoot\idesign\scripts") { Remove-Item -Recurse -Force "$HermesRoot\idesign\scripts" }
Copy-Item -Recurse -Force "$ScriptDir\scripts" -Destination "$HermesRoot\idesign\scripts"
Write-Host "  OK scripts/ (15 tools)"

# [5/6] Install showcases
Write-Host "[5/6] Installing showcases..."
if (Test-Path "$HermesRoot\idesign\showcases") { Remove-Item -Recurse -Force "$HermesRoot\idesign\showcases" }
Copy-Item -Recurse -Force "$ScriptDir\showcases" -Destination "$HermesRoot\idesign\showcases"
Write-Host "  OK showcases/ (24 examples)"

# [6/6] Install demos
Write-Host "[6/6] Installing demos..."
if (Test-Path "$ScriptDir\demos-huashu") {
    if (Test-Path "$HermesRoot\idesign\demos") { Remove-Item -Recurse -Force "$HermesRoot\idesign\demos" }
    Copy-Item -Recurse -Force "$ScriptDir\demos-huashu" -Destination "$HermesRoot\idesign\demos"
    Write-Host "  OK demos/ (21 examples)"
}

Write-Host ""
Write-Host "=== Installation complete ===" -ForegroundColor Green
Write-Host ""
Write-Host "Installed at: $HermesRoot"
Write-Host ""
Write-Host "Verify in Hermes:"
Write-Host "  hermes skills list | Select-String design"
Write-Host ""
Write-Host "Usage example:"
Write-Host '  "Use idesign to build a SaaS landing page"'
