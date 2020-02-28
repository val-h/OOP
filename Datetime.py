from datetime import datetime

rnd_date = '29.07.1954'

parsed_date = datetime.strptime(rnd_date, "%d.%m.%Y")

print(parsed_date)