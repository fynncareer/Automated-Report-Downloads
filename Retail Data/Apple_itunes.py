import gzip
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

from functions import *

download_dir = r"C:\download_dir"
target_dir = r"\\target_dir"

config, log_filename = LoggingConfig("Apple iTunes", logging.INFO)

username, password = GetLogin("Apple iTunes")

start_date, start_date_obj, end_date, end_date_obj = DaysFromMonday('%Y%m%d', 1)

zip_file = "source_{}.txt.gz".format(end_date) 

zip_file = os.path.join(download_dir, zip_file)
zip_file_decompressed = zip_file[:-3] 

def main():

	CloseOpenBrowserWindows("firefox")

	if os.path.exists(zip_file) == False:		
		
		driver = StartFireFox("https://itunesconnect.apple.com", download_dir, 60)
		
		frame = driver.find_element_by_id("")	 
		driver.switch_to_frame(frame)
		
		AppleSignIn(driver, username, password)
		
		driver.switch_to.default_content()
		sales = driver.find_element_by_xpath("") 
		sales.send_keys(Keys.ENTER)
		
		#time.sleep(15)
		
		driver.get("https://reportingitc2.apple.com/reports.html")
		
		
		top_content = driver.find_element_by_class_name("")
		top_content.send_keys(Keys.ENTER)
		
		time.sleep(3)
		dropdown = driver.find_element_by_xpath("")
		dropdown.send_keys(Keys.ENTER)
		time.sleep(3)
		
		reports = driver.find_element_by_xpath("")
		reports.send_keys(Keys.ENTER)

		end_date = driver.find_element_by_css_selector("")
		end_date.send_keys(Keys.ENTER)
		end_date.click()

		week = driver.find_element_by_css_selector("")
		week.send_keys(Keys.ENTER)
		end_date.send_keys(Keys.ENTER)
		
		download = driver.find_element_by_css_selector("")
		download.send_keys(Keys.ENTER)
		
		time.sleep(30)
		
		driver.close()
		
		PrintLog("Downloaded: %s" % (zip_file))
		
		inF = gzip.GzipFile(zip_file, 'rb')
		s = inF.read()
		inF.close()

		outF = open(zip_file_decompressed, "wb")
		outF.write(s)
		outF.close()

		data = pd.read_csv(zip_file_decompressed, sep = "	")
		data = data[data.SKU != "Exception Library"] # remove rows where column C = "Exception Library" as these can't be ingested by the DWH.
		data.to_csv(zip_file_decompressed, mode = 'w+', index = False, sep = "\t", quoting = 3) 

		TransferFile(zip_file_decompressed, target_dir, "13 Apple iTunes")
		
		PrintLog("End of script.")
		
		#SendEmail('', "Apple iTunes", log_filename)
		
		CloseOpenBrowserWindows("firefox")
		
	else: 	
		PrintLog("{} already exists.".format(os.path.basename(zip_file)))

try:
	main()

except BaseException as error:
	logging.exception("An exception occured")
	print(error) 
	#SendEmail('', "Apple iTunes", log_filename)

