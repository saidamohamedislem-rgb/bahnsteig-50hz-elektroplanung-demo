#requires -version 5.1
# Load two LDT product types into the CURRENT Relux V0.6 product selector.
# This is not a luminaire placement or a lighting calculation.
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
if(-not ('BahnLdtUI26' -as [type])){
Add-Type @'
using System;using System.Text;using System.Collections.Generic;using System.Runtime.InteropServices;
public static class BahnLdtUI26{
 public class W{public IntPtr H;public int PID;public string Name;public string Class;}
 public delegate bool Callback(IntPtr hwnd,IntPtr data);
 [DllImport("user32.dll")]public static extern bool EnumWindows(Callback fn,IntPtr data);
 [DllImport("user32.dll")]public static extern bool IsWindowVisible(IntPtr hwnd);
 [DllImport("user32.dll")]public static extern IntPtr GetForegroundWindow();
 [DllImport("user32.dll")]public static extern bool SetForegroundWindow(IntPtr hwnd);
 [DllImport("user32.dll")]public static extern uint GetWindowThreadProcessId(IntPtr hwnd,out uint pid);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)]public static extern int GetWindowText(IntPtr hwnd,StringBuilder b,int n);
 [DllImport("user32.dll",CharSet=CharSet.Unicode)]public static extern int GetClassName(IntPtr hwnd,StringBuilder b,int n);
 [DllImport("user32.dll")]public static extern bool GetWindowRect(IntPtr hwnd,out RECT r);
 [DllImport("user32.dll")]public static extern bool SetCursorPos(int x,int y);
 [DllImport("user32.dll")]public static extern void mouse_event(uint f,uint x,uint y,uint data,UIntPtr extra);
 [StructLayout(LayoutKind.Sequential)]public struct RECT{public int Left,Top,Right,Bottom;}
 public static W[] List(){
  var list=new List<W>();
  EnumWindows((hwnd,data)=>{
   if(!IsWindowVisible(hwnd))return true;
   uint pid;GetWindowThreadProcessId(hwnd,out pid);
   var b=new StringBuilder(300);var c=new StringBuilder(100);
   GetWindowText(hwnd,b,b.Capacity);GetClassName(hwnd,c,c.Capacity);
   list.Add(new W{H=hwnd,PID=(int)pid,Name=b.ToString(),Class=c.ToString()});
   return true;
  },IntPtr.Zero);
  return list.ToArray();
 }
}
'@
}
$downloads=Join-Path $env:USERPROFILE 'Downloads'
$report=Join-Path $downloads ('Relux_LDT_Import_'+(Get-Date -Format 'yyyyMMdd_HHmmss'))
New-Item -ItemType Directory -Path $report -Force|Out-Null
$log=New-Object System.Collections.Generic.List[string]
$originalClipboard=try{Get-Clipboard -Raw -ErrorAction Stop}catch{$null}
$ok=$false
function Say([string]$value){$log.Add($value);Write-Host $value}
function Bounds([IntPtr]$h){
 $r=New-Object BahnLdtUI26+RECT
 if(-not [BahnLdtUI26]::GetWindowRect($h,[ref]$r)){throw 'Cannot measure dialog.'}
 [pscustomobject]@{X=$r.Left;Y=$r.Top;W=$r.Right-$r.Left;H=$r.Bottom-$r.Top}
}
function Click([int]$x,[int]$y){
 [BahnLdtUI26]::SetCursorPos($x,$y)|Out-Null
 Start-Sleep -Milliseconds 170
 [BahnLdtUI26]::mouse_event(2,0,0,0,[UIntPtr]::Zero)
 [BahnLdtUI26]::mouse_event(4,0,0,0,[UIntPtr]::Zero)
}
function Selector([int]$processId){
 $items=@([BahnLdtUI26]::List()|Where-Object {
  $_.PID -eq $processId -and $_.Name -match '^(?i:Product selection|Produktauswahl)$'
 })
 if($items.Count -ne 1){throw ('Relux Product selection count = '+$items.Count)}
 $box=Bounds $items[0].H
 if($box.W -lt 850 -or $box.W -gt 1250 -or $box.H -lt 550 -or $box.H -gt 850){
  throw ('Unexpected product dialog dimensions '+$box.W+'x'+$box.H)
 }
 [pscustomobject]@{H=$items[0].H;B=$box;PID=$processId}
}
function At($dialog,[double]$x,[double]$y){
 Click ([int]($dialog.B.X+$dialog.B.W*$x)) ([int]($dialog.B.Y+$dialog.B.H*$y))
}
function Screenshot($dialog,[string]$tag){
 $b=$dialog.B
 $bmp=New-Object System.Drawing.Bitmap($b.W,$b.H)
 $g=[System.Drawing.Graphics]::FromImage($bmp)
 try{$g.CopyFromScreen($b.X,$b.Y,0,0,$bmp.Size);
   $bmp.Save((Join-Path $report ($tag+'.png')),[System.Drawing.Imaging.ImageFormat]::Png)}
 finally{$g.Dispose();$bmp.Dispose()}
}
function ImportLdt($dlg,[string]$file){
 Say ('Selecting '+[IO.Path]::GetFileName($file))
 [BahnLdtUI26]::SetForegroundWindow($dlg.H)|Out-Null
 Start-Sleep -Milliseconds 180
 At $dlg 0.104 0.332
 Start-Sleep -Milliseconds 530
 $fg=[BahnLdtUI26]::GetForegroundWindow()
 $candidate=@([BahnLdtUI26]::List()|Where-Object{$_.H -eq $fg})
 if($candidate.Count -ne 1 -or $candidate[0].PID -ne $dlg.PID -or
   ($candidate[0].Class -ne '#32770' -and $candidate[0].Name -notmatch '(?i)open|ffnen')){
  throw 'File picker not confirmed; no text typed.'
 }
 [System.Windows.Forms.SendKeys]::SendWait('%n')
 Start-Sleep -Milliseconds 130
 Set-Clipboard -Value $file
 [System.Windows.Forms.SendKeys]::SendWait('^a')
 [System.Windows.Forms.SendKeys]::SendWait('^v')
 Start-Sleep -Milliseconds 150
 Set-Clipboard -Value '__NO_LDT__'
 [System.Windows.Forms.SendKeys]::SendWait('^a')
 [System.Windows.Forms.SendKeys]::SendWait('^c')
 Start-Sleep -Milliseconds 150
 if((Get-Clipboard -Raw).Trim() -ne $file){throw 'Picker filename read-back failed. No Enter sent.'}
 [System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
 Start-Sleep -Milliseconds 630
 $dlg=Selector $dlg.PID
 At $dlg 0.335 0.278
 Start-Sleep -Milliseconds 120
 Set-Clipboard -Value '__NO_LDT__'
 [System.Windows.Forms.SendKeys]::SendWait('^a')
 [System.Windows.Forms.SendKeys]::SendWait('^c')
 Start-Sleep -Milliseconds 150
 $read=(Get-Clipboard -Raw).Trim()
 if($read -notlike ('*'+[IO.Path]::GetFileName($file)+'*')){
  Screenshot $dlg 'FileSelected_Unverified'
  throw ('Relux product filename read-back was '+$read+'; no Add click.')
 }
 Say 'LDT path confirmed in Relux product selector.'
 Screenshot $dlg ('Selected_'+[IO.Path]::GetFileNameWithoutExtension($file))
 At $dlg 0.125 0.708
 Start-Sleep -Milliseconds 450
 Say 'Add >> requested; verify product acceptance in Relux.'
}
try{
 $apps=@(Get-Process reluxPro -ErrorAction SilentlyContinue|Where-Object{
  $_.MainWindowHandle -ne [IntPtr]::Zero -and $_.MainWindowTitle -match '^Bahnsteig_Beleuchtung_V0\.6 - ReluxDesktop'
 })
 if($apps.Count -ne 1){throw 'Cannot identify exactly one V0.6 process.'}
 $ready=@(Get-ChildItem $downloads -Directory -Filter 'Bahnsteig_Relux_Ready_*' |
  Sort-Object LastWriteTime -Descending)
 $ldt=$null
 foreach($d in $ready){
  $try=Join-Path $d.FullName '01_LDT_Photometry'
  if(Test-Path $try){$ldt=$try;break}
 }
 if(!$ldt){throw 'No prepared LDT directory.'}
 $files=@(
  (Join-Path $ldt 'DB_Schmidt_Strahl_18p5W_BB_4000K.LDT'),
  (Join-Path $ldt 'DB_Schmidt_Strahl_14W_4000K.LDT')
 )
 foreach($f in $files){if(!(Test-Path -LiteralPath $f)){throw ('LDT not found: '+$f)}}
 $selector=Selector $apps[0].Id
 Say 'Existing V0.6 product selector found.'
 Screenshot $selector '01_Before'
 foreach($f in $files){$selector=Selector $apps[0].Id;ImportLdt $selector $f}
 $selector=Selector $apps[0].Id
 Screenshot $selector '03_After'
 Say 'Two Add requests sent; physical luminaire placement NOT performed.'
 $ok=$true
}catch{Say ('SAFE STOP: '+$_.Exception.Message)}
finally{
 $log|Set-Content -LiteralPath (Join-Path $report 'Status.txt') -Encoding UTF8
 if($null -ne $originalClipboard){try{Set-Clipboard -Value $originalClipboard}catch{}}
 Write-Host ('Report: '+$report)
 Write-Host 'V0.5, V0.6 and GitHub main not modified by this script.'
}
if(!$ok){exit 1}
