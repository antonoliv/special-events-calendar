from datetime import date, timedelta

def calculate_summer_time(year):
    d = date(year, 3, 31)
    
    day_of_week = d.weekday()
    
    days_to_subtract = (day_of_week + 1) % 7
    
    last_sunday = d - timedelta(days=days_to_subtract)
    
    return last_sunday

def calculate_winter_time(year):
    d = date(year, 10, 31)
    
    day_of_week = d.weekday()
    
    days_to_subtract = (day_of_week + 1) % 7
    
    last_sunday = d - timedelta(days=days_to_subtract)
    
    return last_sunday