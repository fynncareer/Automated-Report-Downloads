from selenium.webdriver.chrome.options import Options
import gzip
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

from functions import *

config, log_filename = LoggingConfig("Apple Ebooks", logging.INFO)

download_dir = r"C:\download_dir"
target_dir = r"\\target\dir"
BO_dir = r"\\BO\dir"

username, password = GetLogin("Apple Ebooks")

start_date, start_date_obj, end_date, end_date_obj = DaysFromMonday('%Y%m%d', 1)

zip_file = "format_{}.txt.gz".format(end_date)
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
		
		driver.get("https://reportingitc2.apple.com/reports.html")
		
		end_date = driver.find_element_by_css_selector('')
		end_date.click()
		
		time.sleep(4)
		driver.find_element_by_css_selector('').click()
		
		end_date.send_keys(Keys.ENTER)
		
		driver.find_element_by_css_selector('').send_keys(Keys.ENTER) # download 
		
		PrintLog("Downloading File...")
		time.sleep(45) # wait for file to download.

		driver.close()
		
		PrintLog("Downloaded: %s" % (zip_file))
		
		inF = gzip.GzipFile(zip_file, 'rb')
		s = inF.read()
		inF.close()

		outF = open(zip_file_decompressed, "wb")
		outF.write(s)
		outF.close()

		TransferFile(zip_file_decompressed, BO_dir, "12 Apple Books")

		data = pd.read_csv(zip_file_decompressed, sep = "	") 

		Postal_Code = pd.Series(data['Postal Code']) 
		data['Postal Code'] = Postal_Code.str.replace(' ', '')
			
		new_df = pd.DataFrame() 
		new_df_1 = new_df.append(data, ignore_index = True)
		
		new_df_1.to_csv(zip_file_decompressed, encoding = 'utf-8', mode = 'w+', index = False, sep = "\t")
		
		TransferFile(zip_file_decompressed, target_dir, "12 Apple Books")	
			
		CloseOpenBrowserWindows("firefox")
		
		#SendEmail('', "Apple Ebooks", log_filename)		
	else: 	
		PrintLog("{} already exists.".format(os.path.basename(zip_file)))

try:
	main()

except BaseException as error:
	logging.exception("An exception occured")
	print(error)
	#SendEmail('', "Apple Ebooks", log_filename)

	
