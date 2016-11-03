from datetime import date, timedelta

from .models import Started, Completed, CompletedDrop
from .data import users_started_transaction, new_users_started_transaction, users_completed_transaction, new_users_completed_transaction

from mada.core import active_users, new_users


def update_started(for_date):
    try:
        row = Started.objects.get(dated=for_date)
        return
    except:
        row = Started()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_started_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_started_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_completed(for_date):
    try:
        row = Completed.objects.get(dated=for_date)
        return
    except:
        row = Completed()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_completed_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_completed_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_completed_drop(for_date):
    try:
        row = CompletedDrop.objects.get(dated=for_date)
        return
    except:
        row = CompletedDrop()
        row_started = Started.objects.get(dated=for_date)
        row_completed = Completed.objects.get(dated=for_date)


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = row_started.dau_total
    dau = row_started.dau - row_completed.dau
    nu_total = row_started.nu_total
    nu = row_started.nu - row_completed.nu

    row.dau_total = dau_total
    row.dau = dau
    row.nu_total = nu_total
    row.nu = nu
    row.dated = for_date

    row.save()

def update_last_month():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_completed_drop(date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_started(for_date):
    delta = timedelta(days=1)
    try:
        row = Started.objects.get(dated=for_date)
        row_yesterday = Started.objects.get(dated=for_date-delta)
        row_before = Started.objects.get(dated=for_date-delta*2)
    except:
        return

    row.yesterday_dau = row_yesterday.dau
    row.before_dau = row_before.dau
    row.dau_compare = row.dau -row_yesterday.dau
    row.yesterday_dau_compare = row_yesterday.dau - row_before.dau

    row.yesterday_nu = row_yesterday.nu
    row.before_nu = row_before.nu
    row.nu_compare = row.nu -row_yesterday.nu
    row.yesterday_nu_compare = row_yesterday.nu - row_before.nu

    row.save()

def update_last_data_completed(for_date):
    delta = timedelta(days=1)
    try:
        row = Completed.objects.get(dated=for_date)
        row_yesterday = Completed.objects.get(dated=for_date-delta)
        row_before = Completed.objects.get(dated=for_date-delta*2)
    except:
        return

    row.yesterday_dau = row_yesterday.dau
    row.before_dau = row_before.dau
    row.dau_compare = row.dau -row_yesterday.dau
    row.yesterday_dau_compare = row_yesterday.dau - row_before.dau

    row.yesterday_nu = row_yesterday.nu
    row.before_nu = row_before.nu
    row.nu_compare = row.nu -row_yesterday.nu
    row.yesterday_nu_compare = row_yesterday.nu - row_before.nu

    row.save()

def update_last_data_drop(for_date):
    delta = timedelta(days=1)
    try:
        row = CompletedDrop.objects.get(dated=for_date)
        row_yesterday = CompletedDrop.objects.get(dated=for_date-delta)
        row_before = CompletedDrop.objects.get(dated=for_date-delta*2)
    except:
        return

    row.yesterday_dau = row_yesterday.dau
    row.before_dau = row_before.dau
    row.dau_compare = row.dau -row_yesterday.dau
    row.yesterday_dau_compare = row_yesterday.dau - row_before.dau

    row.yesterday_nu = row_yesterday.nu
    row.before_nu = row_before.nu
    row.nu_compare = row.nu -row_yesterday.nu
    row.yesterday_nu_compare = row_yesterday.nu - row_before.nu

    row.save()

def update_same_model():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_last_data_started(date_counter)
        update_last_data_completed(date_counter)
        update_last_data_drop(date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_last_data_before_compare(ModelClass, for_date):
    delta = timedelta(days=2)
    try:
        row = ModelClass.objects.get(dated=for_date)
        row_before = ModelClass.objects.get(dated=for_date-delta)
    except:
        return

    row.before_dau_compare = row_before.dau_compare
    row.before_nu_compare = row_before.nu_compare
    row.save()

def update_same_model_before_compare():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_last_data_before_compare(Started, date_counter)
        update_last_data_before_compare(Completed, date_counter)
        update_last_data_before_compare(CompletedDrop, date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_week_data(ModelClass, for_date, days_count):
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

def update_same_model_week():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_week_data(Started, date_counter, 7)
        update_week_data(Completed, date_counter, 7)
        update_week_data(CompletedDrop, date_counter, 7)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_month_data(ModelClass, for_date, days_count):
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

def update_same_model_month():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_month_data(Started, date_counter, 30)
        update_month_data(Completed, date_counter, 30)
        update_month_data(CompletedDrop, date_counter, 30)
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

def update_same_model_week_month_compare():
    date_counter = date.today() - timedelta(days=60)

    while True:
        update_last_data_week_month_compare(Started, date_counter)
        update_last_data_week_month_compare(Completed, date_counter)
        update_last_data_week_month_compare(CompletedDrop, date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break

def update_continuous_started(for_date):
    delta = timedelta(days=1)
    try:
        row = Started.objects.get(dated=for_date)
    except:
        row = Started()

    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_started_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_started_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_continuous_completed(for_date):
    delta = timedelta(days=1)
    try:
        row = Completed.objects.get(dated=for_date)
    except:
        row = Completed()

    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau_total = active_users(for_date_text, for_date_text)
    dau = users_completed_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu_total = new_users(for_date_text, for_date_text)
    nu = new_users_completed_transaction(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau_total = len(dau_total)
    row.dau = len(dau)
    row.nu_total = len(nu_total)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_continuous_completed_drop(for_date):
    try:
        row = CompletedDrop.objects.get(dated=for_date)
    except:
        row = CompletedDrop()

    try:
        row_started = Started.objects.get(dated=for_date)
        row_completed = Completed.objects.get(dated=for_date)
    except:
        return

    dau_total = row_started.dau_total
    dau = row_started.dau - row_completed.dau
    nu_total = row_started.nu_total
    nu = row_started.nu - row_completed.nu

    row.dau_total = dau_total
    row.dau = dau
    row.nu_total = nu_total
    row.nu = nu
    row.dated = for_date

    row.save()

def update_continuous(ModelClass, for_date):
    delta = timedelta(days=1)
    try:
        row = ModelClass.objects.get(dated=for_date)
        row_yesterday = ModelClass.objects.get(dated=for_date - delta)
        row_before = ModelClass.objects.get(dated=for_date - delta*2)
        row_week = ModelClass.objects.get(dated=for_date - delta*8)
        row_month = ModelClass.objects.get(dated=for_date - delta*31)
    except:
        return


    for_date_text = int(for_date.strftime("%Y%m%d"))

    row.dau_compare = row.dau - row_yesterday.dau
    row.yesterday_dau = row_yesterday.dau
    row.yesterday_dau_compare = row_yesterday.dau_compare
    row.before_dau = row_before.dau
    row.before_dau_compare = row_before.dau_compare

    row.nu_compare = row.nu - row_yesterday.nu
    row.yesterday_nu = row_yesterday.nu
    row.yesterday_nu_compare = row_yesterday.nu_compare
    row.before_nu = row_before.nu
    row.before_nu_compare = row_before.nu_compare

    row.week_dau = row_yesterday.week_dau + row_yesterday.dau/7 - row_week.dau/7
    row.week_dau_compare = row.week_dau - row_yesterday.week_dau
    row.month_dau = row_yesterday.month_dau + row_yesterday.dau/7 - row_month.dau/7
    row.month_dau_compare = row.month_dau - row_yesterday.month_dau

    row.save()

def update_transactions_for_day(date):
    update_continuous_started(date)
    update_continuous_completed(date)
    update_continuous_completed_drop(date)

def update_lag():
    delta = timedelta(days=1)
    starter = date.today() - delta
    end = date.today() - delta*7

    while starter >= end:
        update_transactions_for_day(starter)
        starter -= delta