#author @60888
import time
import papermill as pm
from datetime import datetime
import json, sys
import os
import random

def install(package):
    os.system(str("python3 -m pip install " + package))
		
def comprehensionCatch(func, handle=lambda e : e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return handle # handle(e)

def job(resultKey): # parameterize job - naturally!
    with open("subscriptionConfig.json") as jsonfile:
        dictionary = json.load(jsonfile)
		containsNumberOfLists = sum([len(dictionary[x]) for x in dictionary if isinstance(dictionary[x], list)])
		resultAttributes = dictionary.pop(resultKey, None)
		dictionaryNew = {resultKey:resultAttributes}
		try: # Is this a drill?
			# Do some dictionary magic
			stringDictionary = { key:value for (key,value) in dictionary.items() if isinstance(value[0], str)}
			stringListDictionary = [dict(zip(stringDictionary, i)) for i in zip(*stringDictionary.values())] # [dict(zip(dictionary, i)) for i in zip(*dictionary.values())] 
			dictionaryNew.update(stringListDictionary[0])
			intergerDictionary = { key:value for (key,value) in dictionary.items() if isinstance(value[0], int)}
			#intergerListDictionary = [dict(zip(intergerDictionary, i)) for i in zip(*intergerDictionary.values())]
			randomIntegers = { key:random.randint(value[0],value[1]) for (key,value) in intergerDictionary.items()}
			dictionaryNew.update(randomIntegers) 
			floatDictionary = { key:value for (key,value) in dictionary.items() if isinstance(value[0], float)}
			#floatListDictionary = [dict(zip(floatDictionary, i)) for i in zip(*floatDictionary.values())]
			randomFloats = { key:random.uniform(value[0],value[1]) for (key,value) in floatDictionary.items()}
			dictionaryNew.update(randomFloats)
			dictionary = dictionaryNew
		except:
			print("This is not a drill")
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
install('schedule') # Special environment package for production scheduling
import schedule
schedule.every(10).minutes.do(job('resultAttribute'))

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