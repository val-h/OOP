from datetime import datetime

parsed_date = datetime.strptime(input('Target date: '), "%d.%m.%Y")

print(parsed_date.strftime('%d %m %Y'))
