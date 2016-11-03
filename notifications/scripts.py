from datetime import date, timedelta, datetime
from mada.core import active_users, new_users

from .data import users_accepted_notifications, new_users_accepted_notifications, users_rejected_notifications, new_users_rejected_notifications
from .data import new_users_accepted_social_notifications, users_accepted_social_notifications, new_users_rejected_social_notifications, users_rejected_social_notifications
from .data import new_users_accepted_commerce_notifications, users_accepted_commerce_notifications, new_users_rejected_commerce_notifications, users_rejected_commerce_notifications
from .models import Opens, Rejects, OpensSocial, RejectsSocial, OpensCommerce, RejectsCommerce

def update_current_opens(for_date):
    try:
        row = Opens.objects.get(dated=for_date)
        return
    except:
        row = Opens()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_accepted_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_accepted_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_rejects(for_date):
    try:
        row = Rejects.objects.get(dated=for_date)
        return
    except:
        row = Rejects()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_rejected_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_rejected_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_opens_social(for_date):
    try:
        row = OpensSocial.objects.get(dated=for_date)
        return
    except:
        row = OpensSocial()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_accepted_social_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_accepted_social_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_rejects_social(for_date):
    try:
        row = RejectsSocial.objects.get(dated=for_date)
        return
    except:
        row = RejectsSocial()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_rejected_social_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_rejected_social_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_opens_commerce(for_date):
    try:
        row = OpensCommerce.objects.get(dated=for_date)
        return
    except:
        row = OpensCommerce()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_accepted_commerce_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_accepted_commerce_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_current_rejects_commerce(for_date):
    try:
        row = RejectsCommerce.objects.get(dated=for_date)
        return
    except:
        row = RejectsCommerce()


    for_date_text = int(for_date.strftime("%Y%m%d"))

    dau = users_rejected_commerce_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)
    nu = new_users_rejected_commerce_notifications(for_date_text, for_date_text,
        for_date_text, for_date_text)

    row.dau = len(dau)
    row.nu = len(nu)
    row.dated = for_date

    row.save()

def update_last_month():
    date_counter = datetime.strptime('2016-06-01', "%Y-%m-%d").date()

    while True:
        update_current_opens(date_counter)
        update_current_rejects(date_counter)
        update_current_opens_social(date_counter)
        update_current_rejects_social(date_counter)
        update_current_opens_commerce(date_counter)
        update_current_rejects_commerce(date_counter)
        date_counter = date_counter + timedelta(days=1)

        if date_counter > date.today():
            break