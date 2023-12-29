from datetime import date, timedelta

def calculate_festa_mazouco(year):
    d = date(year, 8, 1)

    # Calculate the number of days to add to get to the first Sunday
    days_to_add = (6 - d.weekday()) % 7

    # Add the days to the first of August
    first_sunday = d + timedelta(days=days_to_add)

    festa = first_sunday + timedelta(days=19)

    return festa


def calculate_festa_freixo(year):
    d = date(year, 8, 1)

    # Calculate the number of days to add to get to the first Sunday
    days_to_add = (6 - d.weekday()) % 7

    # Add the days to the first of August
    first_sunday = d + timedelta(days=days_to_add)

    festa = first_sunday + timedelta(days=12)

    return festa