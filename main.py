from datetime import datetime as dt

import pytz

from eorzea_time import EorzeaTime
from eorzea_weather import EorzeaWeather, Zones

if __name__ == '__main__':

    print(EorzeaTime())
    ew = EorzeaWeather()
    et = EorzeaTime(dt.now(tz=pytz.timezone("Asia/Tokyo")))
    et.shift_weather_period()
    for i in range(20):
        print(f"{et.get_hour():>2}:{et.get_minute():>02} {ew.get_weather(Zones.EUREKA_PYROS, et)}")
        et.next_weather_period()
