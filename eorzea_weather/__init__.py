from datetime import datetime as dt
from numpy import uint32

from .rate import rates
from .zone import Zones


class EorzeaWeather:

    def __init__(self):
        self.rates = rates
        self.ONE_HOUR = 175 * 1000
        self.EIGHT_HOUR = self.ONE_HOUR * 8
        self.ONE_DAY = self.EIGHT_HOUR * 3
        self.TIME_CONST = 3600.0 / 175.0
        self.test = 28800

    @staticmethod
    def get_weather_chance(lt: dt) -> int:
        lt_stamp = lt.timestamp()
        bell = lt_stamp / 175
        print(bell)
        increment = uint32(bell + 8 - (bell % 8)) % 24

        total_days = uint32(lt_stamp / 4200)

        calc_base = total_days * 0x64 + increment

        step1 = uint32(calc_base << 0xB) ^ calc_base

        step2 = (step1 >> 8) ^ step1

        print(int(step2 % 100))
        return int(step2 % 0x64)

    def get_weather(self, target_zone: Zones, lt: dt):

        lt = self.move_start_period(lt)

        chance: int = self.get_weather_chance(lt)
        for rate, weather in self.rates[target_zone].items():
            if chance < int(rate):
                return weather

    def move_start_period(self, lt: dt) -> dt:
        et_stamp = lt.timestamp() * self.TIME_CONST
        lt_stamp = int(int(et_stamp / 28800) * 28800) / self.TIME_CONST
        return dt.fromtimestamp(lt_stamp)
