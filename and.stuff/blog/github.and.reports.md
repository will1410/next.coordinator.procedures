I began working at Northeast Kansas Library System in July of 2016.  NEKLS had a long history of operating a Koha based system.  Beginning in 2008, NEKLS spent several years on LibLime Koha before migrating to community Koha in 2011.  Currently there are 44 libraries operating at 51 locations and during the last 10 years 5 or 6 staff members have been involved in the management of the shared catalog.

One side effect of 5 or 6 staff members managing a Koha installation for over 10 years is that when I started at NEKLS in 2016 we had about 1200 SQL reports.  This situation seems to have arisen for XX reasons.

1. Reports that were written but multiple staff members and were not well documented.

  If someone needed a report, they called or e-mailed our offices, said "I need a report that does X, Y, and Z," and then a staff member wrote a report and called it something like "Report for Library A" with no notes.  A week later if someone from another library called and talked to a different staff member and said, "I need a report that does X, Y, and Z," the other staff member would do a keyword search to see if a report that does X, Y, and Z already exists, but, since the description for the first report only said "Report for Library A," they would end up creating a new report that does X, Y, and Z and then call it "Report for Library B."  This lead to a lot of duplicate reports.

2. The reports that were written were not very flexible.

  If someone needed a report that listed items with lost statuses but limited by item type and someone else needed a report that listed items with lost statuses but limited by collection code, 2 reports were written.  Since I've been working at NEKLS, we've adopted more flexible report writing as described here: https://kohathings.blogspot.com/2017/08/using-autorised-values-tables-and.html

3. Reports that became obsolete or were no longer necessary were never deleted.

  Since we have been using Koha since 2008, we have many reports that no longer work but have not been deleted.

Once a week I try to spend an hour or so reviewing and testing reports and in a month I usually flag 10-25 reports per month for deletion either because they don't work or because the report is a duplicate of a newer report or, frequently, because I absolutely cannot figure out what purpose the report may serve.

Deleting reports is always a tricky business, though, because within a week or to of batch deleting 10-25 reports someone will call and ask "Where is the super special report that _(Insert name of an employee who resigned 2-10 years ago)_ created for me.  I run it every time we have a month with 5 Tuesdays to find out _(Insert some impossibly bizarre and totally confusing concept)_.  Could you bring it back for me?"

In order to make it easier for me to resurrect those _super special_ reports I've begun using Github as an outside repository for our custom SQL.

The process I use and am going to describe involves Koha, Microsoft Excel, Github desktop, and sometimes Atom.  So if you  don't have a Github account, getting that set up would be a good first step.  And if you don't have Github desktop and Atom, you should install those on your computer also.

The next thing you would want to do would be to create a repository.  You can call it whatever you like.  I happened to call min nexpress.sql.

Once the repository has been created, the next step is to clone the repository to your local computer.
