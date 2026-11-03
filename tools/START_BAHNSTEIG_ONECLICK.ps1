#requires -Version 5.1
# Bahnsteig 50 Hz - Relux / SIMARIS assisted automation, V1
# SAFETY: no changes to existing V0.2/V0.3; no invented calculation results.
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

if (-not ("BahnAutoWin32_20261103" -as [type])) {
Add-Type @'
using System;
using System.Text;
using System.Collections.Generic;
using System.Runtime.InteropServices;
public static class BahnAutoWin32_20261103 {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left, Top, Right, Bottom; }
    public delegate bool EnumProc(IntPtr hwnd, IntPtr lParam);
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hwnd, int cmd);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hwnd);
    [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hwnd, out uint pid);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hwnd, out RECT rect);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
    [DllImport("user32.dll")] public static extern void mouse_event(uint flags, uint dx, uint dy, int data, UIntPtr extra);
    [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc fn, IntPtr param);
    [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr hwnd, EnumProc fn, IntPtr param);
    [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr hwnd, StringBuilder str, int size);
    [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr hwnd, StringBuilder str, int size);
    [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr hwnd);
    [DllImport("user32.dll")] public static extern bool IsWindowEnabled(IntPtr hwnd);
    [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr hwnd, uint msg, IntPtr wparam, IntPtr lparam);
    public class WndInfo { public IntPtr Handle; public int PID; public string Title; public string ClassName; }
    public static WndInfo[] Windows() {
        var items = new List<WndInfo>();
        EnumWindows((hwnd, data) => {
            uint pid;
            GetWindowThreadProcessId(hwnd, out pid);
            if (pid == 0 || !IsWindowVisible(hwnd)) return true;
            var title = new StringBuilder(500);
            var cls = new StringBuilder(300);
            GetWindowText(hwnd, title, title.Capacity);
            GetClassName(hwnd, cls, cls.Capacity);
            items.Add(new WndInfo {Handle=hwnd, PID=(int)pid, Title=title.ToString(), ClassName=cls.ToString()});
            return true;
        }, IntPtr.Zero);
        return items.ToArray();
    }
    public static WndInfo[] Children(IntPtr parent) {
        var items = new List<WndInfo>();
        EnumChildWindows(parent, (hwnd, data) => {
            uint pid;
            GetWindowThreadProcessId(hwnd, out pid);
            var title = new StringBuilder(500);
            var cls = new StringBuilder(300);
            GetWindowText(hwnd, title, title.Capacity);
            GetClassName(hwnd, cls, cls.Capacity);
            items.Add(new WndInfo {Handle=hwnd, PID=(int)pid, Title=title.ToString(), ClassName=cls.ToString()});
            return true;
        }, IntPtr.Zero);
        return items.ToArray();
    }
}
'@
}

