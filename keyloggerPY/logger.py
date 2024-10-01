from datetime import datetime

def write_on_file(log_file, key):
	with open(log_file, 'a') as f:
		time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		f.write(f"{time_stamp} {key}\n")
