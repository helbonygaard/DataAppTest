import schedule
import time
import papermill as pm
from datetime import datetime
import json, sys

def job(): # parameterize job - naturally!
    with open("subscription.json") as jsonfile:
        dictionary = json.load(jsonfile)
    pm.execute_notebook(
		'OverflowServiceSandbox.ipynb',
		'./runLogs/OverflowServiceSandbox_run_time_'+str(datetime.timestamp(datetime.now()))+'.ipynb',
		parameters = dictionary
        
	)
#Dictionary
#dict(start='2019-06-04T0:55:52Z', stop='2019-06-05T19:28:52Z', levelThreshold=0.45, maxThreshold=0.90, levelSlopeAngle=0.000085, dataOffset=0, bufferLength=30, resultAttribute='overflow')

#JSON
#{"start":"2019-06-04T0:55:52Z", "stop":"2019-06-05T19:28:52Z", "levelThreshold":0.45, "maxThreshold":0.90, "levelSlopeAngle":0.000085, "dataOffset":0, "bufferLength":30, "resultAttribute":"overflow"}
    
# Run single line cli example
#papermill OverflowServiceSandbox.ipynb ./OverflowServiceSandbox_run_cli.ipynb -p start '2019-06-04T0:55:52Z' -p stop '2019-06-05T19:28:52Z' -p levelThreshold 0.45 -p maxThreshold 0.90 -p levelSlopeAngle 0.000085 -p dataOffset 0 -p bufferLength 30 -p resultAttribute 'overflow'

# Activate job schedule
# Set up CLI Arguments
schedule.every(1).minutes.do(job)

# Other schedules
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

# Execute schedule for ever
while True:
    schedule.run_pending()
    time.sleep(1)

# How to start-up in cli
# python scheduledNotebook.py '{start:'2019-06-04T0:55:52Z', stop:'2019-06-05T19:28:52Z', levelThreshold:0.45, maxThreshold:0.90, levelSlopeAngle:0.000085, dataOffset=0, bufferLength=30, resultAttribute='overflow'}'