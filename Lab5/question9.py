from city import make_city, get_name, get_lat, get_lon
from question8 import distance

def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """

    dummy_city = make_city('Dummy city', lat, lon)
    d1 = distance(dummy_city, city1)
    d2 = distance(dummy_city, city2)

    if d1 > d2:
    	return get_name(city2)
    else:
    	return get_name(city1)