from datetime import datetime


def get_weekday(datetime_obj: datetime):
    return datetime_obj.strftime("%A")
