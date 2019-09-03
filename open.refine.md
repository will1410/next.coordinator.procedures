Open refine

Prep a 3257 file for open refine

```
Sub Open_refine_prep()
'
' Open refine prep
'

'
    Columns("B:B").Select
    Selection.NumberFormat = "0"
    Range("AF:AF,AI:AI,AJ:AJ,AK:AK,AN:AN").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Cells.Select
    Selection.Replace What:=",", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range("AF:AF,AI:AI,AJ:AJ,AK:AK,AN:AN").Select
    Selection.Replace What:="0000-00-00", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range("AF:AF,AI:AI,AJ:AJ,AK:AK,AN:AN").Select
    Selection.Replace What:="12/31/9999", Replacement:="12/31/2099", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Columns("Q:Q").Select
    Selection.NumberFormat = "0"
End Sub
```
