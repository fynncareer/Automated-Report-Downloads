import os
import datetime 
from datetime import timedelta

def ExecuteScripts(start_date = None, end_date = None, scripts = []): # scripts = list
	
	def DateRange(start_date, end_date):
		start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
		if end_date is None:
			end_date = start_date
		else:
			end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y").date()
		print(start_date, end_date)
		
		while start_date <= end_date:
			yield datetime.datetime.strftime(start_date, '%d/%m/%Y')
			start_date += timedelta(days=1)
			print(start_date)
	
	
	if start_date:
		for job in scripts:
			for date in DateRange(start_date, end_date):
				script = "py {} --start_date {}".format(job, date)
				print(script) 
				os.system(script)
				os.system(script)
				os.system(script)
				
	else:
		for job in scripts:
			script = "py {}".format(job)
			os.system(script)
			os.system(script)
			

weekday = datetime.date.today().weekday()	# Mon = 0, Tues = 1, Weds = 2, Thu = 3, Fri = 4, Sat = 5, Sun = 6 

if weekday == 0: 
	end_date = datetime.datetime.today()- datetime.timedelta(days = 1)
	end_date = datetime.datetime.strftime(end_date, "%d/%m/%Y")
else:
	weekday_day = 1 + weekday
	end_date = datetime.datetime.today()- datetime.timedelta(days = weekday_day)
	end_date = datetime.datetime.strftime(end_date, "%d/%m/%Y")
	
	
start_date = datetime.datetime.strptime(end_date, "%d/%m/%Y") - datetime.timedelta(days = 6) 
start_date = datetime.datetime.strftime(start_date, "%d/%m/%Y")

print(start_date)
print(end_date)

## WEEKLY

ExecuteScripts(scripts = ["SaleDiag_W_OrdRev_Phy.py", "SaleDiag_W_ShipCOGS_Phy.py", "FcstInv_W_OrdUnit_Phy.py"]) 

ExecuteScripts(scripts = ["Alternative_Purchase_W_Phy.py"])	

ExecuteScripts(scripts = ["Market_Basket_Analysis_W_Phy.py", "Repeat_Purchase_W_Phy.py"]) # 9

# DAILY 

ExecuteScripts(start_date, end_date, scripts = ["Traffic_Diagnostic.py"]) 

ExecuteScripts(start_date, end_date, scripts = ["AmzSrchTerms_Books_D.py", "AmzSrchTerms_KindleStore_D.py"])  

ExecuteScripts(start_date, end_date, scripts = ["SaleDiag_D_OrdRev_Dig.py", "PreOrders_D_Dig.py"])  

ExecuteScripts(start_date, end_date, scripts = ["GeoSales_D_ShipRev_Phy.py", "GeoSales_D_ShipCOGS_Phy.py", "PreOrders_D_Phy.py"]) 


