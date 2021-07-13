duration = int(input('Введите количество секунд:'))
if duration /60 < 1 :
    print(duration, 'sec')
elif duration < 3600:
     duration /60 > 1
     min = float(duration)/60
     sec = duration % 60
     print(int(min), 'min', sec,'sec')
elif duration < 86400:
    duration /60 >= 60
    hour = float(duration) / 3600
#ввел промежутотчную переменную, чтобы корректно считались минуты
    min_promezh = duration % 3600
    min = min_promezh / 60
    sec = duration % 60
    print(int(hour),'hour', int(min), 'min', sec, 'sec')
elif duration >= 86400:
    duration / 60 >= 1440
    day = duration / 86400
    hour = (duration % 86400) / 3600
    min_promezh = duration % 3600
    min = min_promezh / 60
    sec = duration % 60
    print(int(day),'day',int(hour), 'hour', int(min), 'min', sec, 'sec')



