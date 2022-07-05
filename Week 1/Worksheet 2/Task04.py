import datetime

startTimeHours = int(input("Starting time (hours): "))
startTimeMinutes = int(input("Starting time (minutes): "))

startTime = datetime.datetime(1,1,1,startTimeHours, startTimeMinutes)

eventDuration = int(input("Event duration (minutes): "))

endTime = startTime + datetime.timedelta(seconds=eventDuration * 60)
durationDays = (endTime - startTime).days

print("End time = {:d}:{:02d}".format(endTime.hour, endTime.minute), end="")
if endTime.day == 2 and durationDays <= 1:
    print(", the next day")
elif durationDays >= 1:
    print(",", durationDays + 1, "days later")
