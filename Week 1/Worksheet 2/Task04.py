import datetime

start_time_hours = int(input("Starting time (hours): "))
start_time_minutes = int(input("Starting time (minutes): "))

start_time = datetime.datetime(1,1,1,start_time_hours, start_time_minutes)

event_duration = int(input("Event duration (minutes): "))

end_time = start_time + datetime.timedelta(seconds=event_duration * 60)
duration_days = (end_time - start_time).days

print("End time = {:d}:{:02d}".format(end_time.hour, end_time.minute), end="")
if end_time.day == 2 and duration_days <= 1:
    print(", the next day")
elif duration_days >= 1:
    print(",", duration_days + 1, "days later")
