class WeekDayError(Exception):
    pass

class Weeker:
    DAYS_OF_WEEK = ['Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab', 'Dom']

    def __init__(self, day):
        if day not in self.DAYS_OF_WEEK:
            raise WeekDayError("Día de la semana no válido")
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = self.DAYS_OF_WEEK[(self.DAYS_OF_WEEK.index(self.__day) + n) % 7]

    def subtract_days(self, n):
        self.add_days(-n)

try:
    weekday = Weeker('InvalidDay')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")



