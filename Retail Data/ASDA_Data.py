import re
import zipfile

from functions import * 

config, log_filename = LoggingConfig("Asda", logging.INFO)

download_dir = r"C:\download_dir"
target_dir = r"\\target_dir"

username, password = GetLogin("ASDA")
	
start_date, start_date_obj, end_date, end_date_obj = DaysFromMonday("%d/%m/%Y", 2)	
report_date = start_date_obj.strftime('%Y%m%d') 


def main():

	newfilename = os.path.join(download_dir, "ASDA Weekly Sales {}.xls").format(report_date)

	CloseOpenBrowserWindows("firefox")

	if os.path.exists(newfilename) == False: # check the filename doesn't exist before executing the script.

		driver = StartFireFox("", download_dir, 240)	 
		
		driver.find_element_by_id("").send_keys(username)
		driver.find_element_by_id("").send_keys(password)
		time.sleep(1)
		driver.find_element_by_id("").click()
		
		toplink = driver.find_elements_by_class_name("")
		toplink_dict = dict(enumerate(toplink))
		
		toplink = toplink_dict[2]
		toplink.click()
		
		actionChains = ActionChains(driver)  

		frame = driver.find_element_by_id("")	 
		driver.switch_to_frame(frame)
		
		plus = driver.find_element_by_id("")
		plus.click()
		
		value = 'report - weekly'
		span_xpath = '//span[contains(text(), "' + value + '")]'
		span_element = driver.find_element_by_xpath(span_xpath)
		
		actionChains.context_click(span_element).perform()
		
		Modify = driver.find_element_by_link_text("")
		Modify.click()
		
		for handle in driver.window_handles:
			driver.switch_to_window(handle)
			
		# content_1
		frame = driver.find_element_by_id("submit")	 
		driver.switch_to_frame(frame)
		time.sleep(5)
		excel = driver.find_element_by_id("")
		excel.click()
		time.sleep(5)
		compressed = driver.find_element_by_id("")
		compressed.click()
		time.sleep(5)
		weekly = driver.find_element_by_id("")
		weekly.click()
		time.sleep(5)
		cal_day = driver.find_element_by_link_text("18")
		cal_day.click()
		
		run_now = driver.find_element_by_id("subnow")
		run_now.click()
		
		PrintLog("Waiting 10 minutes for the file to load on the site.")
		
		time.sleep(600) 
		
		view = driver.find_element_by_id("")
		view.click()
		
		frame = driver.find_element_by_id("")	 
		driver.switch_to_frame(frame)
		
		report_box = driver.find_element_by_xpath("")
		report_box.click()
		
		current_window = driver.current_window_handle # "JobTable" Frame is a sub frame of "submit" Frame. We need to switch back to the same window to select the parent Frame "submit" again.
		for handle in driver.window_handles:
			driver.switch_to_window(current_window)
			
		time.sleep(10)		
			
		frame = driver.find_element_by_css_selector("")
		driver.switch_to_frame(frame)
		
		retrieve = driver.find_element_by_xpath('')
		retrieve.click()
		
		time.sleep(180)
		
		os.chdir(download_dir)

		for file in os.listdir(download_dir):
			if re.match("_", file):
				ASDA_file = file  
			

		original_download_filename = os.path.join(download_dir, ASDA_file)

		RenameDownloadedFile(original_download_filename, newfilename, 30)
		
		TransferFile(newfilename, target_dir, "04 Asda")
		
		PrintLog("Script complete! {} downloaded and transferred succesfully!".format(os.path.basename(newfilename)))
		
		SendEmail('', "ASDA Data", log_filename)
		
	else:
		PrintLog("{} already exists.".format(newfilename))
	
	CloseOpenBrowserWindows("firefox")
	
try:
	main()

except BaseException as error:
	logging.exception("An exception occured")
	print(error) 
	#SendEmail('', "ASDA Data", log_filename)
