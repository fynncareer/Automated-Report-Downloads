from functions import SiteLogin, SelectSalesView, SelectReportingPeriod, SelectDate, SelectColumns, DownloadFile, DateRange
from functions import GetLogin, Dates, GetFiles, StartFireFox, RenameDownloadedFile, SendEmail, LogError, StringReplace, checkEndDateFilesExists
import timeit
import os, sys
import traceback
import datetime 

start_time = timeit.default_timer()

start_date, end_date = Dates("%Y%m%d", sys.argv[0])	
	
job, login, source_location, source_file, target_location, target_file_original, base_url = GetFiles(os.path.basename(sys.argv[0]))
source_file = os.path.join(source_location, source_file)

if os.path.exists(source_file) == True:
	os.remove(source_file) # remove source file if it already exists.
	
def main():
	for source in login.split(', '):
		if end_date: # end_date is empty unless --end_date argparse is given. 
				
			if checkEndDateFilesExists(start_date, end_date, target_location, target_file_original, source):
			
				print("Downloading: {}".format(source))
			
				username, password = GetLogin(source)

				driver = StartFireFox(base_url, source_location, 20)
				
				SiteLogin(driver, username, password)
				
				SelectSalesView(driver, "Shipped Revenue")
				
				SelectReportingPeriod(driver, job, "Daily")	
				
				SelectDate(driver, start_date)	
				
				SelectColumns(driver, job, ["Parent ASIN", "EAN", "ISBN-13", "Brand", "Subcategory", "Category", "Author/Artist", "Binding"])
			
				for x in DateRange(start_date, end_date):
				
					start_date_b = datetime.datetime.strftime(x, "%Y%m%d")
					target_file_b = os.path.join(target_location, target_file_original.format(source[:2], start_date_b))
			
					if os.path.exists(target_file_b) == False: 
					
						SelectDate(driver, start_date_b)
						
						DownloadFile(driver, job)
						
						RenameDownloadedFile(source_file, target_file_b, 120)
						StringReplace(target_file_b, '—', 0.00)
					else:
						print("{} already exists.".format(os.path.basename(target_file_b)))
						
			else:
				print("files for {} already exist.".format(source))
				
		else:
			
			target_file = os.path.join(target_location, target_file_original.format(source[:2], start_date))
			
			if os.path.exists(target_file) == False: 
			
				print("Downloading: {}".format(source))
				
				username, password = GetLogin(source)

				driver = StartFireFox(base_url, source_location, 20)
				
				SiteLogin(driver, username, password)
				
				SelectSalesView(driver, "Shipped Revenue")
				
				SelectReportingPeriod(driver, job, "Daily")	
				
				SelectDate(driver, start_date)	
				
				SelectColumns(driver, job, ["Parent ASIN", "EAN", "ISBN-13", "Brand", "Subcategory", "Category", "Author/Artist", "Binding"])
		
				DownloadFile(driver, job)
				RenameDownloadedFile(source_file, target_file, 120)
				StringReplace(target_file, '—', 0.00)
			else:
				print("{} already exists.".format(os.path.basename(target_file)))
			
			
			
try:
	main()
	# email_message = "{} downloaded.".format(os.path.basename(target_file))
	email_status = "Succeeded"
except BaseException as e: 
	email_message = e
	email_status = "Failed"
	traceback.print_exc()
	
	LogError(e) 

execution_time = (round(timeit.default_timer() - start_time , 1))
if email_status == "Failed":
	#SendEmail('to_email', "from_email", job = job, duration = execution_time, status = email_status, message = email_message)
	pass