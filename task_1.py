import re

class Time(object):
    def __init__(self, hr, mn, sec):
        self.hour = hr
        self.minute = mn
        self.second = sec

    def convert(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def __str__(self):
        return f"{self.hour} hours {self.minute} minutes {self.second} seconds"

    def __add__(self, other):
        seconds = self.convert() + other.convert()
        return Time(seconds//3600, (seconds % 3600) // 60, seconds % 60)

    def __sub__(self, other):
        seconds = self.convert() - other.convert()
        return Time(seconds//3600, (seconds % 3600) // 60, seconds % 60)

    def __eq__(self, other):
        return self.convert() == other.convert()

    def __le__(self, other):
        return self.convert() <= other.convert()

    def __lt__(self, other):
        return self.convert() < other.convert()

    def __ge__(self, other):
        return self.convert() >= other.convert()

    def __gt__(self, other):
        return self.convert() > other.convert()

    def __hash__(self):
        return hash((self.hour, self.minute, self.second))

    def __repr__(self):
        return str(self) + f'; hash:{hash(self)}'


class Time1(object):
    def __init__(self, strng):
        if re.compile(r"([0-9]{1,2})+\s*hours?").search(strng):
            self.hours = int(re.compile(r"([0-9]{1,2})+\s*hours?").findall(strng)[0])
        else:
            self.hours = 0
        if re.compile(r"([0-9]{1,2})+\s*minutes?").search(strng):
            self.minutes = re.compile(r"([0-9]{1,2})+\s*minutes?").findall(strng)[0]
        else:
            self.minutes = 0
        if re.compile(r"([0-9]{1,2})+\s*seconds?").search(strng):
            self.seconds = re.compile(r"([0-9]{1,2})+\s*seconds?").findall(strng)[0]
        else:
            self.seconds = 0

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes {self.seconds} seconds"


class Time2(object):
    def __init__(self, lst):
        self.hours = lst[0] if len(lst) > 0 else 0
        self.minutes = lst[1] if len(lst) > 1 else 0
        self.seconds = lst[2] if len(lst) > 2 else 0

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes {self.seconds} seconds"

class NanoTime(Time):
    def __init__(self, hr, mn, sec, nanos):
        super().__init__(hr, mn, sec)
        self.nanos = nanos

    def __str__(self):
        return f"{self.hour} hours {self.minute} minutes {self.second} seconds {self.nanos} nanoseconds"

    def convert(self):
        return self.hour * 3600 + self.minute * 60 + self.second + self.nanos/1000000000

    def __hash__(self):
        return hash((self.hour, self.minute, self.second, self.nanos))



t = Time2([1,4])
print(t)
