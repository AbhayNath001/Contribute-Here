import datetime

def Time():
    hours = int(datetime.datetime.now().strftime("%H"))
    minutes = datetime.datetime.now().strftime(":%M %p")
    if hours > 12:
        hours = hours - 12
        time = str(hours) + minutes
    else:
        time = str(hours) + minutes
    return time

def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    date_str = f"{month}/{date}/{year}"
    return date_str

def Day():
    day = datetime.datetime.now().strftime("%A")
    return day

def DateTimeInfo(choice):
    if choice == "time":
        print("Current Time:", Time())
    elif choice == "date":
        print("Current Date:", Date())
    elif choice == "day":
        print("Current Day:", Day())
    else:
        print("Invalid choice. Please choose 'time', 'date', or 'day'.")

# Example usage:
print("Choose 'time', 'date', or 'day':")
user_choice = input().lower()
DateTimeInfo(user_choice)
