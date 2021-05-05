from functions import *

config, log_filename = LoggingConfig("Google Data", logging.INFO)

download_dir = r"C:\download_dir"
target_dir = r"\\target_dir"

username, password = GetLogin("Google")

start_date, start_date_dateobj, end_date, end_date_dateobj = DaysFromMonday("%d/%m/%Y", 2)	
	
report_date = end_date_dateobj.strftime('%Y%m%d') 

downloaded_filename = os.path.join(download_dir, "GoogleSales.csv")
newfilename = os.path.join(download_dir, "GoogleSales {}.csv").format(report_date) 


def main():

	CloseOpenBrowserWindows("firefox")

	if os.path.exists(newfilename) == False: 

		driver = StartFireFox("", download_dir, 60)	 
		
		time.sleep(5)
		driver.find_element_by_link_text("").click()
		time.sleep(5)
		driver.find_element_by_id("").click()
		time.sleep(5)
		driver.find_element_by_id("").send_keys(username)
		time.sleep(5)

		password_form = driver.find_element_by_name("")
		password_form.click()
		password_form.send_keys(password)
		
		time.sleep(5)
		driver.find_element_by_id("").click()	
		driver.find_element_by_id("").send_keys(Keys.ENTER)

		driver.find_element_by_css_selector("").send_keys(Keys.ENTER)
		driver.find_element_by_xpath('').send_keys(Keys.ENTER)
		
		enter_start_date = datetime.datetime.strptime(start_date,'%d/%m/%Y').date().strftime('%Y-%m-%d')
		enter_end_date = datetime.datetime.strptime(end_date,'%d/%m/%Y').date().strftime('%Y-%m-%d')

		setdate(driver.find_element_by_id(""), enter_end_date, "To Date")
		setdate(driver.find_element_by_id(""), enter_start_date, "From Date")

		elem = driver.find_element_by_xpath("")
		elem.click()

		if os.getcwd() != download_dir:
			os.chdir(download_dir)
		
		RenameDownloadedFile(downloaded_filename, newfilename, 75)
		
		destination_file = "\\dest\dest_file.csv"
		
		time.sleep(30)
		
		with open(newfilename, 'rb') as source_file:
			with open(destination_file, 'wb') as dest_file:
				contents = source_file.read()
				dest_file.write(contents.decode('utf-16').encode('utf-8'))
		
		time.sleep(30)
		
		df = pd.read_csv(destination_file, sep = "\t")
		df["Transaction Date"].unique() 
		

		PrintLog("Script complete! {} downloaded and transferred succesfully!".format(os.path.basename(newfilename)))
		
		#SendEmail('', "Google Data", log_filename)

		
	else:	
		PrintLog("Filename already exists for:" + newfilename)
	
	CloseOpenBrowserWindows("firefox")
	
try:
	main()

except BaseException as error:
	print("An exception occured: {}".format(error))
	logging.exception("An exception occured: {}".format(error))
	
	#SendEmail('', "Google Data", log_filename)

