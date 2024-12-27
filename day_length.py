# based on https://en.wikipedia.org/wiki/Sunrise_equation
from math import sin, cos, acos, tan, radians, degrees, pi


def sunRiseSunSet(lon, d, m, y):
    """for given longitude and day of a year"""
    dl = dayLength(lon, d, m, y)
    (h, mi) = hoursMins(dl / 2)
    midHour = 13 if isDst(d, m) else 12
    sunSet = (midHour + h, mi)
    sunRise = (midHour - 1 - h, 59 - mi)
    return sunRise, sunSet


def isDst(d, m):
    """daylight saving time"""
    # simplified between 27.3. and 27.10
    return 2 < m < 11 and (m != 3 or d >= 27) and (m != 10 or d <= 27)


def hoursMins(h):
    return tuple(divmod(round(60 * h), 60))


def dayLength(lat, d, m, y):
    """for given latitude and day of a year"""
    # angle of sunrise from noon
    # ha = arccos (cos(90.833) /(cos(L)*cos(dec)) - tan(L)*tan(dec)).
    # dl day length in hours
    # dl = 2 * ha / 15
    ha = hourAngle(lat, d, m, y)
    return 2 * degrees(ha) / 15


def hourAngle(lat, d, m, y):
    dec = radians(declination(d, m, y))
    rLon = radians(lat)
    # angle of sunrise from noon
    return acos(cos(radians(90.833)) / (cos(rLon)*cos(dec)) - tan(rLon)*tan(dec))


def declination(d, m, y):
    """earth declination angle towards sun"""
    # declination d is number of days after the spring equinox usually March 21st
    # dec = 23.45 * sin((360 * d/365.25)°)°
    d = daysFromEquinox(d, m, y)
    return 23.45 * sin(radians(360 * d / 365.24))


def daysFromEquinox(d, m, y):
    """number of days after the spring equinox usually March 21st"""
    if m == 3:
        if d >= 21:
            return d - 21
        else:
            return (366 if isLeapYear(y + 1) else 365) - d
    days = -21
    for m in range(3, m if m > 3 else m + 12):
        mo = m % 12
        if not mo:
            mo = 12
        days += daysInMonth(y, mo)
    return days + d


def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def daysInMonth(year, month):
    """month must be between 1 and 12"""
    if month == 2:
        if isLeapYear(year):
            return 29  # Leap year
        else:
            return 28
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    return 30


def jDateToHoursMins(jd):
    """Converts a Julian Date to hours and minutes."""
    # Calculate the number of days since noon, January 1, 2000
    days_since_j2000 = jd - 2451545.0
    # Calculate the number of hours
    hours = days_since_j2000 * 24 + 13  # why + 13 ?
    # Extract the fractional part of the hours
    fractional_hours = hours - int(hours)
    # Calculate the number of minutes
    minutes = fractional_hours * 60
    # Extract the integer part of minutes
    minutes = int(minutes)
    # Extract the integer part of hours
    hours = int(hours)
    # Adjust hours to 24-hour format
    hours = hours % 24
    return hours, minutes


def solarTransit(lon, d, m, y):
    # mean solar time
    j = daysFromNewYear(d, m, y) - lon / 360
    # mean solar anomaly
    m = radians(357.5291 + 0.98560028 * j) % (2 * pi)
    # center
    c = 1.9148 * sin(m) + 0.02 * sin(2*m) + 0.0003 * sin(3*m)
    # ecliptic longitude
    la = (m + radians(c + 180 + 102.9372)) % (2 * pi)
    # solar transit
    jt = 2451545 + j + 0.0053 * sin(m) - 0.0069 * sin(2 * la)
    return jDateToHoursMins(jt)


def daysFromNewYear(d, m, y):
    """number of days after New Year"""
    days = 0
    for m in range(1, m + 1):
        days += daysInMonth(y, m)
    return days + d
