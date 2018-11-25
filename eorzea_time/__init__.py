from datetime import datetime as dt


class EorzeaTime:

    def __init__(self, lt: dt = dt.now()):
        self.EORZEA_TIME_CONST = 3600.0 / 175.0
        self.ONE_MINUTE = 60
        self.ONE_HOUR = self.ONE_MINUTE * 60
        self.EIGHT_HOUR = self.ONE_HOUR * 8
        self.EORZEA_SUN = 24
        self.EORZEA_BELL = 60

        self.et_stamp = lt.timestamp() * self.EORZEA_TIME_CONST

    def __str__(self):
        return str(f"ET {self.get_hour():>2}:{self.get_minute():>02}")

    def convert_to_lt_stamp(self) -> float:
        return self.et_stamp / self.EORZEA_TIME_CONST

    def get_hour(self) -> int:
        return int(self.et_stamp / self.ONE_HOUR % self.EORZEA_SUN)

    def get_minute(self) -> int:
        return int(self.et_stamp / self.ONE_MINUTE % self.EORZEA_BELL)

    def shift_weather_period(self):
        self.et_stamp = (int(self.et_stamp / self.EIGHT_HOUR) * self.EIGHT_HOUR)

    def next_weather_period(self, period: int = 1):
        self.et_stamp = self.et_stamp + self.EIGHT_HOUR * period

    def prev_weather_period(self, period: int = 1):
        self.et_stamp = self.et_stamp - self.EIGHT_HOUR * period
