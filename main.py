from eorzea_weather import EorzeaWeather, Zones
from eorzea_time import Et
from datetime import datetime as dt
import pytz
if __name__ == '__main__':
    ew = EorzeaWeather()

    lt_stamp = dt.now().timestamp()
    et = Et(dt.now(tz=pytz.timezone("Asia/Tokyo")))

    print(f"ET:{et}")

    print(f"Current Weather period: {et.shift_weather_period()}")
    print(f"Next Weather period: {et.next_weather_period()}")

    for i in range(5):
        print(ew.get_weather(Zones.EUREKA_PYROS, dt.fromtimestamp(
            ((lt_stamp * ew.TIME_CONST) + 28800 * i) / ew.TIME_CONST)))
