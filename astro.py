import ephem
from datetime import datetime, timedelta

def calculate_solstices_equinoxes(year, lat, long, ele):
    observer = ephem.Observer()
    observer.lat = lat  # Latitude of the observer (equator)
    observer.lon = long  # Longitude of the observer (prime meridian)
    observer.elev = ele  # Elevation (sea level)
    observer.date = f'{year}-01-01 00:00:00'

    # Calculate equinoxes and solstices
    vernal_equinox = ephem.next_vernal_equinox(observer.date)
    summer_solstice = ephem.next_summer_solstice(vernal_equinox)
    autumnal_equinox = ephem.next_autumnal_equinox(summer_solstice)
    winter_solstice = ephem.next_winter_solstice(autumnal_equinox)

    # Convert results to datetime objects
    vernal_equinox_date = datetime.strptime(str(vernal_equinox), '%Y/%m/%d %H:%M:%S')
    summer_solstice_date = datetime.strptime(str(summer_solstice), '%Y/%m/%d %H:%M:%S')
    autumnal_equinox_date = datetime.strptime(str(autumnal_equinox), '%Y/%m/%d %H:%M:%S')
    winter_solstice_date = datetime.strptime(str(winter_solstice), '%Y/%m/%d %H:%M:%S')

    return {
        'spring_eq': vernal_equinox_date,
        'summer_sol': summer_solstice_date,
        'autumn_eq': autumnal_equinox_date,
        'winter_sol': winter_solstice_date
    }

    return dates

def calculate_moon_phases(start, end):
    """
    Generate a list of significant moon phases (halfs, quarters, full) and their dates for a given year.
    """
    phases = []
    prev_phase = None
    start = datetime(start, 1, 1)
    end = datetime(end + 1, 1, 1)
    one_day = timedelta(days=1)

    current_date = start

    
    while current_date < end:
        new_moon = ephem.next_new_moon(current_date).datetime()
        last_quarter = ephem.next_last_quarter_moon(current_date).datetime()
        full_moon = ephem.next_full_moon(current_date).datetime()
        first_quarter = ephem.next_first_quarter_moon(current_date).datetime()
        phases.append(["New Moon", new_moon])
        phases.append(["Last Quarter", last_quarter])
        phases.append(["Full Moon", full_moon])
        phases.append(["First Quarter", first_quarter])
        current_date = max(new_moon, last_quarter, full_moon, first_quarter) + one_day
    return phases
