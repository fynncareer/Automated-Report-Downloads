Scrape daily and weekly sales reports from Amazon and other retailers, to be ingested into the Data Warehouse. 

BACKGROUND:

When I joined the Application Support team at Penguin Random House it was a Support persons job to manually download files from each site, change the data in excel, amend the filename and save it into the data warehouse load location. There were many files to change and it was hard not to make a manual mistake or two doing this (I made many!). It would usually take the whole afternoon (3-4 hours) for the unlucky person who had to do the manual process that week as part of the team rota.

We had a broken python script that was built using Selenium, a library for web automation testing, to automatically download some of the files from Amazon. It wasn't working but I was grateful to inherit it because I had some exposure to python and a test environment to play with. I fixed that script after some trial and error. I wanted to do more, so volunteered to do the manual process every week which gave me enough time to work on them.

Over the next few months I wrote a suite of scripts so each file was downloaded, updated, renamed and transferred. I learned several python libraries like pandas, selenium, parimiko and openpyxl to achieve this. I tackled web elements on several different sites (and learned to dislike front end web development, but 'inspect element' was my friend). I made the process more modular with functions and config files to avoid repeating code. This repository is the end result. 

My team mates were very pleased they no longer had to manually do the process and I improved my python skills. I really enjoyed the whole process and have to say its a project that I'm proud to have accomplished. I would love to utilise my python skills more in future.


SCRIPTS:

Made to be run on any day of the week and the daily files take 2 optional arguments from the command line (--start_date and --end_date) so a backlog of files can be run through. At one point we had over a hundred missing files for some reports in the data warehouse, and using these scripts we managed to fill the backlog completely.


The folders are grouped:
1. Amazon Reporting - 12 scripts for a variety of Amazon reports. Split between digital and physical sales. All logged into the same Amazon site, just selecting different report data.
2. Retail Data - 5 scripts for Apple ebooks, Apple iTunes, ASDA, Google and Amazon sftp data. Each script is more custom.


How the scripts are structured:
1. Functions are held in functions.py
2. Configuration items (logins, source/target filenames and folders) are held in config.xlsx
3. All scripts are run from control_script.py.


Note: For privacy I have removed any web elements, internal file/server path names and login details.

