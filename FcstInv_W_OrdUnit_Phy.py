from functions_file import SiteLogin, SelectSalesView, SelectReportingPeriod, SelectDate, SelectColumns, DownloadFile, DateRange
from functions_file import GetLogin, Dates, GetFiles, StartFireFox, RenameDownloadedFile, SendEmail, LogError, StringReplace
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
		
		target_file = os.path.join(target_location, target_file_original.format(source[:2], start_date))
		
		if os.path.exists(target_file) == False:
	
			print("Downloading: {}".format(source))
			
			username, password = GetLogin(source)

			driver = StartFireFox(base_url, source_location, 60)
			
			SiteLogin(driver, username, password)
			
			#SelectSalesView(driver, "Shipped Revenue")
			
			#SelectReportingPeriod(driver, job, "Weekly")	
			
			SelectDate(driver, start_date)	
			
			SelectColumns(driver, job, ["Parent ASIN", "EAN", "ISBN-13", "Brand", "Subcategory", "Category", "Author/Artist", "Binding"])
		
			DownloadFile(driver, job)
			RenameDownloadedFile(source_file, target_file, 60)
			StringReplace(target_file, '—', 0.00)
			
		else:
			print("{} already exists.".format(target_file))
		
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