
from datetime import datetime, timedelta, date
from holidays import calculate_holidays, calculate_lunar_holidays

def create_full_day_event(name, day):
    date_format = "%Y%m%d"
    # Create the beginning of the ICS file
    
    if "Festa" in name:
        day_end = day + timedelta(days=3)
        ics_data = "BEGIN:VEVENT\n"
        ics_data += f"DTSTART;VALUE=DATE:{day.strftime(date_format)}\n"
        ics_data += f"DTEND;VALUE=DATE:{day_end.strftime(date_format)}\n"
        ics_data += f"SUMMARY:{name}\n"
        ics_data += "END:VEVENT\n"
    else:
        ics_data = "BEGIN:VEVENT\n"
        ics_data += f"DTSTART;VALUE=DATE:{day.strftime(date_format)}\n"
        ics_data += f"DTEND;VALUE=DATE:{day.strftime(date_format)}\n"
        ics_data += f"SUMMARY:{name}\n"
        ics_data += "END:VEVENT\n"
 
    
    return ics_data

# Create a new calendar
cal = "BEGIN:VCALENDAR\n"
cal += "VERSION:2.0\n" 

lat = '41.19928439762175'
lon = '-8.634738760618731'
elev = 100

year_start = 2024
year_end = 2100

holidays = calculate_holidays(year_start, year_end)

for event in holidays:
    cal += create_full_day_event(event[0], event[1])


cal += "END:VCALENDAR\n"



# Export the calendar to an .ics file
with open("holidays.ics", "w") as f:
    f.writelines(cal)

print("Holidays created successfully.")


cal = "BEGIN:VCALENDAR\n"
cal += "VERSION:2.0\n" 

lunar_holidays = calculate_lunar_holidays(year_start, year_end, lat, lon, elev)

for event in lunar_holidays:
    cal += create_full_day_event(event[0], event[1])



cal += "END:VCALENDAR\n"


# Export the calendar to an .ics file
with open("lunar.ics", "w") as f:
    f.writelines(cal)

print("Lunar Holidays created successfully.")

