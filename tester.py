from logger import Logger
import random 

#CREATE singleton instance
logger = Logger()

events = ['START', 'STOP', 'ERROR', 'SUCCESS']
crons = ['FDKAT', 'FELISPOLONIA', 'CATPEDIGREES', 'SIAMESSEE']


for iteration in range(10000):
    event = events[random.randrange(len(events))]
    cron = crons[random.randrange(len(crons))]
    
    print(str(iteration), "-LOGGING: ", event, "/", str(iteration) + str("th event value"), "/", cron)
    logger.logDB(event, str(iteration) + str("th event value"), cron)

