from numpy import uint32

from eorzea_time import EorzeaTime
from .rate import rates
from .zone import Zones


class EorzeaWeather:

    def __init__(self):
        self.rates = rates

    @staticmethod
    def get_weather_chance(et: EorzeaTime) -> int:

        lt_stamp = et.convert_to_lt_stamp()
        bell = lt_stamp / 175
        increment = uint32(bell + 8 - (bell % 8)) % 24

        total_days = uint32(lt_stamp / 4200)

        calc_base = total_days * 0x64 + increment

        step1 = uint32(calc_base << 0xB) ^ calc_base

        step2 = (step1 >> 8) ^ step1

        return int(step2 % 0x64)

    def get_weather(self, target_zone: Zones, et: EorzeaTime=EorzeaTime()):

        et.shift_weather_period()
        chance: int = self.get_weather_chance(et)
        for rate, weather in self.rates[target_zone].items():
            if chance < int(rate):
                return weather
