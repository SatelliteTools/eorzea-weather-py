from datetime import datetime as dt


class Et:
    EORZEA_TIME_CONST = 3600.0 / 175.0

    ONE_MINUTE = 60
    ONE_HOUR = 60 * 60

    EORZEA_SUN = 24
    EORZEA_BELL = 60

    EIGHT_HOUR = 28800

    def __init__(self, lt: dt):
        self.et_stamp = lt.timestamp() * self.EORZEA_TIME_CONST
        self.MINUTE = 60
        self.HOUR = self.MINUTE * 60

        self.EORZEA_SUN = 24
        self.EORZEA_BELL = 60

        self.EIGHT_HOUR = self.HOUR * 8

    def __str__(self):
        return str(f"{self.get_hour()}:{self.get_minute():>02}")

    def convert_to_lt_stamp(self) -> float:
        return self.et_stamp / self.EORZEA_TIME_CONST

    @classmethod
    def current_hour(cls) -> int:
        return int(dt.now().timestamp() / cls.ONE_HOUR % cls.EORZEA_SUN)

    @classmethod
    def current_minute(cls) -> int:
        return int(dt.now().timestamp() / cls.ONE_MINUTE % cls.EORZEA_BELL)

    def get_hour(self) -> int:
        return int(self.et_stamp / self.ONE_HOUR % self.EORZEA_SUN)

    def get_minute(self) -> int:
        return int(self.et_stamp / self.ONE_MINUTE % self.EORZEA_BELL)

    def shift_weather_period(self):
        self.et_stamp = (int(self.et_stamp / self.EIGHT_HOUR) * self.EIGHT_HOUR)

        return self

    def next_weather_period(self, period: int = 1):
        self.et_stamp = self.et_stamp + self.EIGHT_HOUR * period

        return self

    def prev_weather_period(self, period: int = 1):
        self.et_stamp = self.et_stamp - self.EIGHT_HOUR * period

        return self
