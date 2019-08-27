Sub borrowersprocess()
'
' borrowersprocess Macro
'

'
    Columns("A:A").Select
    Selection.NumberFormat = "0"
    Columns("M:M").Select
    Selection.NumberFormat = "0"
    Columns("P:P").Select
    Selection.NumberFormat = "0"
    Columns("AD:AD").Select
    Selection.NumberFormat = "0"
    Columns("AE:AE").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Columns("AH:AH").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Columns("AI:AI").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Columns("AJ:AJ").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Columns("AM:AM").Select
    Selection.NumberFormat = "mm/dd/yyyy"
    Columns("BF:BF").Select
    Selection.NumberFormat = "0"
    Range("A1:ZZ250000").Select
    Selection.Replace What:=",", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
End Sub
