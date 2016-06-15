# -*- coding: utf-8 -*-
from datetime import timedelta, date
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core import serializers

from velafrica.download.models import File
from velafrica.organisation.models import Organisation
from velafrica.sbbtracking.models import Tracking, TrackingEvent
from velafrica.stock.models import Category, Product, Stock, Warehouse
from velafrica.transport.models import Ride, Car, VeloState
from velafrica.velafrica_sud.models import Container


@login_required
def downloads(request):
  files = File.objects.all()
  return render_to_response(
    'download/index.html', 
    {'files': files}, 
    context_instance=RequestContext(request)
    )


@login_required
def profile(request):
  return render_to_response(
    'auth/profile.html',
    context_instance=RequestContext(request)
    )


def accounts_logout(request):
  """
  according to https://docs.djangoproject.com/en/1.9/topics/auth/default/
  """
  logout(request)
  return redirect('django.contrib.auth.views.login')


def home(request):
  return render_to_response('base.html', context_instance=RequestContext(request))

def tracking(request, tracking_no=0):
  """
  velo tracking
  """
  tracking = []
  tracking_events = []
  tno = tracking_no
  direct_access = False   # Indicates if visitor accessed tracking over direct url (/tracking/XYZ)

  if tno == 0:
    if 'tracking_no' in request.POST:
      tno = request.POST['tracking_no']
    else:
      pass

  if tno and tno != 0:
    tno = str(tno)
    tno = tno.upper()

    tracking = Tracking.objects.filter(tracking_no=tno).first()
    direct_access = True
    if tracking: 
      tracking_events = TrackingEvent.objects.filter(tracking=tracking.id)
    else:
      messages.add_message(request, messages.ERROR, "Kein Tracking mit der Nummer {} gefunden.".format(tno))

  return render_to_response('sbbtracking/index.html', {
    'tno': tno,
    'tracking': tracking,
    'tracking_events': tracking_events,
    'direct_access': direct_access,
    }, context_instance=RequestContext(request)
  )

@login_required
def transport(request):
  """
  transport
  """
  rides = Ride.objects.all()
  velos = 0
  for r in rides:
      velos += r.velos
  cars = Car.objects.all()
  return render_to_response('transport/index.html', {
    'rides': rides,
    'velos': velos,
    'cars': cars,
    }, context_instance=RequestContext(request)
  )

@login_required
def container(request):
  """
  container
  """
  containers = Container.objects.all()
  bicycles_total = 0
  for c in containers:
    bicycles_total += c.velos_loaded

  return render_to_response('velafrica_sud/container.html', {
    'containers': containers,
    'bicycles_total': bicycles_total,
    }, context_instance=RequestContext(request)
  )