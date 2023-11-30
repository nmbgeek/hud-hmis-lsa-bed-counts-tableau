# hud-hmis-lsa-bed-counts-tableau
Uses your HUD LSA export to see bed counts in Tableau.

You will need to take your LSA Export and combine the sheets in Excel.  The required sheets must be named "Project", "HMISParticipation", "Inventory", and "Organization".  If you don't have Tableau Desktop you can use the Tableau Public client to see the data and modify the PIT date.  There is no client level data so you could also host on Tableau public depending on your organization/CoC's policies for others to be able to review the information.  [Tableau Public can be download here.](https://www.tableau.com/products/public/download)

To use this you can either: 

* Create an Excel woorkbook and add each of the CSVs as a sheet

*OR* 

* Use the csv-zip-to-excel.py to do the work for you.  This is recommended unless you want to manually recompile your xlsx file with every export.

  * To use the python script make sure you have python, pandas, and openpyxl installed.
    * Python 3.9+ should work and can be downloaded here if you don't already have it - https://www.python.org/downloads/
    * Once Python is installed you can install pandas and openpyxl use `pip install pandas openpyxl` from the command line.  If Python wasn't added to your path you may need to add the full path to python before the pip command. If Python was added to your PATH you may need to log off and log back in.
    * To create your xlsx from the zip file use `python csv-zip-to-excel.py c:\path_to_your_export\export_file.zip`  If there are spaces in the path you will need to surround them by quotes.  The output xlsx will be placed in the same folder that the zip was originally located in.
   
Once you have your XLSX file you can then open the Tableau workbook and choose the XLSX file for the data source!

The [PIT Date] variable is set to "2023-01-25" (January 25th, 2023).  You can modify this value to your community's PIT/HIC date.

[Download Tableau Workbook and Python script here](https://github.com/nmbgeek/hud-hmis-lsa-bed-counts-tableau/releases/latest)

![Tableau Preview](./preview.jpg)
