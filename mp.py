import datetime

def get_current_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    if hour > 12:
        hour -= 12
        am_pm = "PM"
    else:
        am_pm = "AM"

    current_time = f"{hour}:{minute:02d}:{second:02d} {am_pm}"
    return current_time

print(get_current_time())