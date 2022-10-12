# cibc_reimbursement_formating
Automating formating for a report to my parents about spendings.

First, make sure the modules in requirements.txt are installed.
Then, go to the cibc website, 
https://www.cibconline.cibc.com/ebm-resources/public/banking/cibc/client/web/index.html#/signon . Sign in. 

Go to MyAccounts > Download Transactions. There, pick the appropriate account, and select "All Available" in Display.
Download the transaction, name it "cibc_data.csv", and place it in a "data" folder within the current directory.
If needed, check settings.py and modify the file names there.

Then, run main.py, and answer the input questions (You can leave them blank). 

Once the program finished running, open the resulting excel document.

You can obtain a "tableau croisé dynamique", or pivot table, using this excel document. 
It lets you analyze what each of "Maybe", "Yes" and "No" represent in "Loss", the amnt of $ spent in each category.

For the pivot table, go in Insertion > Pivot Table (tableau croisé dynamique in French). Press OK. 

Slide "Answer" to Lines (Lignes),
Slide "Name" to Lines (Lignes) under Answer,
Slide "Loss" to Values (Valeurs),
Slide "Reason" to Filters (Filtres),
and you will have the completed Pivot Table.

Save, and send this document to whoever it concerns.
