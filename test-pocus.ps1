#
#
#
$Pocus = "$PSScriptRoot\Pocus.py"
$list = @() 
for ($i = 0; $i -lt 1000; $i++) {
    $list += $(py $Pocus)
    
}
$list = $list | ConvertFrom-Csv -Delimiter "," -Header "CardPick","ActCard","Status","Card_pos_NUM"
$list | Sort-Object -Property Card_pos_NUM -Descending | Format-Table -AutoSize