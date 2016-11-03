from datetime import date, timedelta, datetime
from mada.core import active_users, new_users

from .data import users_profile_views, new_users_profile_views, new_users_likes
from .data import users_likes, new_users_comments, users_comments, users_shares, new_users_shares
from .models import Likes, Shares, Comments, ProfileViews

def update_current_comments(for_date):
    try:
        row = Comments.objects.get(dated=for_date)
        return
    except:
        row = Comments()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_comments(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_comments(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_likes(for_date):
    try:
        row = Likes.objects.get(dated=for_date)
        return
    except:
        row = Likes()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_likes(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_likes(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()
    
def update_current_shares(for_date):
    try:
        row = Shares.objects.get(dated=for_date)
        return
    except:
        row = Shares()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_shares(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_shares(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()
    
def update_current_profile_views(for_date):
    try:
        row = ProfileViews.objects.get(dated=for_date)
        return
    except:
        row = ProfileViews()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_profile_views(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_profile_views(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_last_month():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_current_likes(date_counter)
        update_current_comments(date_counter)
        update_current_shares(date_counter)
        update_current_profile_views(date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_day(ModelClass, for_date):
    delta = timedelta(days=1)
    try:
        row = ModelClass.objects.get(dated=for_date)
        row_yesterday = ModelClass.objects.get(dated=for_date-delta)
        row_before = ModelClass.objects.get(dated=for_date-delta*2)
        row_before_before = ModelClass.objects.get(dated=for_date-delta*3)
    except:
        return

    row.yesterday_dau = row_yesterday.dau
    row.before_dau = row_before.dau
    row.dau_compare = row.dau -row_yesterday.dau
    row.yesterday_dau_compare = row_yesterday.dau - row_before.dau
    row.before_dau_compare = row_before.dau - row_before_before.dau

    row.yesterday_nu = row_yesterday.nu
    row.before_nu = row_before.nu
    row.nu_compare = row.nu -row_yesterday.nu
    row.yesterday_nu_compare = row_yesterday.nu - row_before.nu
    row.before_nu_compare = row_before.nu - row_before_before.nu

    row.save()

def update_last_month_day():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_last_data_day(Likes, date_counter)
        update_last_data_day(Comments, date_counter)
        update_last_data_day(Shares, date_counter)
        update_last_data_day(ProfileViews, date_counter)

        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_week(ModelClass, for_date, days_count):
    delta = timedelta(days=1)
    counter = 0

    try:
        row = ModelClass.objects.get(dated=for_date)
    except:
        return

    total_dau = 0
    total_nu = 0

    while counter < days_count:
        for_date = for_date-delta
        try:
            row_old = ModelClass.objects.get(dated=for_date-delta)
            total_dau += row_old.dau
            total_nu += row_old.nu
        except:
            return

        counter += 1
    

    row.week_dau = total_dau/days_count
    row.week_nu = total_nu/days_count
    row.save()

def update_last_month_week():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_last_data_week(Likes, date_counter, 7)
        update_last_data_week(Comments, date_counter, 7)
        update_last_data_week(Shares, date_counter, 7)
        update_last_data_week(ProfileViews, date_counter, 7)

        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_month(ModelClass, for_date, days_count):
    delta = timedelta(days=1)
    counter = 0

    try:
        row = ModelClass.objects.get(dated=for_date)
    except:
        return

    total_dau = 0
    total_nu = 0

    while counter < days_count:
        for_date = for_date-delta
        try:
            row_old = ModelClass.objects.get(dated=for_date-delta)
            total_dau += row_old.dau
            total_nu += row_old.nu
        except:
            return

        counter += 1
    

    row.month_dau = total_dau/days_count
    row.month_nu = total_nu/days_count
    row.save()

def update_last_month_month():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_last_data_month(Likes, date_counter, 30)
        update_last_data_month(Comments, date_counter, 30)
        update_last_data_month(Shares, date_counter, 30)
        update_last_data_month(ProfileViews, date_counter, 30)

        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_week_month_compare(ModelClass, for_date):
    delta = timedelta(days=1)
    try:
        row = ModelClass.objects.get(dated=for_date)
        row_yesterday = ModelClass.objects.get(dated=for_date-delta)
    except:
        return

    try:
        row.week_dau_compare = row.week_dau - row_yesterday.week_dau
        row.week_nu_compare = row.week_nu - row_yesterday.week_nu
    except:
        pass

    try:
        row.month_dau_compare = row.month_dau - row_yesterday.month_dau
        row.month_nu_compare = row.month_nu - row_yesterday.month_nu
    except:
        pass

    row.save()

def update_last_month_week_month_compare():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_last_data_week_month_compare(Likes, date_counter)
        update_last_data_week_month_compare(Comments, date_counter)
        update_last_data_week_month_compare(Shares, date_counter)
        update_last_data_week_month_compare(ProfileViews, date_counter)

        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break