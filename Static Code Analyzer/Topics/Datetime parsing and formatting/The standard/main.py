from datetime import datetime


def convert_to_standard(datetime_obj: datetime):
    return datetime_obj.strftime("%Y-%m-%d")
