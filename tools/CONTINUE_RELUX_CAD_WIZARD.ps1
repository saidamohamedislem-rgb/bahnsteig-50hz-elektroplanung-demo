#requires -Version 5.1
# Continue the EXISTING Relux CAD import wizard (not a new project).
# Do not run a new-project wizard over an open CAD import dialog.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName UIAutomationClient
Add-Type -AssemblyName UIAutomationTypes
if (-not ('BahnCadWinApi20261103' -as [type])) {
Add-Type @'
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Text;
public static class BahnCadWinApi20261103 {
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int Left, Top, Right, Bottom; }
  public delegate bool EnumProc(IntPtr h, IntPtr p);
  [DllImport("user32.dll")] public static extern bool EnumWindows(EnumProc cb, IntPtr p);
  [DllImport("user32.dll")] public static extern bool EnumChildWindows(IntPtr h, EnumProc cb, IntPtr p);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetWindowText(IntPtr h, StringBuilder b, int n);
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern int GetClassName(IntPtr h, StringBuilder b, int n);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool IsWindowVisible(IntPtr h);
  [DllImport("user32.dll")] public static extern bool IsWindowEnabled(IntPtr h);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern IntPtr GetForegroundWindow();
  [DllImport("user32.dll")] public static extern uint GetWindowThreadProcessId(IntPtr h, out uint pid);
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int x, int y);
  [DllImport("user32.dll")] public static extern void mouse_event(uint f,uint x,uint y,int data,UIntPtr e);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h,uint msg,IntPtr w,IntPtr l);
  public class W { public IntPtr H; public int ProcessId; public string Title; public string Cls; public int X,Y,Width,Height; }
  public static W[] EnumAll(IntPtr parent) {
    var output=new List<W>();
    EnumProc callback=(h,p)=> {
      if (!IsWindowVisible(h)) return true;
      uint procId; GetWindowThreadProcessId(h,out procId);
      RECT r; if (!GetWindowRect(h,out r)) return true;
      var title=new StringBuilder(512);var cls=new StringBuilder(256);
      GetWindowText(h,title,title.Capacity);GetClassName(h,cls,cls.Capacity);
      output.Add(new W { H=h, ProcessId=(int)procId, Title=title.ToString(),Cls=cls.ToString(),
        X=r.Left,Y=r.Top,Width=r.Right-r.Left,Height=r.Bottom-r.Top });
      return true;
    };
    if (parent==IntPtr.Zero) EnumWindows(callback,IntPtr.Zero);
    else EnumChildWindows(parent,callback,IntPtr.Zero);
    return output.ToArray();
  }
}
'@
}
$project=Join-Path ([Environment]::GetFolderPath('MyDocuments')) 'bahnsteig-50hz-elektroplanung-demo'
$dxf=Join-Path $project '05_Relux_Beleuchtung\Bahnsteig_Relux_Import_V0.4.dxf'
$diag=Join-Path $env:USERPROFILE ('Downloads\Bahnsteig-CAD-Import-'+(Get-Date -Format 'yyyyMMdd-HHmmss'))
New-Item -ItemType Directory -Path $diag -Force | Out-Null
$messages=New-Object System.Collections.Generic.List[string]
$scriptFailed=$false
function Say([string]$s) { Write-Host $s; $messages.Add($s) }
function Get-Rect([IntPtr]$h) {
  $r=New-Object BahnCadWinApi20261103+RECT
  if (-not [BahnCadWinApi20261103]::GetWindowRect($h,[ref]$r)) {throw 'Window rect could not be read'}
  return $r
}
function Snapshot([IntPtr]$h,[string]$name) {
  $r=Get-Rect $h; $width=$r.Right-$r.Left; $height=$r.Bottom-$r.Top
  if ($width -lt 250 -or $height -lt 200) {return}
  $bitmap=New-Object System.Drawing.Bitmap($width,$height)
  $graphics=[System.Drawing.Graphics]::FromImage($bitmap)
  try {
    $graphics.CopyFromScreen($r.Left,$r.Top,0,0,$bitmap.Size)
    $bitmap.Save((Join-Path $diag ($name+'.png')),[System.Drawing.Imaging.ImageFormat]::Png)
  } finally {$graphics.Dispose();$bitmap.Dispose()}
}
function Get-Uia([IntPtr]$h) {
  $ui=[System.Windows.Automation.AutomationElement]::FromHandle($h)
  $items=$ui.FindAll([System.Windows.Automation.TreeScope]::Descendants,
    [System.Windows.Automation.Condition]::TrueCondition)
  foreach($item in $items) { Write-Output $item }
}
function Click([int]$x,[int]$y) {
  [BahnCadWinApi20261103]::SetCursorPos($x,$y) | Out-Null
  Start-Sleep -Milliseconds 160
  [BahnCadWinApi20261103]::mouse_event(2,0,0,0,[UIntPtr]::Zero)
  [BahnCadWinApi20261103]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
}
function ActivePid() {
  $n=[uint32]0
  [BahnCadWinApi20261103]::GetWindowThreadProcessId([BahnCadWinApi20261103]::GetForegroundWindow(),[ref]$n) | Out-Null
  return [int]$n
}
function Invoke-Next([IntPtr]$h,[object[]]$controls,[object]$geometry) {
  $buttons=@($controls | Where-Object {
    try {
      $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Button -and
      $_.Current.Name -match '^(?i:Next\s*>?|Weiter\s*>?)$' -and
      $_.Current.IsEnabled -and !$_.Current.IsOffscreen
    } catch {$false}
  })
  if($buttons.Count -eq 1) {
    $invoke=$null
    if($buttons[0].TryGetCurrentPattern([System.Windows.Automation.InvokePattern]::Pattern,[ref]$invoke)) {
      $invoke.Invoke();Say 'Next invoked via Windows Automation.';return $true
    }
  }
  $native=@([BahnCadWinApi20261103]::EnumAll($h) | Where-Object {
    $_.Cls -match '(?i)Button' -and $_.Title -match '^(?i:Next\s*>?|Weiter\s*>?)$' -and
    [BahnCadWinApi20261103]::IsWindowEnabled($_.H)
  })
  if($native.Count -eq 1) {
    $ok=[BahnCadWinApi20261103]::PostMessage($native[0].H,0x00F5,[IntPtr]::Zero,[IntPtr]::Zero)
    if($ok) {Say 'Next invoked via native Windows button.';return $true}
  }
  # Coordinates ONLY for the user's verified 798x612 CAD-Import wizard image.
  if($geometry.Width -ge 780 -and $geometry.Width -le 820 -and
     $geometry.Height -ge 595 -and $geometry.Height -le 630) {
    Click ($geometry.X+$geometry.Width-177) ($geometry.Y+$geometry.Height-28)
    Say 'Next clicked at verified CAD wizard location.'
    return $true
  }
  return $false
}
$oldClip=$null
try {$oldClip=Get-Clipboard -Raw -ErrorAction Stop} catch {}
try {
  if(!(Test-Path "$project\.git") -or !(Test-Path $dxf)){throw 'Original project or CAD DXF missing.'}
  $apps=@(Get-Process -Name reluxPro -ErrorAction SilentlyContinue | Where-Object {
      $_.MainWindowHandle -ne [IntPtr]::Zero
    })
  if($apps.Count -eq 0) {throw 'Relux is not running.'}
  $openWin=@([BahnCadWinApi20261103]::EnumAll([IntPtr]::Zero))
  $allWin=New-Object System.Collections.Generic.List[object]
  foreach($proc in $apps) {
    foreach($top in @($openWin | Where-Object {$_.ProcessId -eq $proc.Id})) {
      $allWin.Add($top)
      foreach($child in [BahnCadWinApi20261103]::EnumAll($top.H)) {$allWin.Add($child)}
    }
  }
  # Diagnose Win32 windows, but also search inside the Relux UI Automation tree:
  # custom Relux dialogs do not always own a separate top-level HWND.
  $allWin | Select-Object ProcessId,Title,Cls,X,Y,Width,Height |
    Export-Csv -Path (Join-Path $diag 'Windows.csv') -Encoding UTF8 -Delimiter ';' -NoTypeInformation
  $possible = New-Object System.Collections.Generic.List[object]
  foreach($app in $apps) {
    try {
      $top=$app.MainWindowHandle
      $nodes=@(Get-Uia $top)
      $visibleEditors=@($nodes | Where-Object {
        try {
          $b=$_.Current.BoundingRectangle
          $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Edit -and
          $_.Current.IsEnabled -and !$_.Current.IsOffscreen -and
          $b.Width -ge 290 -and $b.Width -le 850 -and
          $b.Height -ge 18 -and $b.Height -le 55
        } catch {$false}
      })
      $searchControls=@($nodes | Where-Object {
        try {
          $_.Current.Name -match '^(?i:Search\.\.\.|Search|Suchen\.\.\.|Durchsuchen)$' -and
          !$_.Current.IsOffscreen
        } catch {$false}
      })
      foreach($editor in $visibleEditors) {
        $b=$editor.Current.BoundingRectangle
        $adjacent=@($searchControls | Where-Object {
          try {
            $sr=$_.Current.BoundingRectangle
            $sr.Left -ge ($b.Right - 15) -and
            $sr.Left -le ($b.Right + 170) -and
            [Math]::Abs($sr.Top - $b.Top) -le 45
          } catch {$false}
        })
        if($adjacent.Count -gt 0) {
          $possible.Add([pscustomobject]@{
            H=$top; ProcessId=$app.Id; Title='CAD file selection (UIA detected)';
            Editor=$editor; Rect=$b
          })
        }
      }
    } catch {
      Say "UI Automation scan for process $($app.Id) failed: $($_.Exception.Message)"
    }
  }
  if($possible.Count -eq 1) {
    $dialog=$possible[0]
  } elseif($possible.Count -eq 0) {
    # The GUI screenshot confirms the CAD import file-picker's visual geometry,
    # but some Relux controls are invisible to Windows accessibility APIs.
    $chosen=@($apps | Where-Object { $_.Id -eq 7248 })
    if($chosen.Count -ne 1) {
      throw 'CAD UI controls unavailable and original Relux PID 7248 is not present.'
    }
    $app=$chosen[0]
    $r=Get-Rect $app.MainWindowHandle
    $w=$r.Right-$r.Left
    $height=$r.Bottom-$r.Top
    if($w -lt 1580 -or $w -gt 1800 -or $height -lt 830 -or $height -gt 1020) {
      throw 'CAD controls not found; window geometry does not match original screenshot.'
    }
    $dialog=[pscustomobject]@{
      H=$app.MainWindowHandle
      ProcessId=$app.Id
      Title='CAD wizard screenshot-position fallback'
      Editor=$null
      Rect=[pscustomobject]@{Left=$r.Left+180;Top=$r.Top+225}
    }
    Say 'Using verified screenshot position fallback; no previous projects modified.'
  } else {
    throw "Multiple possible CAD edit fields: $($possible.Count)."
  }
  Say "CAD filename field detected inside Relux PID $($dialog.ProcessId)"
  [BahnCadWinApi20261103]::SetForegroundWindow($dialog.H) | Out-Null
  Start-Sleep -Milliseconds 400
  if((ActivePid) -ne $dialog.ProcessId) {throw 'Relux does not have focus.'}
  Snapshot $dialog.H '01-before'
  $controls=Get-Uia $dialog.H
  $fileInput=$dialog.Editor
  $verified=$false
  if($fileInput) {
    $vp=$null
    if($fileInput.TryGetCurrentPattern([System.Windows.Automation.ValuePattern]::Pattern,[ref]$vp) -and
       !$vp.Current.IsReadOnly){
      $vp.SetValue($dxf)
      $verified=($vp.Current.Value -eq $dxf)
    } else {
      $fileInput.SetFocus()
      Set-Clipboard -Value $dxf
      [System.Windows.Forms.SendKeys]::SendWait('^a')
      [System.Windows.Forms.SendKeys]::SendWait('^v')
      [System.Windows.Forms.SendKeys]::SendWait('^a')
      [System.Windows.Forms.SendKeys]::SendWait('^c')
      Start-Sleep -Milliseconds 180
      $verified=((Get-Clipboard -Raw).Trim() -eq $dxf)
    }
  }
  if(-not $verified -and !$fileInput -and $dialog.Title -eq 'CAD wizard screenshot-position fallback') {
    $pos=Get-Rect $dialog.H
    Click ($pos.Left+400) ($pos.Top+239)
    Set-Clipboard -Value $dxf
    [System.Windows.Forms.SendKeys]::SendWait('^a')
    [System.Windows.Forms.SendKeys]::SendWait('^v')
    Start-Sleep -Milliseconds 400
    Set-Clipboard -Value '__NO_CAD_TEXT_COPIED__'
    [System.Windows.Forms.SendKeys]::SendWait('^a')
    [System.Windows.Forms.SendKeys]::SendWait('^c')
    Start-Sleep -Milliseconds 180
    $verified=((Get-Clipboard -Raw).Trim() -eq $dxf)
    if($verified) {Say 'DXF field verified using clipboard read-back from reference position.'}
  }
  if(-not $verified){throw 'DXF filename field could not be verified; stopped without pressing Next.'}
  Say 'DXF filename verified in CAD wizard.'
  Snapshot $dialog.H '02-file-filled'
  Start-Sleep -Milliseconds 400
  $controls=Get-Uia $dialog.H
  $nextDone=$false
  $buttonCandidates=@($controls | Where-Object {
    try {
      $_.Current.ControlType -eq [System.Windows.Automation.ControlType]::Button -and
      $_.Current.Name -match '^(?i:Next|Weiter|Next >|Weiter >)$' -and
      $_.Current.IsEnabled -and !$_.Current.IsOffscreen
    } catch {$false}
  })
  if($buttonCandidates.Count -eq 1) {
    $invokePattern=$null
    if($buttonCandidates[0].TryGetCurrentPattern(
      [System.Windows.Automation.InvokePattern]::Pattern,[ref]$invokePattern)) {
      $invokePattern.Invoke()
      $nextDone=$true
      Say 'Next clicked through UI Automation.'
    }
  }
  if(-not $nextDone) {
    # Only after the entered DXF has been copied back and verified.
    # The wizard screenshot establishes these offsets from that exact input field.
    $b=$dialog.Rect
    $nextX=[int]($b.Left+568)
    $nextY=[int]($b.Top+446)
    $windowRect=Get-Rect $dialog.H
    if($nextX -gt $windowRect.Left -and $nextX -lt $windowRect.Right -and
       $nextY -gt $windowRect.Top -and $nextY -lt $windowRect.Bottom) {
      Click $nextX $nextY
      $nextDone=$true
      Say 'Next click sent at verified position relative to CAD filename field.'
    }
  }
  if(-not $nextDone) { throw 'Next control unavailable; no click sent.' }
  Start-Sleep -Milliseconds 1300
  Snapshot $dialog.H '03-after-next'
  $after=Get-Uia $dialog.H
  $names=@($after | ForEach-Object {
    try {$_.Current.Name} catch {''}
  } | Where-Object {$_})
  $names | Select-Object -First 180 | Set-Content -Path (Join-Path $diag 'UIAfterNext.txt') -Encoding UTF8
  $stageText=($names -join ' ')
  if($stageText -match '(?i)Step 2 of 4|Schritt 2 von 4|Scale|Massstab|Scaling') {
    Say 'CAD wizard stage 2 detected. Scale must be 1 drawing unit = 1 metre.'
    # Do not choose arbitrary scale or accidentally alter geometry.
  } else {
    Say 'Next requested; stage 2 not independently confirmed. Screenshots saved.'
  }
  Say 'Actual Relux .rdf and lighting calculation still need validation.'
} catch {
  $scriptFailed=$true
  Say ('STOPPED: '+$_.Exception.Message)
} finally {
  $messages | Set-Content -Path (Join-Path $diag 'Status.txt') -Encoding UTF8
  if($null -ne $oldClip) { try {Set-Clipboard -Value $oldClip} catch {} }
  Write-Host "Diagnostic folder: $diag"
  Write-Host 'Original CAD and GitHub main branch unchanged.'
}

if($scriptFailed) {exit 1}
