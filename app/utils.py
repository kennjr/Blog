from datetime import datetime
import time


def format_default_timestamp_single(user_item):
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")
