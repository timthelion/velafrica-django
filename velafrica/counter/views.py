# -*- coding: utf-8 -*-
from django.shortcuts import render

from velafrica.counter.models import Entry


# Create your views here.

def counter(request):
    """
    Counter main view

    :model:`counter.Entry`
    """

    org_id = 0
    if 'id' in request.GET:
        org_id = int(request.GET.get('id'))

    statistics = Entry.get_statistics(org_id)

    print("STATS: {}".format(statistics))

    return render(request,
                  'counter/index.html', {
                      'org_id': statistics["org_id"],
                      'organisations': statistics["organisations"],
                      'velos_total': statistics["velos_total"],
                      'velos_thisyear': statistics["velos_thisyear"],
                      'velos_thismonth': statistics["velos_thismonth"],
                      'velos_thisweek': statistics["velos_thisweek"],
                      'velos_yesterday': statistics["velos_yesterday"],
                      'velos_today': statistics["velos_today"],
                      'velos_max': statistics["velos_max"],
                      'velos_max_date': statistics["velos_max_date"],
                  }
                  )
