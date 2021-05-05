Scrape daily and weekly sales reports from Amazon and other retailers, to be ingested into the Data Warehouse. 

BACKGROUND:

When I joined the Application Support team at Penguin Random House it was a Support persons job to manually download files from each site, change the data in excel, amend the filename and save it into the data warehouse load location. There were many files to change and it was hard not to make a manual mistake or two doing this (I made many!). It would usually take the whole afternoon (3-4 hours) for the unlucky person who had to do the manual process that week as part of the team rota.

We had a broken python script that was built using Selenium, a library for web automation testing, to automatically download some of the files from Amazon. It wasn't working but I had some exposure to python and I fixed it after some trial and error. I volunteered to do the manual process every week so I could work on the scripts to automate. Over the next few months I wrote a script for every file so it was downloaded, updated, renamed and transferred. I made the process more modular with functions and config files to avoid repeating code. This repository is the end result. My team mates were very pleased they no longer had to manually do the process and I improved my python skills.

SCRIPTS:

Made to be run on any day of the week and the daily files take 2 optional arguments from the command line (--start_date and --end_date) so a backlog of files could be run if need be. We had over a hundred missing files for lesser priority reports, and using these scripts we managed to fill the backlog.


The folders are grouped:
1. Amazon Reporting - 12 scripts for a variety of Amazon reports. Split between digital and physical sales. All logged into the same Amazon site, just selecting different report data.
2. Retail Data - 5 scripts for Apple ebooks, Apple iTunes, ASDA, Google and Amazon sftp data. Each script is more custom.


How the scripts are structured:
1. Functions are held in functions.py
2. Configuration items (logins, source/target filenames and folders) are held in config.xlsx
3. All scripts are run from control_script.py.


Note: For privacy I have removed any web elements, internal file/server path names and login details.

