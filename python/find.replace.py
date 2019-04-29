# Read in the file
with open('C:/Users/George/Documents/GitHub/next.coordinator.procedures/python/file.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('<<branches.branchcode>>', '[% branch.branchcode %]')
filedata = filedata.replace('<<branches.branchname>>', '[% branch.branchname %]')
filedata = filedata.replace('<<branches.branchaddress1>>', '[% branch.branchaddress1 %]')
filedata = filedata.replace('<<branches.branchaddress2>>', '[% branch.branchaddress2 %]')
filedata = filedata.replace('<<branches.branchaddress3>>', '[% branch.branchaddress3 %]')
filedata = filedata.replace('<<branches.branchzip>>', '[% branch.branchzip %]')
filedata = filedata.replace('<<branches.branchcity>>', '[% branch.branchcity %]')
filedata = filedata.replace('<<branches.branchstate>>', '[% branch.branchstate %]')
filedata = filedata.replace('<<branches.branchcountry>>', '[% branch.branchcountry %]')
filedata = filedata.replace('<<branches.branchphone>>', '[% branch.branchphone %]')
filedata = filedata.replace('<<branches.branchfax>>', '[% branch.branchfax %]')
filedata = filedata.replace('<<branches.branchemail>>', '[% branch.branchemail %]')
filedata = filedata.replace('<<branches.branchreplyto>>', '[% branch.branchreplyto %]')
filedata = filedata.replace('<<branches.branchreturnpath>>', '[% branch.branchreturnpath %]')
filedata = filedata.replace('<<branches.branchurl>>', '[% branch.branchurl %]')
filedata = filedata.replace('<<branches.issuing>>', '[% branch.issuing %]')
filedata = filedata.replace('<<branches.branchip>>', '[% branch.branchip %]')
filedata = filedata.replace('<<branches.branchprinter>>', '[% branch.branchprinter %]')
filedata = filedata.replace('<<branches.branchnotes>>', '[% branch.branchnotes %]')
filedata = filedata.replace('<<branches.opac_info>>', '[% branch.opac_info %]')
filedata = filedata.replace('<<branches.geolocation>>', '[% branch.geolocation %]')
filedata = filedata.replace('<<branches.marcorgcode>>', '[% branch.marcorgcode %]')
filedata = filedata.replace('<<branches.pickup_location>>', '[% branch.pickup_location %]')
filedata = filedata.replace('<<biblio.biblionumber>>', '[% biblio.biblionumber %]')
filedata = filedata.replace('<<biblio.frameworkcode>>', '[% biblio.frameworkcode %]')
filedata = filedata.replace('<<biblio.author>>', '[% biblio.author %]')
filedata = filedata.replace('<<biblio.title>>', '[% biblio.title %]')
filedata = filedata.replace('<<biblio.unititle>>', '[% biblio.unititle %]')
filedata = filedata.replace('<<biblio.notes>>', '[% biblio.notes %]')
filedata = filedata.replace('<<biblio.serial>>', '[% biblio.serial %]')
filedata = filedata.replace('<<biblio.seriestitle>>', '[% biblio.seriestitle %]')
filedata = filedata.replace('<<biblio.copyrightdate>>', '[% biblio.copyrightdate %]')
filedata = filedata.replace('<<biblio.datecreated>>', '[% biblio.datecreated %]')
filedata = filedata.replace('<<biblio.abstract>>', '[% biblio.abstract %]')
filedata = filedata.replace('<<biblioitems.biblioitemnumber>>', '[% biblioitems.biblioitemnumber %]')
filedata = filedata.replace('<<biblioitems.biblionumber>>', '[% biblioitems.biblionumber %]')
filedata = filedata.replace('<<biblioitems.volume>>', '[% biblioitems.volume %]')
filedata = filedata.replace('<<biblioitems.number>>', '[% biblioitems.number %]')
filedata = filedata.replace('<<biblioitems.itemtype>>', '[% biblioitems.itemtype %]')
filedata = filedata.replace('<<biblioitems.isbn>>', '[% biblioitems.isbn %]')
filedata = filedata.replace('<<biblioitems.issn>>', '[% biblioitems.issn %]')
filedata = filedata.replace('<<biblioitems.ean>>', '[% biblioitems.ean %]')
filedata = filedata.replace('<<biblioitems.publicationyear>>', '[% biblioitems.publicationyear %]')
filedata = filedata.replace('<<biblioitems.publishercode>>', '[% biblioitems.publishercode %]')
filedata = filedata.replace('<<biblioitems.volumedate>>', '[% biblioitems.volumedate %]')
filedata = filedata.replace('<<biblioitems.volumedesc>>', '[% biblioitems.volumedesc %]')
filedata = filedata.replace('<<biblioitems.collectiontitle>>', '[% biblioitems.collectiontitle %]')
filedata = filedata.replace('<<biblioitems.collectionissn>>', '[% biblioitems.collectionissn %]')
filedata = filedata.replace('<<biblioitems.collectionvolume>>', '[% biblioitems.collectionvolume %]')
filedata = filedata.replace('<<biblioitems.editionstatement>>', '[% biblioitems.editionstatement %]')
filedata = filedata.replace('<<biblioitems.editionresponsibility>>', '[% biblioitems.editionresponsibility %]')
filedata = filedata.replace('<<biblioitems.illus>>', '[% biblioitems.illus %]')
filedata = filedata.replace('<<biblioitems.pages>>', '[% biblioitems.pages %]')
filedata = filedata.replace('<<biblioitems.notes>>', '[% biblioitems.notes %]')
filedata = filedata.replace('<<biblioitems.size>>', '[% biblioitems.size %]')
filedata = filedata.replace('<<biblioitems.place>>', '[% biblioitems.place %]')
filedata = filedata.replace('<<biblioitems.lccn>>', '[% biblioitems.lccn %]')
filedata = filedata.replace('<<biblioitems.url>>', '[% biblioitems.url %]')
filedata = filedata.replace('<<biblioitems.cn_source>>', '[% biblioitems.cn_source %]')
filedata = filedata.replace('<<biblioitems.cn_class>>', '[% biblioitems.cn_class %]')
filedata = filedata.replace('<<biblioitems.cn_item>>', '[% biblioitems.cn_item %]')
filedata = filedata.replace('<<biblioitems.cn_suffix>>', '[% biblioitems.cn_suffix %]')
filedata = filedata.replace('<<biblioitems.cn_sort>>', '[% biblioitems.cn_sort %]')
filedata = filedata.replace('<<biblioitems.agerestriction>>', '[% biblioitems.agerestriction %]')
filedata = filedata.replace('<<biblioitems.totalissues>>', '[% biblioitems.totalissues %]')
filedata = filedata.replace('<<items.itemnumber>>', '[% item.itemnumber %]')
filedata = filedata.replace('<<items.biblionumber>>', '[% item.biblionumber %]')
filedata = filedata.replace('<<items.biblioitemnumber>>', '[% item.biblioitemnumber %]')
filedata = filedata.replace('<<items.barcode>>', '[% item.barcode %]')
filedata = filedata.replace('<<items.dateaccessioned>>', '[% item.dateaccessioned | $KohaDates %]')
filedata = filedata.replace('<<items.booksellerid>>', '[% item.booksellerid %]')
filedata = filedata.replace('<<items.homebranch>>', '[% item.homebranch %]')
filedata = filedata.replace('<<items.price>>', '[% item.price %]')
filedata = filedata.replace('<<items.replacementprice>>', '[% item.replacementprice %]')
filedata = filedata.replace('<<items.replacementpricedate>>', '[% item.replacementpricedate %]')
filedata = filedata.replace('<<items.datelastborrowed>>', '[% item.datelastborrowed | $KohaDates %]')
filedata = filedata.replace('<<items.datelastseen>>', '[% item.datelastseen | $KohaDates %]')
filedata = filedata.replace('<<items.stack>>', '[% item.stack %]')
filedata = filedata.replace('<<items.notforloan>>', '[% item.notforloan %]')
filedata = filedata.replace('<<items.damaged>>', '[% item.damaged %]')
filedata = filedata.replace('<<items.damaged_on>>', '[% item.damaged_on %]')
filedata = filedata.replace('<<items.itemlost>>', '[% item.itemlost %]')
filedata = filedata.replace('<<items.itemlost_on>>', '[% item.itemlost_on | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<items.withdrawn>>', '[% item.withdrawn %]')
filedata = filedata.replace('<<items.withdrawn_on>>', '[% item.withdrawn_on | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<items.itemcallnumber>>', '[% item.itemcallnumber %]')
filedata = filedata.replace('<<items.coded_location_qualifier>>', '[% item.coded_location_qualifier %]')
filedata = filedata.replace('<<items.issues>>', '[% item.issues %]')
filedata = filedata.replace('<<items.renewals>>', '[% item.renewals %]')
filedata = filedata.replace('<<items.reserves>>', '[% item.reserves %]')
filedata = filedata.replace('<<items.restricted>>', '[% item.restricted %]')
filedata = filedata.replace('<<items.itemnotes>>', '[% item.itemnotes %]')
filedata = filedata.replace('<<items.itemnotes_nonpublic>>', '[% item.itemnotes_nonpublic %]')
filedata = filedata.replace('<<items.holdingbranch>>', '[% item.holdingbranch %]')
filedata = filedata.replace('<<items.paidfor>>', '[% item.paidfor %]')
filedata = filedata.replace('<<items.location>>', '[% item.location %]')
filedata = filedata.replace('<<items.permanent_location>>', '[% item.permanent_location %]')
filedata = filedata.replace('<<items.onloan>>', '[% item.onloan | $KohaDates %]')
filedata = filedata.replace('<<items.cn_source>>', '[% item.cn_source %]')
filedata = filedata.replace('<<items.cn_sort>>', '[% item.cn_sort %]')
filedata = filedata.replace('<<items.ccode>>', '[% item.ccode %]')
filedata = filedata.replace('<<items.materials>>', '[% item.materials %]')
filedata = filedata.replace('<<items.uri>>', '[% item.uri %]')
filedata = filedata.replace('<<items.itype>>', '[% item.itype %]')
filedata = filedata.replace('<<items.more_subfields_xml>>', '[% item.more_subfields_xml %]')
filedata = filedata.replace('<<items.enumchron>>', '[% item.enumchron %]')
filedata = filedata.replace('<<items.copynumber>>', '[% item.copynumber %]')
filedata = filedata.replace('<<items.stocknumber>>', '[% item.stocknumber %]')
filedata = filedata.replace('<<items.new_status>>', '[% item.new_status %]')
filedata = filedata.replace('<<borrowers.borrowernumber>>', '[% borrower.borrowernumber %]')
filedata = filedata.replace('<<borrowers.cardnumber>>', '[% borrower.cardnumber %]')
filedata = filedata.replace('<<borrowers.surname>>', '[% borrower.surname %]')
filedata = filedata.replace('<<borrowers.firstname>>', '[% borrower.firstname %]')
filedata = filedata.replace('<<borrowers.title>>', '[% borrower.title %]')
filedata = filedata.replace('<<borrowers.othernames>>', '[% borrower.othernames %]')
filedata = filedata.replace('<<borrowers.initials>>', '[% borrower.initials %]')
filedata = filedata.replace('<<borrowers.streetnumber>>', '[% borrower.streetnumber %]')
filedata = filedata.replace('<<borrowers.streettype>>', '[% borrower.streettype %]')
filedata = filedata.replace('<<borrowers.address>>', '[% borrower.address %]')
filedata = filedata.replace('<<borrowers.address2>>', '[% borrower.address2 %]')
filedata = filedata.replace('<<borrowers.city>>', '[% borrower.city %]')
filedata = filedata.replace('<<borrowers.state>>', '[% borrower.state %]')
filedata = filedata.replace('<<borrowers.zipcode>>', '[% borrower.zipcode %]')
filedata = filedata.replace('<<borrowers.country>>', '[% borrower.country %]')
filedata = filedata.replace('<<borrowers.email>>', '[% borrower.email %]')
filedata = filedata.replace('<<borrowers.phone>>', '[% borrower.phone %]')
filedata = filedata.replace('<<borrowers.mobile>>', '[% borrower.mobile %]')
filedata = filedata.replace('<<borrowers.fax>>', '[% borrower.fax %]')
filedata = filedata.replace('<<borrowers.emailpro>>', '[% borrower.emailpro %]')
filedata = filedata.replace('<<borrowers.phonepro>>', '[% borrower.phonepro %]')
filedata = filedata.replace('<<borrowers.B_streetnumber>>', '[% borrower.B_streetnumber %]')
filedata = filedata.replace('<<borrowers.B_streettype>>', '[% borrower.B_streettype %]')
filedata = filedata.replace('<<borrowers.B_address>>', '[% borrower.B_address %]')
filedata = filedata.replace('<<borrowers.B_address2>>', '[% borrower.B_address2 %]')
filedata = filedata.replace('<<borrowers.B_city>>', '[% borrower.B_city %]')
filedata = filedata.replace('<<borrowers.B_state>>', '[% borrower.B_state %]')
filedata = filedata.replace('<<borrowers.B_zipcode>>', '[% borrower.B_zipcode %]')
filedata = filedata.replace('<<borrowers.B_country>>', '[% borrower.B_country %]')
filedata = filedata.replace('<<borrowers.B_email>>', '[% borrower.B_email %]')
filedata = filedata.replace('<<borrowers.B_phone>>', '[% borrower.B_phone %]')
filedata = filedata.replace('<<borrowers.dateofbirth>>', '[% borrower.dateofbirth | $KohaDates %]')
filedata = filedata.replace('<<borrowers.branchcode>>', '[% borrower.branchcode %]')
filedata = filedata.replace('<<borrowers.categorycode>>', '[% borrower.categorycode %]')
filedata = filedata.replace('<<borrowers.dateenrolled>>', '[% borrower.dateenrolled | $KohaDates %]')
filedata = filedata.replace('<<borrowers.dateexpiry>>', '[% borrower.dateexpiry | $KohaDates %]')
filedata = filedata.replace('<<borrowers.date_renewed>>', '[% borrower.date_renewed %]')
filedata = filedata.replace('<<borrowers.gonenoaddress>>', '[% borrower.gonenoaddress %]')
filedata = filedata.replace('<<borrowers.lost>>', '[% borrower.lost %]')
filedata = filedata.replace('<<borrowers.debarred>>', '[% borrower.debarred | $KohaDates %]')
filedata = filedata.replace('<<borrowers.debarredcomment>>', '[% borrower.debarredcomment %]')
filedata = filedata.replace('<<borrowers.contactname>>', '[% borrower.contactname %]')
filedata = filedata.replace('<<borrowers.contactfirstname>>', '[% borrower.contactfirstname %]')
filedata = filedata.replace('<<borrowers.contacttitle>>', '[% borrower.contacttitle %]')
filedata = filedata.replace('<<borrowers.guarantorid>>', '[% borrower.guarantorid %]')
filedata = filedata.replace('<<borrowers.borrowernotes>>', '[% borrower.borrowernotes %]')
filedata = filedata.replace('<<borrowers.relationship>>', '[% borrower.relationship %]')
filedata = filedata.replace('<<borrowers.ethnicity>>', '[% borrower.ethnicity %]')
filedata = filedata.replace('<<borrowers.ethnotes>>', '[% borrower.ethnotes %]')
filedata = filedata.replace('<<borrowers.sex>>', '[% borrower.sex %]')
filedata = filedata.replace('<<borrowers.password>>', '[% borrower.password %]')
filedata = filedata.replace('<<borrowers.flags>>', '[% borrower.flags %]')
filedata = filedata.replace('<<borrowers.userid>>', '[% borrower.userid %]')
filedata = filedata.replace('<<borrowers.opacnote>>', '[% borrower.opacnote %]')
filedata = filedata.replace('<<borrowers.contactnote>>', '[% borrower.contactnote %]')
filedata = filedata.replace('<<borrowers.sort1>>', '[% borrower.sort1 %]')
filedata = filedata.replace('<<borrowers.sort2>>', '[% borrower.sort2 %]')
filedata = filedata.replace('<<borrowers.altcontactfirstname>>', '[% borrower.altcontactfirstname %]')
filedata = filedata.replace('<<borrowers.altcontactsurname>>', '[% borrower.altcontactsurname %]')
filedata = filedata.replace('<<borrowers.altcontactaddress1>>', '[% borrower.altcontactaddress1 %]')
filedata = filedata.replace('<<borrowers.altcontactaddress2>>', '[% borrower.altcontactaddress2 %]')
filedata = filedata.replace('<<borrowers.altcontactaddress3>>', '[% borrower.altcontactaddress3 %]')
filedata = filedata.replace('<<borrowers.altcontactstate>>', '[% borrower.altcontactstate %]')
filedata = filedata.replace('<<borrowers.altcontactzipcode>>', '[% borrower.altcontactzipcode %]')
filedata = filedata.replace('<<borrowers.altcontactcountry>>', '[% borrower.altcontactcountry %]')
filedata = filedata.replace('<<borrowers.altcontactphone>>', '[% borrower.altcontactphone %]')
filedata = filedata.replace('<<borrowers.smsalertnumber>>', '[% borrower.smsalertnumber %]')
filedata = filedata.replace('<<borrowers.sms_provider_id>>', '[% borrower.sms_provider_id %]')
filedata = filedata.replace('<<borrowers.privacy>>', '[% borrower.privacy %]')
filedata = filedata.replace('<<borrowers.privacy_guarantor_checkouts>>', '[% borrower.privacy_guarantor_checkouts %]')
filedata = filedata.replace('<<borrowers.checkprevcheckout>>', '[% borrower.checkprevcheckout %]')
filedata = filedata.replace('<<borrowers.updated_on>>', '[% borrower.updated_on %]')
filedata = filedata.replace('<<borrowers.lastseen>>', '[% borrower.lastseen %]')
filedata = filedata.replace('<<borrowers.lang>>', '[% borrower.lang %]')
filedata = filedata.replace('<<borrowers.login_attempts>>', '[% borrower.login_attempts %]')
filedata = filedata.replace('<<borrowers.overdrive_auth_token>>', '[% borrower.overdrive_auth_token %]')
filedata = filedata.replace('<<opac_news.idnew>>', '[% news.idnew %]')
filedata = filedata.replace('<<opac_news.branchcode>>', '[% news.branchcode %]')
filedata = filedata.replace('<<opac_news.title>>', '[% news.title %]')
filedata = filedata.replace('<<opac_news.content>>', '[% news.content %]')
filedata = filedata.replace('<<opac_news.lang>>', '[% news.lang %]')
filedata = filedata.replace('<<opac_news.expirationdate>>', '[% news.expirationdate %]')
filedata = filedata.replace('<<opac_news.number>>', '[% news.number %]')
filedata = filedata.replace('<<opac_news.borrowernumber>>', '[% news.borrowernumber %]')
filedata = filedata.replace('<<issues.issue_id>>', '[% checkout.issue_id %]')
filedata = filedata.replace('<<issues.borrowernumber>>', '[% checkout.borrowernumber %]')
filedata = filedata.replace('<<issues.itemnumber>>', '[% checkout.itemnumber %]')
filedata = filedata.replace('<<issues.date_due>>', '[% checkout.date_due | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<issues.branchcode>>', '[% checkout.branchcode %]')
filedata = filedata.replace('<<issues.returndate>>', '[% checkout.returndate | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<issues.lastreneweddate>>', '[% checkout.lastreneweddate | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<issues.renewals>>', '[% checkout.renewals %]')
filedata = filedata.replace('<<issues.auto_renew>>', '[% checkout.auto_renew %]')
filedata = filedata.replace('<<issues.auto_renew_error>>', '[% checkout.auto_renew_error %]')
filedata = filedata.replace('<<issues.issuedate>>', '[% checkout.issuedate | $KohaDates with_hours => 1 %]')
filedata = filedata.replace('<<issues.onsite_checkout>>', '[% checkout.onsite_checkout %]')
filedata = filedata.replace('<<issues.note>>', '[% checkout.note %]')
filedata = filedata.replace('<<issues.notedate>>', '[% checkout.notedate %]')
filedata = filedata.replace('<<issues.noteseen>>', '[% checkout.noteseen %]')

# Write the file out again
with open('C:/Users/George/Documents/GitHub/next.coordinator.procedures/python/file.txt', 'w') as file:
  file.write(filedata)
