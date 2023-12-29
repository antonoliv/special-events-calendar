from datetime import date, timedelta
from easter import calculate_easter
from dst import calculate_summer_time, calculate_winter_time
from astro import calculate_solstices_equinoxes, calculate_moon_phases
from festas import calculate_festa_freixo, calculate_festa_mazouco

def calculate_holidays(start, end):
    ret = []
    year = start
    while(year <= end):
        holidays = {}
        
        holidays["Páscoa"] = calculate_easter(year)
        holidays["Carnaval"] = holidays["Páscoa"] - timedelta(days=47)
        holidays["Sexta-feira Santa"] = holidays["Páscoa"] - timedelta(days=2)

        holidays['Festa de Freixo de Espada à Cinta'] = calculate_festa_freixo(year)
        holidays['Festa de Mazouco'] = calculate_festa_mazouco(year)
        holidays_list = [[key, value] for key, value in holidays.items()]
        ret.extend(holidays_list)
        year += 1
    return ret

def calculate_lunar_holidays(start, end, lat, long, ele):
    ret = []
    year = start

    while(year <= end):
        holidays = {}
        holidays["Summer Time "] = calculate_summer_time(year)
        holidays["Winter Time"] = calculate_winter_time(year)
        sol_eq = calculate_solstices_equinoxes(year, lat, long, ele)
        holidays['Spring Equinox'] = sol_eq['spring_eq']
        holidays['Summer Solstice'] = sol_eq['summer_sol']
        holidays['Autumn Equinox'] = sol_eq['autumn_eq']
        holidays['Winter Solstice'] = sol_eq['winter_sol']
        holidays_list = [[key, value] for key, value in holidays.items()]
        ret.extend(holidays_list)
        year += 1

    ret.extend(calculate_moon_phases(start, end))
    return ret

