Import-Module -Name Terminal-Icons
Invoke-Expression (& { (zoxide init powershell | Out-String) })
Get-ChildItem "$PROFILE\..\Completions\" | ForEach-Object {
    . $_.FullName
}
oh-my-posh init pwsh --config "~/.mytheme.omp.json" | Invoke-Expression
