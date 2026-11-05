# Recalculate a model workbook in Microsoft Excel (macros off, links not refreshed), save it and clear the last-author field,
# so model_workbook.py check can compare Excel's own results with the specification.
# Optionally cycle the scenario selector and record named outputs for every case.
#
# powershell -NoProfile -ExecutionPolicy Bypass -File recalc_excel.ps1 -Workbook model.xlsx `
#   [-Selector "Cover!C9" -Cases 3 -Outputs "Statements!K50,Valuation!D24" -Report excel.json]
param(
    [Parameter(Mandatory = $true)][string]$Workbook,
    [string]$Selector = '',
    [int]$Cases = 0,
    [string]$Outputs = '',
    [string]$Report = ''
)
$ErrorActionPreference = 'Stop'
$path = (Resolve-Path -LiteralPath $Workbook).Path
$excel = $null; $book = $null
function Get-Range($ref) {
    $i = $ref.LastIndexOf('!')
    $book.Worksheets.Item($ref.Substring(0, $i).Trim("'")).Range($ref.Substring($i + 1))
}
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false; $excel.DisplayAlerts = $false
    $excel.AutomationSecurity = 3; $excel.AskToUpdateLinks = $false
    $book = $excel.Workbooks.Open($path, 0, $false)
    $records = @()
    if ($Selector -and $Cases -gt 0) {
        $cell = Get-Range $Selector
        $original = $cell.Value2
        foreach ($case in 1..$Cases) {
            $cell.Value2 = [double]$case
            $excel.CalculateFullRebuild()
            $values = [ordered]@{}
            foreach ($ref in ($Outputs -split ',' | Where-Object { $_ })) { $values[$ref] = (Get-Range $ref).Value2 }
            $records += [PSCustomObject]@{ case = $case; outputs = $values }
        }
        $cell.Value2 = $original
    }
    $excel.CalculateFullRebuild()
    $errors = 0
    foreach ($ws in $book.Worksheets) {
        $used = $ws.UsedRange
        foreach ($c in $used.Cells) { if ($c.Value2 -is [int] -and $c.Text -like '#*') { $errors++ } }
    }
    $book.Save()
    $result = [PSCustomObject]@{ engine = 'Microsoft Excel'; version = $excel.Version; macrosDisabled = $true; linksRefreshed = $false; errorCells = $errors; cases = $records }
    $json = $result | ConvertTo-Json -Depth 6
    if ($Report) { $json | Set-Content -LiteralPath $Report -Encoding UTF8 }
    $json
} finally {
    if ($book) { $book.Close($false) }
    if ($excel) { $excel.Quit() }
    foreach ($o in @($book, $excel)) { if ($o) { [void][Runtime.InteropServices.Marshal]::FinalReleaseComObject($o) } }
}
# Excel stamps the user's name as last author on save; clear it so a shared model names no one.
Add-Type -AssemblyName System.IO.Compression, System.IO.Compression.FileSystem
$zip = [IO.Compression.ZipFile]::Open($path, 'Update')
try {
    $entry = $zip.GetEntry('docProps/core.xml')
    if ($entry) {
        $reader = New-Object IO.StreamReader($entry.Open()); $xml = $reader.ReadToEnd(); $reader.Close()
        $xml = $xml -replace '<cp:lastModifiedBy>[^<]*</cp:lastModifiedBy>', '<cp:lastModifiedBy></cp:lastModifiedBy>'
        $entry.Delete()
        $writer = New-Object IO.StreamWriter($zip.CreateEntry('docProps/core.xml').Open()); $writer.Write($xml); $writer.Close()
    }
} finally { $zip.Dispose() }
