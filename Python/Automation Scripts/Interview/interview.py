#!/usr/bin/python

import sys

# Accepting the Command Line Arguments
sys.argv.pop(0)             # Popping out the first element as it contains script file
arguments =[]
arguments = sys.argv

# Checking for the number of arguments
if len(arguments) < 3:
    print("Please enter all the required arguments to execute the script.")
elif len(arguments) > 3:
    print("Too many arguments, Please only enter three arguments.")

# to fetch the date
with open(arguments[1], 'r') as app_file:
    lines = app_file.read().splitlines()
    date = lines[0]

# getting the day of the week
import datetime  
year, month, day = (int(x) for x in date.split('-'))    
day_of_week = datetime.date(year, month, day).weekday()

# Adjusting the day_of_week value(Sunday = 1, Monday = 2 & so on)
day_of_week = ((day_of_week + 1) % 7) + 1

# reading the schedule file
with open(arguments[0], 'r') as schedule_file:
    schedules = schedule_file.read().splitlines()

# Cleaning the data
schedules.pop(0)
schedules.pop(0)

schedule_dict = {}

for line in schedules:
    cols=line.split('|')
    cols.pop(0)
    cols = [x.strip() for x in cols]
    schedule_dict[cols[0]] = cols

lines.pop(0)
writeLines = []

# Storing the data in a list
for application in lines:
    schedule = schedule_dict[application]
    if schedule[4] == "true":
        continue
    
    conditions = schedule[5].split(',')
    for condition in conditions:
        if '-' in condition:
            r = condition.split('-')
            if int(r[0]) <= day_of_week <= int(r[1]):
                writeLines.append(",".join([application,schedule[1],schedule[2],schedule[3]]))
        elif condition == '*':
           writeLines.append(",".join([application,schedule[1],schedule[2],schedule[3]])) 
        elif int(condition) == day_of_week:
            writeLines.append(",".join([application,schedule[1],schedule[2],schedule[3]]))

# Writing data from python list to csv file    
with open(arguments[2],'w') as output_file:
    for write in writeLines:
        output_file.write(write)
        output_file.write('\n')
