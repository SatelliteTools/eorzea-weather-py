from datetime import datetime as dt

import pytz

from eorzea_time import EorzeaTime
from eorzea_weather import EorzeaWeather, Zones

if __name__ == '__main__':


    target_zone: Zones = Zones.EUREKA_PYROS
    print(str(target_zone))

    ew = EorzeaWeather()
    et = EorzeaTime(dt.now(tz=pytz.timezone("Asia/Tokyo")))
    et.shift_weather_period()
    et.prev_weather_period(period=6)
    for i in range(10):
        print(
            f"LT {et.convert_to_lt().strftime('%H:%M')} ET {et.get_hour():>2}:{et.get_minute():>02} {ew.get_weather(target_zone, et)}")
        et.next_weather_period()

    print(f"LT {et.convert_to_lt().strftime('%H:%M')} ET {et.get_hour():>2}:{et.get_minute():>02} {ew.get_weather(target_zone, et)}")
    print(f"<<<<<<<<<<  now LT {dt.now().strftime('%H:%M')} {EorzeaTime()} >>>>>>>>>>")
    et.next_weather_period()
    for i in range(10):
        print(f"LT {et.convert_to_lt().strftime('%H:%M')} ET {et.get_hour():>2}:{et.get_minute():>02} {ew.get_weather(target_zone, et)}")
        et.next_weather_period()
