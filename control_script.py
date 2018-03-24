import os
import datetime 
from datetime import timedelta

def ExecuteScripts(start_date = None, end_date = None, scripts = []): # scripts = list
	
	if start_date:
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

		for job in scripts:
			for date in DateRange(start_date, end_date):
				script = "py {} --start_date {}".format(job, date)
				os.system(script)
				os.system(script)
				os.system(script)
				
	else:
		for job in scripts:
			script = "py {}".format(job)
			os.system(script)
			os.system(script)
			os.system(script)
			

weekday = datetime.date.today().weekday()	# Mon = 0, Tues = 1, Weds = 2, Thu = 3, Fri = 4, Sat = 5, Sun = 6 

if weekday == 0: 
	start_date = datetime.datetime.today()- datetime.timedelta(days = 1)
	start_date = datetime.datetime.strftime(start_date, "%d/%m/%Y")
else:
	weekday_day = 1 + weekday
	start_date = datetime.datetime.today()- datetime.timedelta(days = weekday_day)
	start_date = datetime.datetime.strftime(start_date, "%d/%m/%Y")
	
	
end_date = datetime.datetime.strptime(start_date, "%d/%m/%Y") - datetime.timedelta(days = 6) 
end_date = datetime.datetime.strftime(end_date, "%d/%m/%Y")

print(start_date)
print(end_date)

## WEEKLY

ExecuteScripts(scripts = ["SaleDiag_W_OrdRev_Phy.py", "SaleDiag_W_ShipCOGS_Phy.py", "FcstInv_W_OrdUnit_Phy.py"])	# 10 days before

ExecuteScripts(scripts = ["Alternative_Purchase_W_Phy.py"])	

ExecuteScripts(scripts = ["Market_Basket_Analysis_W_Phy.py", "Repeat_Purchase_W_Phy.py"])	

# DAILY 

ExecuteScripts(start_date, end_date, ["SaleDiag_D_OrdRev_Dig.py", "PreOrders_D_Dig.py"])

ExecuteScripts(start_date, end_date, ["GeoSales_D_ShipRev_Phy.py", "GeoSales_D_ShipCOGS_Phy.py", "PreOrders_D_Phy.py"])

