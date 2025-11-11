import json
from datetime import datetime, timedelta

# Load habit tracker data from JSON file
with open("habit_data.json", "r") as f:
    data = json.load(f) 
    
print(type(data)) # dictionary

# Convert date strings to datetime objects(Dates as objects allow us to calculate week numbers easily.)
habit_entries = []
for date_str, habits in data.items():
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    habit_entries.append((date_obj, habits))  # habit_entries = [
  #(datetime(2025,11,3), {"exercise": True, "reading": False}),
  #(datetime(2025,11,4), {"exercise": True, "reading": True}),
  #...
#]

# Sort entries by date
habit_entries.sort(key=lambda x: x[0])

# Compute weekly report
weekly_report = {}
for date_obj, habits in habit_entries:
    # Compute ISO week number (year, week, day)
    year, week, _ = date_obj.isocalendar()
    week_key = f"{year}-W{week}"
    
    if week_key not in weekly_report:
        weekly_report[week_key] = {} # weekly_report = {
    # "2025-W45": {}
#}
    
    for habit, done in habits.items():
        if habit not in weekly_report[week_key]:
            weekly_report[week_key][habit] = {"done": 0, "total": 0}
        weekly_report[week_key][habit]["done"] += int(done)
        weekly_report[week_key][habit]["total"] += 1

# Print weekly report
for week, habits in weekly_report.items():
    print(f"\nWeek: {week}")
    for habit, stats in habits.items():
        percentage = stats["done"] / stats["total"] * 100
        print(f"  {habit}: {stats['done']}/{stats['total']} days ({percentage:.1f}%)")
