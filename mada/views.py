from datetime import date, timedelta
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect


def site_main(request):
    today = date.today() - timedelta(days=1)
    context = RequestContext(request, {'today': today.strftime("%Y-%m-%d")})
    return render_to_response("index.html", context)



    