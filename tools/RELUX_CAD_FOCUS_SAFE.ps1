#requires -Version 5.1
# Relux 2026 CAD import: fallback based on keyboard focus and file edit bounds.
# Continue the existing "Import CAD plan" window. Never overwrite CAD source files.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

if (-not ('ReluxWinCad20261103' -as [type])) {
Add-Type @'
using System;
using System.Text;
using System.Runtime.InteropServices;
public static class ReluxWinCad20261103 {
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT {public int Left,Top,Right,Bottom;}
    [StructLayout(LayoutKind.Sequential)]
    public struct GUITHREADINFO {
        public uint cbSize,flags;
        public IntPtr hwndActive,hwndFocus,hwndCapture,hwndMenuOwner,hwndMoveSize,hwndCaret;
        public RECT rcCaret;
    }
    [DllImport("user32.dll")] public static extern bool ShowWindow(IntPtr hwnd,int cmd);
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr hwnd);
    [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
    [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr hwnd,out uint procId);
    [DllImport("user32.dll")] public static extern bool GetGUIThreadInfo(uint thread,ref GUITHREADINFO data);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr hwnd,out RECT bounds);
    [DllImport("user32.dll",CharSet=CharSet.Unicode)]
    public static extern int GetClassName(IntPtr hwnd,StringBuilder text,int length);
    [DllImport("user32.dll",CharSet=CharSet.Unicode)]
    public static extern int GetWindowText(IntPtr hwnd,StringBuilder text,int length);
    [DllImport("user32.dll")] public static extern bool SetCursorPos(int x,int y);
    [DllImport("user32.dll")] public static extern void mouse_event(uint flags,uint x,uint y,uint dwData,UIntPtr extra);
}
'@
}
$root=Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'bahnsteig-50hz-elektroplanung-demo'
$dxf=Join-Path $root '05_Relux_Beleuchtung\Bahnsteig_Relux_Import_V0.4.dxf'
$folder=Join-Path $env:USERPROFILE ('Downloads\Bahnsteig-CAD-Focus-'+(Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $folder -Force | Out-Null
$log=New-Object System.Collections.Generic.List[string]
$failed=$false
$oldClipboard=try {Get-Clipboard -Raw -ErrorAction Stop} catch {$null}
function Status([string]$message) {$log.Add($message);Write-Host $message}
function Rect([IntPtr]$h) {
    $r=New-Object ReluxWinCad20261103+RECT
    if(-not [ReluxWinCad20261103]::GetWindowRect($h,[ref]$r)) {return $null}
    return [pscustomobject]@{Left=$r.Left;Top=$r.Top;Width=$r.Right-$r.Left;Height=$r.Bottom-$r.Top}
}
function Snap([IntPtr]$h,[string]$name) {
    $r=Rect $h
    if(!$r -or $r.Width -lt 300 -or $r.Height -lt 300){return}
    $bitmap=New-Object System.Drawing.Bitmap($r.Width,$r.Height)
    $graphics=[System.Drawing.Graphics]::FromImage($bitmap)
    try {
        $graphics.CopyFromScreen($r.Left,$r.Top,0,0,$bitmap.Size)
        $bitmap.Save((Join-Path $folder ($name+'.png')),[System.Drawing.Imaging.ImageFormat]::Png)
    } finally {$graphics.Dispose();$bitmap.Dispose()}
}
function Focused() {
    $foreground=[ReluxWinCad20261103]::GetForegroundWindow()
    $processId=[uint32]0
    $thread=[ReluxWinCad20261103]::GetWindowThreadProcessId($foreground,[ref]$processId)
    if($thread -eq 0){return $null}
    $info=New-Object ReluxWinCad20261103+GUITHREADINFO
    $info.cbSize=[System.Runtime.InteropServices.Marshal]::SizeOf(
        [type]'ReluxWinCad20261103+GUITHREADINFO')
    if(-not [ReluxWinCad20261103]::GetGUIThreadInfo($thread,[ref]$info)){return $null}
    if($info.hwndFocus -eq [IntPtr]::Zero){return $null}
    $c=New-Object System.Text.StringBuilder(256)
    $t=New-Object System.Text.StringBuilder(256)
    [ReluxWinCad20261103]::GetClassName($info.hwndFocus,$c,$c.Capacity) | Out-Null
    [ReluxWinCad20261103]::GetWindowText($info.hwndFocus,$t,$t.Capacity) | Out-Null
    return [pscustomobject]@{Handle=$info.hwndFocus;Class=$c.ToString();Text=$t.ToString();
       Bounds=(Rect $info.hwndFocus);ProcessId=[int]$processId}
}
function Click([int]$x,[int]$y) {
    [ReluxWinCad20261103]::SetCursorPos($x,$y) | Out-Null
    Start-Sleep -Milliseconds 120
    [ReluxWinCad20261103]::mouse_event(2,0,0,0,[UIntPtr]::Zero)
    [ReluxWinCad20261103]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
}
try {
    if(!(Test-Path "$root\.git") -or !(Test-Path $dxf)) {throw 'Project or V0.4 DXF missing.'}
    $apps=@(Get-Process -Name reluxPro -ErrorAction SilentlyContinue | Where-Object {
        $_.MainWindowHandle -ne [IntPtr]::Zero
    })
    $selection=@($apps | Where-Object {$_.Id -eq 7248})
    if($selection.Count -ne 1) {
        if($apps.Count -ne 1) {throw 'Cannot choose unique Relux window. No input sent.'}
        $selection=@($apps[0])
    }
    $app=$selection[0]
    $handle=$app.MainWindowHandle
    [ReluxWinCad20261103]::ShowWindow($handle,9) | Out-Null
    [ReluxWinCad20261103]::SetForegroundWindow($handle) | Out-Null
    Start-Sleep -Milliseconds 500
    $start=Focused
    if(!$start -or $start.ProcessId -ne $app.Id) {throw 'Relux is not foreground.'}
    Status 'Relux focused; scanning keyboard-focus controls without assuming window size.'
    Snap $handle '01_before'
    $field=$null
    for($n=0;$n -lt 18;$n++) {
        $f=Focused
        if($f -and $f.ProcessId -eq $app.Id -and $f.Bounds -and
           $f.Class -match '(?i)edit|rich' -and
           $f.Bounds.Width -ge 390 -and $f.Bounds.Width -le 540 -and
           $f.Bounds.Height -ge 18 -and $f.Bounds.Height -le 55) {
            $field=$f
            break
        }
        [System.Windows.Forms.SendKeys]::SendWait('{TAB}')
        Start-Sleep -Milliseconds 110
    }
    if(!$field) {throw 'CAD text edit not found via keyboard focus. No text entered.'}
    Status ('CAD input discovered: '+$field.Class+' '+$field.Bounds.Width+'x'+$field.Bounds.Height)
    Set-Clipboard -Value $dxf
    [System.Windows.Forms.SendKeys]::SendWait('^a')
    [System.Windows.Forms.SendKeys]::SendWait('^v')
    Start-Sleep -Milliseconds 200
    Set-Clipboard -Value '__NO_TEXT_COPIED__'
    [System.Windows.Forms.SendKeys]::SendWait('^a')
    [System.Windows.Forms.SendKeys]::SendWait('^c')
    Start-Sleep -Milliseconds 200
    if((Get-Clipboard -Raw).Trim() -ne $dxf) {throw 'Read-back mismatch: CAD path was not entered into input.'}
    Status 'Original DXF path verified inside filename edit.'
    Snap $handle '02_filled'
    $clicked=$false
    for($n=0;$n -lt 10;$n++) {
        [System.Windows.Forms.SendKeys]::SendWait('{TAB}')
        Start-Sleep -Milliseconds 100
        $f=Focused
        if($f -and $f.ProcessId -eq $app.Id -and $f.Text -match '^(?i:Next|Next >|Weiter|Weiter >)$') {
            [System.Windows.Forms.SendKeys]::SendWait(' ')
            $clicked=$true
            Status 'Next activated via keyboard focus.'
            break
        }
    }
    if(!$clicked) {
        # Verified CAD wizard screenshot positions RELATIVE TO THE INPUT FIELD.
        # x Next - x input = 568, y Next - y input = 446 (at reference width 442).
        # This avoids relying on the application's outer window dimensions.
        $b=$field.Bounds
        if($b.Width -ge 430 -and $b.Width -le 455 -and
           $b.Height -ge 24 -and $b.Height -le 34) {
            $x=$b.Left+568
            $y=$b.Top+446
            $window=Rect $handle
            if($x -gt $window.Left -and $x -lt ($window.Left+$window.Width) -and
               $y -gt $window.Top -and $y -lt ($window.Top+$window.Height)) {
                Click $x $y
                $clicked=$true
                Status 'Next requested at CAD field-relative screenshot position.'
            }
        }
    }
    if(!$clicked) {throw 'Next control was not discoverable. DXF filename entered; no click sent.'}
    Start-Sleep -Milliseconds 900
    Snap $handle '03_after_next'
    Status 'Next requested; stage transition and actual Relux computation NOT verified.'
} catch {
    $failed=$true
    Status ('SAFE STOP: '+$_.Exception.Message)
} finally {
    $log | Set-Content -Path (Join-Path $folder 'Status.txt') -Encoding UTF8
    if($null -ne $oldClipboard) {try {Set-Clipboard -Value $oldClipboard} catch {}}
    Write-Host ('Diagnostic folder: '+$folder)
    Write-Host 'No CAD source overwritten; no Git commits made.'
}
if($failed) {exit 1}
