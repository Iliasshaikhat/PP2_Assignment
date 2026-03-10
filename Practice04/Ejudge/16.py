from datetime import datetime, timedelta, timezone
import re

def parse(line):
    m = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) UTC([+-])(\d{2}):(\d{2})', line)
    date_part, time_part, sign, hh, mm = m.groups()
    
    dt = datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H:%M:%S")
    
    offset = timedelta(hours=int(hh), minutes=int(mm))
    if sign == '-':
        offset = -offset
    
    tz = timezone(offset)
    return dt.replace(tzinfo=tz)

start = parse(input().strip())
end = parse(input().strip())

start_utc = start.astimezone(timezone.utc)
end_utc = end.astimezone(timezone.utc)

print(int((end_utc - start_utc).total_seconds()))