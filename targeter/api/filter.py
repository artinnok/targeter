from datetime import datetime
from datetime import timedelta


def is_old(item):
    created_time = datetime.fromtimestamp(int(item['created_time']))
    return datetime.now() - created_time < timedelta(days=30)


def has_caption(item):
    return item['caption']
