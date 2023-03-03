#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
    @author:goukaiyu
    @email:goukaiyu@163.com
    @time:2021/8/19 4:13 下午
    @File: date.py
    @project_name: Yingyue-bot
"""
import datetime
import time

hours = 7
Time_zone = datetime.timedelta(hours=hours)


def get_today_date():
    return str((datetime.datetime.today() - Time_zone).date())


def get_yesterday():
    return str((datetime.datetime.today() - Time_zone - datetime.timedelta(days=1)).date())


def get_tomorrow():
    return str((datetime.datetime.today() - Time_zone + datetime.timedelta(days=1)).date())


def get_now_time():
    return str(datetime.datetime.now() - Time_zone).split('.')[0]


def get_now_hour_minute():
    now = datetime.datetime.now() - Time_zone
    hour = now.hour
    minute = now.minute
    second = now.second
    return int(f'{str(hour).zfill(2)}{str(minute).zfill(2)}{str(second).zfill(2)}')


def get_now_datetime():
    now = datetime.datetime.now() - Time_zone
    return now


def get_week_num():
    return int(datetime.datetime.weekday(datetime.datetime.today() - Time_zone ))


def get_week_num4date(date):
    return int(datetime.datetime.weekday(date))


def get_monday4date(date, end_date=False):
    """
    得到传入日期周的周一
    :return:
    """
    if type(date) == str:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    if not end_date:
        return get_date4date_diff(date, get_week_num4date(date))
    start_date = get_date4date_diff(date, get_week_num4date(date))
    end_date = get_date4date_diff(start_date, -6)
    return start_date, end_date


def get_date4date_diff(date, num):
    """
    得到 date - num 的日期
    :param date:
    :param num:
    :return:
    """
    if type(date) == str:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    new_start_date = date - datetime.timedelta(days=num)
    # new_end_date = new_start_date + datetime.timedelta(days=6)

    return str(new_start_date).split(" ")[0]


def get_time4time_diff(t, **dt):
    """
    得到 time - num 的日期
    :param t:
    :param dt:
    :return:
    """
    if type(t) == str:
        t = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    new_start_date = t - datetime.timedelta(**dt)

    return str(new_start_date)


def get_now_time_stamp():
    return time.time()


def time_or_date_to_timestamp(time_str: str):
    if " " not in time_str:
        time_str += ' 00:00:00'
    return time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))


def str2datetime(time_str):
    if " " not in time_str:
        time_str += ' 00:00:00'
    return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")


def date_difference(start, end):
    """
    日期差
    :param start:
    :param end:
    :return: end - start
    """
    start_date = str2datetime(start)
    end_date = str2datetime(end)
    return (end_date - start_date).days


def time_str_difference(start, end):
    """
    日期差
    :param start:
    :param end:
    :return: end - start
    """
    start_date = str2datetime(start)
    end_date = str2datetime(end)

    return f"{end_date - start_date}"


if __name__ == '__main__':
    next_time = get_tomorrow() + " 02:00:00"
    now = get_now_time()

    print(time_str_difference('2021-12-21 00:00:00', '2021-12-21 00:01:00'))
#     from datetime import datetime, timezone
#     print(datetime.now(timezone.utc))