$root = Join-Path ([Environment]::GetFolderPath("MyDocuments")) "bahnsteig-50hz-elektroplanung-demo"
$relux = Join-Path $root "05_Relux_Beleuchtung"
$simaris = Join-Path $root "04_SIMARIS_Netzberechnung"
$dxf = Join-Path $relux "Bahnsteig_Relux_Import_V0.4.dxf"
$source = Join-Path $env:USERPROFILE "Downloads\DB-LVK-B0410083\Extracted"
$target = Join-Path $relux "DB_LVK_B0410083"
$diag = Join-Path $env:USERPROFILE ("Downloads\Bahnsteig-OneClick-" + (Get-Date -Format "yyyyMMdd-HHmmss"))
New-Item -ItemType Directory -Path $diag -Force | Out-Null
$log = Join-Path $diag "Status.txt"
$notes = New-Object System.Collections.Generic.List[string]
$oldClipboard = try { Get-Clipboard -Raw -ErrorAction Stop } catch { $null }
function Log([string]$line) {
    $notes.Add((Get-Date -Format "HH:mm:ss") + " " + $line)
    Write-Host $line
}
function Get-ReluxElements([IntPtr]$handle) {
    $e = [System.Windows.Automation.AutomationElement]::FromHandle($handle)
    return $e.FindAll([System.Windows.Automation.TreeScope]::Descendants,
        [System.Windows.Automation.Condition]::TrueCondition)
}
function Get-Edits([IntPtr]$handle) {
    $found = @(Get-ReluxElements $handle | Where-Object {
        $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Edit -and
        $_.Current.Name -eq "RichEdit Control" -and
        !$_.Current.IsOffscreen
    } | Sort-Object { $_.Current.BoundingRectangle.Top })
    return ,$found
}
function Focus-Relux([IntPtr]$handle, [int]$expectedPid) {
    [BahnAutoWin32_20261103]::ShowWindow($handle,3) | Out-Null
    [BahnAutoWin32_20261103]::SetForegroundWindow($handle) | Out-Null
    Start-Sleep -Milliseconds 550
    $active=[BahnAutoWin32_20261103]::GetForegroundWindow()
    $pidNumber=[uint32]0
    [BahnAutoWin32_20261103]::GetWindowThreadProcessId($active,[ref]$pidNumber) | Out-Null
    return ($pidNumber -eq $expectedPid)
}
function Get-ReluxRect([IntPtr]$handle) {
    $r=New-Object BahnAutoWin32_20261103+RECT
    if (![BahnAutoWin32_20261103]::GetWindowRect($handle,[ref]$r)) { throw "Cannot locate Relux window." }
    return $r
}
function Save-ReluxScreenshot([IntPtr]$handle,[string]$name) {
    $r=Get-ReluxRect $handle
    $w=$r.Right-$r.Left; $h=$r.Bottom-$r.Top
    if ($w -lt 350 -or $h -lt 350) { return }
    $bmp=New-Object System.Drawing.Bitmap($w,$h)
    $gfx=[System.Drawing.Graphics]::FromImage($bmp)
    try {
        $gfx.CopyFromScreen($r.Left,$r.Top,0,0,$bmp.Size)
        $bmp.Save((Join-Path $diag ($name + ".png")),[System.Drawing.Imaging.ImageFormat]::Png)
    } finally { $gfx.Dispose();$bmp.Dispose() }
}
function Click-Relux([int]$x,[int]$y) {
    [BahnAutoWin32_20261103]::SetCursorPos($x,$y) | Out-Null
    Start-Sleep -Milliseconds 130
    [BahnAutoWin32_20261103]::mouse_event(0x0002,0,0,0,[UIntPtr]::Zero)
    [BahnAutoWin32_20261103]::mouse_event(0x0004,0,0,0,[UIntPtr]::Zero)
}
function Find-ReluxDialog([int]$targetProcessId,[string]$regex) {
    return @( [BahnAutoWin32_20261103]::Windows() | Where-Object {
        $_.PID -eq $targetProcessId -and $_.Title -match $regex
    })
}
function Invoke-Named([IntPtr]$handle,[string]$regex) {
    foreach ($ui in @(Get-ReluxElements $handle)) {
        try {
            if ($ui.Current.ControlType -ne [System.Windows.Automation.ControlType]::Button) { continue }
            if ($ui.Current.Name -notmatch $regex -or !$ui.Current.IsEnabled) { continue }
            $pattern=$null
            if ($ui.TryGetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern,[ref]$pattern)) {
                $pattern.Invoke()
                return $true
            }
        } catch { }
    }
    foreach($c in @([BahnAutoWin32_20261103]::Children($handle))) {
        if ($c.Title -match $regex -and $c.ClassName -match "Button" -and
            [BahnAutoWin32_20261103]::IsWindowVisible($c.Handle) -and
            [BahnAutoWin32_20261103]::IsWindowEnabled($c.Handle)) {
            if([BahnAutoWin32_20261103]::PostMessage($c.Handle,0x00F5,[IntPtr]::Zero,[IntPtr]::Zero)) {
                return $true
            }
        }
    }
    return $false
}
$failed = $false
try {
    Log "=== Bahnsteig OneClick - safe Relux automation ==="
    if (!(Test-Path "$root\.git")) { throw "Git project not found." }
    if (!(Test-Path $dxf)) { throw "V0.4 DXF not found." }
    if (!(Test-Path $source)) { throw "Official DB photometry download not found." }
    $ldts=@(Get-ChildItem $source -Recurse -File | Where-Object { $_.Extension -ieq ".ldt" })
    if ($ldts.Count -lt 3) { throw "Expected 3 original LDT files, found $($ldts.Count)." }
    New-Item -ItemType Directory -Path $target -Force | Out-Null
    foreach($f in $ldts) {
        $dest=Join-Path $target $f.Name
        if (Test-Path $dest) {
            if ((Get-FileHash $f.FullName).Hash -ne (Get-FileHash $dest).Hash) {
                throw "Conflict in existing LDT (not overwritten): $dest"
            }
        } else {
            Copy-Item -LiteralPath $f.FullName -Destination $dest
        }
    }
    Log "DB LDT: $($ldts.Count) original photometry files checked and preserved."
    $lightingCsv=Join-Path $relux "Leuchtenansatz_DB_V0.4.csv"
    $simarisCsv=Join-Path $simaris "Lastenansatz_DB_V0.5.csv"
    if (!(Test-Path $lightingCsv) -or !(Test-Path $simarisCsv)) {
        throw "V0.4 or V0.5 preparation missing. Originals were not changed."
    }
    $dbRows=@(Import-Csv $lightingCsv -Delimiter ";")
    if ($dbRows.Count -ne 12) { throw "Expected 12 lighting positions." }
    $unresolved=@($dbRows | Where-Object { !$_.Leistung_W -or !$_.Montagehoehe_m })
    Log "Lighting entries: 12. Entries missing power OR mounting height: $($unresolved.Count)."
    Log "No automatic claim of Relux lux compliance or SIMARIS network design."

    $apps=@(Get-Process -Name "reluxPro" -ErrorAction SilentlyContinue |
        Where-Object { $_.MainWindowHandle -ne [IntPtr]::Zero -and $_.MainWindowTitle -match "Relux" } |
        Sort-Object Id -Descending)
    if ($apps.Count -eq 0) { throw "ReluxDesktop is not running." }
    $app=$apps[0];$handle=$app.MainWindowHandle
    if (!(Focus-Relux $handle $app.Id)) { throw "Could not focus Relux window." }
    Log "Relux PID: $($app.Id)."
    Save-ReluxScreenshot $handle "01_before"
    $elements=Get-ReluxElements $handle
    $newProject=@($elements | Where-Object {
        $_.Current.Name -eq "New project" -and !$_.Current.IsOffscreen
    })
    $meta=Find-ReluxDialog $app.Id "(?i)Enter project data|Projektangaben|Projektdaten"
    if ($meta.Count -eq 0 -and $newProject.Count -gt 0) {
        # Verified 1665x900 Relux screenshot: exterior-with-CAD card centre near 24.8% width, 41% height.
        $r=Get-ReluxRect $handle
        $w=$r.Right-$r.Left;$h=$r.Bottom-$r.Top
        if($w -lt 1050 -or $h -lt 670) {throw "Unexpected window resolution. Refusing blind click."}
        $x=$r.Left+[int]($w*0.247)
        $y=$r.Top+[int]($h*0.41)
        Log "Selecting Exterior with CAD plan at verified relative location."
        Click-Relux $x $y
        Start-Sleep -Milliseconds 1100
        $meta=Find-ReluxDialog $app.Id "(?i)Enter project data|Projektangaben|Projektdaten"
        # Relux can host its data dialog inside the same top-level window.
        if($meta.Count -eq 0) {
            $edits=Get-Edits $handle
            if($edits.Count -ne 5) { throw "Project data dialog not confirmed after click. No further GUI actions." }
        }
    }

    # Select the owned project-data dialog where available.
    $dialogHandle=$handle
    if($meta.Count -eq 1) { $dialogHandle=$meta[0].Handle }
    $fields=Get-Edits $dialogHandle
    if($fields.Count -ne 5) { throw "Five metadata fields not detected. Input stopped safely." }
    Log "Found five project data fields."

    $values=@(
        "B50HZ-DEMO-V04",
        "Bahnsteigmodernisierung 120 x 4 m",
        "Bahnsteigbeleuchtung 50 Hz",
        "Portfolio-Demoprojekt",
        "Elektroplanung Demo"
    )
    for($i=0;$i -lt 5;$i++) {
        $field=$fields[$i];$wanted=$values[$i]
        $vp=$null
        if($field.TryGetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern,[ref]$vp) -and !$vp.Current.IsReadOnly) {
            $vp.SetValue($wanted)
            if($vp.Current.Value -ne $wanted) { throw "Metadata field $($i+1) failed verification." }
        } else {
            $field.SetFocus()
            Set-Clipboard -Value $wanted
            [System.Windows.Forms.SendKeys]::SendWait("^a")
            [System.Windows.Forms.SendKeys]::SendWait("^v")
            Start-Sleep -Milliseconds 90
            [System.Windows.Forms.SendKeys]::SendWait("^a")
            [System.Windows.Forms.SendKeys]::SendWait("^c")
            if((Get-Clipboard -Raw).Trim() -ne $wanted) { throw "Field $($i+1) did not accept value." }
        }
    }
    Log "Project metadata verified."
    Save-ReluxScreenshot $handle "02_project_data"

    $advanced=Invoke-Named $dialogHandle "^(?i:OK|Next|Weiter|Continue|Create|Erstellen|Fertigstellen|Finish|\u00DCbernehmen)$"
    if (!$advanced -and $dialogHandle -ne $handle) {
        # Only on a confirmed, dedicated, owned dialog: IDOK is the native default button.
        $advanced=[BahnAutoWin32_20261103]::PostMessage($dialogHandle,0x0111,[IntPtr]1,[IntPtr]::Zero)
    }
    if (!$advanced) {
        $fields[0].SetFocus()
        [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
        $advanced=$true
    }
    Log "Requested transition from project metadata."
    Start-Sleep -Milliseconds 1300
    Save-ReluxScreenshot $handle "03_after_metadata"
    $afterEdits=Get-Edits $handle
    $metaAfter=Find-ReluxDialog $app.Id "(?i)Enter project data|Projektangaben|Projektdaten"
    if ($metaAfter.Count -gt 0) { throw "Relux data dialog stayed open. No further action." }
    if ($afterEdits.Count -eq 5 -and $dialogHandle -eq $handle) {
        Log "Warning: five edit fields still present; wizard may not have advanced."
    }

    # Automatic CAD file chooser when Relux opens the native Windows file picker.
    $openDialogs=Find-ReluxDialog $app.Id "^(?i:Open|\u00D6ffnen|Datei \u00F6ffnen|Select CAD file|CAD-Datei \u00F6ffnen)$"
    if($openDialogs.Count -eq 0) {
        $browse=Invoke-Named $handle "^(?i:Browse|Durchsuchen|\.\.\.|Select file|Datei ausw\u00E4hlen|Datei w\u00E4hlen)$"
        if($browse) {Start-Sleep -Milliseconds 650}
        $openDialogs=Find-ReluxDialog $app.Id "^(?i:Open|\u00D6ffnen|Datei \u00F6ffnen|Select CAD file|CAD-Datei \u00F6ffnen)$"
    }
    if($openDialogs.Count -eq 1) {
        $picker=[System.Windows.Automation.AutomationElement]::FromHandle($openDialogs[0].Handle)
        $controls=$picker.FindAll([System.Windows.Automation.TreeScope]::Descendants,
            [System.Windows.Automation.Condition]::TrueCondition)
        $nameBoxes=@($controls | Where-Object {
            $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Edit -and
            ($_.Current.AutomationId -eq "1148" -or $_.Current.Name -match "(?i)file name|dateiname")
        })
        if($nameBoxes.Count -eq 1) {
            $vp=$null
            if($nameBoxes[0].TryGetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern,[ref]$vp)) {
                $vp.SetValue($dxf)
                if($vp.Current.Value -eq $dxf) {
                    $nameBoxes[0].SetFocus()
                    [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
                    Log "DXF path entered into native file chooser."
                }
            }
        }
    } else {
        Log "No native CAD file chooser confirmed. Wizard may need further controls."
    }
    Start-Sleep -Milliseconds 800
    Save-ReluxScreenshot $handle "04_cad_step"

    $rdf=@(Get-ChildItem $relux -File -ErrorAction SilentlyContinue | Where-Object {$_.Extension -ieq ".rdf"})
    $reluxPdf=Join-Path $root "06_Berichte\Relux_Beleuchtungsbericht.pdf"
    $simPdf=Join-Path $root "06_Berichte\SIMARIS_Netzberechnung.pdf"
    Log ("Relux native project (.rdf): " + $rdf.Count)
    Log ("Relux calculation PDF: " + (Test-Path $reluxPdf))
    Log ("SIMARIS calculation PDF: " + (Test-Path $simPdf))
    $simProcess=@(Get-Process -ErrorAction SilentlyContinue | Where-Object { $_.ProcessName -match "(?i)simaris" })
    Log ("SIMARIS running processes: " + $simProcess.Count)
    Log "END: no simulated electrical dimensions or Relux lighting levels have been fabricated."
}
catch {
    $failed = $true
    Log ("STOPPED SAFELY: " + $_.Exception.Message)
}
finally {
    $notes | Set-Content -Path $log -Encoding UTF8
    if ($null -ne $oldClipboard) {
        try { Set-Clipboard -Value $oldClipboard } catch { }
    }
    Log "Report: $log"
    Log "Original V0.2/V0.3 and main Git branch preserved."
}
if ($failed) { exit 1 }