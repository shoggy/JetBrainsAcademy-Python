from datetime import datetime


def format_time(datetime_obj: datetime):
    print(datetime_obj.strftime("24h %H:%M"))
    print(datetime_obj.strftime("12h %I:%M"))
