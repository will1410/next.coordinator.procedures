Removing guarantors from adult accounts.

Sometimes the process that promotes a child from one of the minor categories to its corresponding adult category can fail to remove all of the guarantor information from the account.  To remove all of the data from the adult's account:

1. Run report 3145 - GHW - ADMINREPORT - Adult patrons with guarantors.  The SQL for this report is:

```
SELECT
  borrowers.borrowernumber,
  borrowers.cardnumber,
  borrowers.surname,
  borrowers.firstname,
  borrowers.title,
  borrowers.othernames,
  borrowers.initials,
  borrowers.streetnumber,
  borrowers.streettype,
  borrowers.address,
  borrowers.address2,
  borrowers.city,
  borrowers.state,
  borrowers.zipcode,
  borrowers.country,
  borrowers.email,
  borrowers.phone,
  borrowers.mobile,
  borrowers.fax,
  borrowers.emailpro,
  borrowers.phonepro,
  borrowers.B_streetnumber,
  borrowers.B_streettype,
  borrowers.B_address,
  borrowers.B_address2,
  borrowers.B_city,
  borrowers.B_state,
  borrowers.B_zipcode,
  borrowers.B_country,
  borrowers.B_email,
  borrowers.B_phone,
  borrowers.dateofbirth,
  borrowers.branchcode,
  borrowers.categorycode,
  borrowers.dateenrolled,
  borrowers.dateexpiry,
  borrowers.date_renewed,
  borrowers.gonenoaddress,
  borrowers.lost,
  borrowers.debarred,
  borrowers.contactname,
  borrowers.contactfirstname,
  borrowers.contacttitle,
  borrowers.guarantorid,
  borrowers.relationship,
  borrowers.ethnicity,
  borrowers.ethnotes,
  borrowers.sex,
  borrowers.sort1,
  borrowers.sort2,
  borrowers.altcontactfirstname,
  borrowers.altcontactsurname,
  borrowers.altcontactaddress1,
  borrowers.altcontactaddress2,
  borrowers.altcontactaddress3,
  borrowers.altcontactstate,
  borrowers.altcontactzipcode,
  borrowers.altcontactcountry,
  borrowers.altcontactphone
FROM
  borrowers
WHERE
  (borrowers.dateofbirth <= CurDate() - INTERVAL 18 YEAR or borrowers.dateofbirth IS NULL) AND
  (borrowers.guarantorid is not null OR
  borrowers.guarantorid <> "" OR
  borrowers.contactname <> "" OR
  borrowers.contactfirstname <> "" OR
  borrowers.contacttitle <> "")
ORDER BY
  borrowers.borrowernumber
```

2. Download the results as a csv file.

3. Process the csv file so that the cardnumber column is formatted as numbers with no decimals, all date columns are formatted as mm/dd/yyyy, all rogue comas are removed, and all phone numbers are formatted as numbers with no decimals.  This VBA macro should do all of those things:

```
Sub Adults_w_guarantors()
'
' Adults with guarantors
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
    Range([AO2], [AO:AO].Find("*", [AO1], , , xlByRows, xlPrevious)).Select
    Selection.Replace What:="*", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range([AP2], [AP:AP].Find("*", [AP1], , , xlByRows, xlPrevious)).Select
    Selection.Replace What:="*", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range([AQ2], [AQ:AQ].Find("*", [AQ1], , , xlByRows, xlPrevious)).Select
    Selection.Replace What:="*", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range([AR2], [AR:AR].Find("*", [AR1], , , xlByRows, xlPrevious)).Select
    Selection.Replace What:="*", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Range([AS2], [AS:AS].Find("*", [AS1], , , xlByRows, xlPrevious)).Select
    Selection.Replace What:="*", Replacement:="", LookAt:=xlPart, _
        SearchOrder:=xlByRows, MatchCase:=False, SearchFormat:=False, _
        ReplaceFormat:=False
    Columns("Q:Q").Select
    Selection.NumberFormat = "0"
End Sub
```



4. Use the patron import tool to overwrite the data for these patrons in Koha.  Use the options "Match on cardnumber;" "Overwrite the existing one with this;" and "Replace only included patron attributes."
