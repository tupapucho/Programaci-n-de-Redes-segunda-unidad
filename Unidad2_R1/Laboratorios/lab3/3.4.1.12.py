'''
Autor: Antonio Uribe Ramirez
lab: 3.4.1.12
fecha: 22/11/10
'''
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds

    def __str__(self):
        return f"{self.__format_digit(self.__hours)}:{self.__format_digit(self.__minutes)}:{self.__format_digit(self.__seconds)}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds, self.__minutes = 0, self.__minutes + 1
            if self.__minutes == 60:
                self.__minutes, self.__hours = 0, self.__hours + 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds, self.__minutes = 59, self.__minutes - 1
            if self.__minutes == -1:
                self.__minutes, self.__hours = 59, self.__hours - 1
                if self.__hours == -1:
                    self.__hours = 23

    def __format_digit(self, digit):
        return f"0{digit}" if digit < 10 else str(digit)

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
