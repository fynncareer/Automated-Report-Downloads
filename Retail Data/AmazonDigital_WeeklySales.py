import paramiko
from functions import *

config, log_filename = LoggingConfig("Amazon Digital Weekly Sales", logging.INFO)

def main():

	target_dir = r"\\target_dir"

	file_date, file_date_obj, end_date, end_date_dateobj = DaysFromMonday("%Y%m%d", 2)

	source_file_1 = "weekly_report_{}_EU_1.csv".format(end_date)
	source_file_2 = "weekly_report_{}_EU_3.csv".format(end_date)
	source_file_3 = "weekly_report_{}_EU_3.csv".format(end_date) # pair with target_file
	target_file = "weekly_report_{}_EU_3.csv".format(end_date)

	if os.path.exists(os.path.join("C:\\target_dir", target_file)) == False:

		#open a transport 
		host = 'kcm.amazon-digital-ftp.com'
		port = 22	
		transport = paramiko.Transport((host, port))

		#auth 
		username, password = GetLogin("Amazon Digital Weekly Sales")
		
		transport.connect(username = username, password = password)

		#sftp
		sftp = paramiko.SFTPClient.from_transport(transport)

		#download 
		filepath = os.path.join("/source/path/", source_file_1)
		localpath = os.path.join("C:\\\target_dir\\", source_file_1)
		PrintLog(filepath)
		sftp.get(filepath, localpath)

		filepath = os.path.join("/source/path/", source_file_2)
		localpath = os.path.join("C:\\\target_dir\\", source_file_2)
		PrintLog(filepath)
		sftp.get(filepath, localpath)

		filepath = os.path.join("/source/path/", source_file_3)
		localpath = os.path.join("C:\\\target_dir\\", target_file)
		PrintLog(filepath)
		sftp.get(filepath, localpath)

		os.chdir("C:\\\target_dir\\")

		df_source_file_1 = pd.read_csv(source_file_1, skiprows = 5, header = None) #sep = "\t"
		df_source_file_2 = pd.read_csv(source_file_2, skiprows = 5, header = None)

		new_df = pd.DataFrame() 

		new_df = new_df.append(df_source_file_1, ignore_index = True)
		new_df = new_df.append(df_source_file_2, ignore_index = True)

		new_df.to_csv(target_file, mode = 'a', index = False, header = False, quoting = 1) 

		TransferFile(target_file, target_dir, "02 Weekly Sales - Amazon Digital")

		PrintLog("Script complete! New file is: %s" % target_file)
		
		SendEmail('', "Amazon Digital Weekly Sales", log_filename)
		
	else:
		PrintLog("{} File already exists.".format(target_file))

try:
	main()

except BaseException as error:
	logging.exception("An exception occured")	
	SendEmail('', "Amazon Digital Weekly Sales", log_filename)
