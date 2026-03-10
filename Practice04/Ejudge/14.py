def parse(line):
    date, tz = line.split()
    
    y, m, d = map(int, date.split("-"))
    
    from datetime import date
    days = date(y, m, d).toordinal()
    
    # парсим часовой пояс
    sign = 1 if tz[3] == "+" else -1
    hours = int(tz[4:6])
    minutes = int(tz[7:9])
    offset_minutes = sign * (hours * 60 + minutes)
    
    # переводим в минуты от некоторой базы
    return days * 1440 - offset_minutes

t1 = parse(input())
t2 = parse(input())

print(abs(t1 - t2) // 1440)