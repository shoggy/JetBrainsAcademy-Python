from datetime import datetime


def get_week_number(datetime_obj: datetime):
    num = datetime_obj.strftime("%U")
    return f"Week number: {num}."
