from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month in range(1, 13):
            for day, wd in self.itermonthdays2(year, month):
                if day != 0 and wd == weekday:
                    count += 1
        return count

# Ejemplos de uso
cal = MyCalendar()
print("Año: 2019, Día de la semana: 0, Ocurrencias:", cal.count_weekday_in_year(2019, 0))
print("Año: 2000, Día de la semana: 6, Ocurrencias:", cal.count_weekday_in_year(2000, 6))




