import os
import datetime 
from datetime import timedelta

def ExecuteScripts(scripts = []): # scripts = list
	
	print("works")
	for job in scripts:
		script = "py {}".format(job)
		os.system(script)
		os.system(script)
		os.system(script)
		
		#Run script more than once to account for any random Selenium errors that can occur from interacting with dynamic DOM elements.

# DAILY 

ExecuteScripts(scripts = ["AmazonDigital_WeeklySales.py", "ASDA_Data.py", "Google_Data.py", "Apple_ebooks.py", "Apple_Itunes.py"])
