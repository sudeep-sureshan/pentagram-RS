from crontab import CronTab
import sys
import os

#task in cron

pwd = os.path.abspath('.') 
cmd = 'cd '+pwd+' ; python '+pwd+'/parser.py >> '+pwd+'/cron_log/crontab_log.txt'

def start_logging():
	tab = CronTab()
	cron_job = tab.new(cmd)
	cron_job.minute.every(1) # change this value to the decided threshold in production phase

	tab.write() # write content to crontab
	print tab.render()
	

def stop_logging():
	tab = CronTab()
	cron_job = tab.find_command(cmd)
	for job in cron_job:
		tab.remove(job)
	tab.write()


if(sys.argv[1]=="start"):
	start_logging()
elif(sys.argv[1]=="stop"):
	stop_logging()

