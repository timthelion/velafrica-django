# -*- coding: utf-8 -*-
from __future__ import print_function

from itertools import chain

from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse, resolve
from django.utils import timezone
from djangocms_blog.models import Post
from paypal.standard.forms import PayPalPaymentsForm

from velafrica.collection.models import Dropoff, CollectionEvent
from velafrica.core.settings import PAYPAL_RECEIVER_MAIL, GMAP_API_KEY, ORDER_RECEIVER
from velafrica.core.utils import send_mail
from velafrica.sbbtracking.models import Tracking, TrackingEvent
from .forms import InvoiceForm, SbbTicketOrderForm, WalkthroughRequestForm, ContactRequestForm
from .models import DonationAmount, TeamMember, References, Partner, Event, Supporter


def render_template(request):
    template_name = '/index'
    template_context = {}
    if request.path != '/cms/':
        template_name = request.path
        print("---> template name: {}".format(template_name))

    if request.path == '/cms/':
        template_context['velo_count'] = Tracking.get_tracked_velo_count()
        if Post.objects.count() > 0:
            template_context['blog_post'] = Post.objects.filter(publish=True).order_by('-date_published').first()
    print("Public_site: Render Template", template_name)
    return render(request, 'public_site' + template_name + '.html', template_context)


def render_map_template(request):
    template_name = 'public_site/map.html'
    template_context = {
        'nofooter': True,
        'api_key': GMAP_API_KEY,
        'map_data_url': reverse('api:public:dropoffs'),
        'sbb_ticket_order_url': reverse('home:sbbticket')
    }

    if request.user.is_authenticated:
        template_context['auth'] = True;

    if 'search' in request.GET:
        template_context.update({
            'search': request.GET['search']
        })

    return render(request, template_name, template_context)


def render_donation_template(request):
    template_name = 'public_site/donation.html'
    donation_amounts = DonationAmount.objects.filter(is_active=True).order_by('amount')
    paypal_dict = {
        "business": PAYPAL_RECEIVER_MAIL,
        "amount": donation_amounts.first().amount,
        "currency_code": "CHF",
        "item_name": "Velafrica Donation",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('home:donation:thank_you_paypal')),
        "cancel_return": request.build_absolute_uri(),
        "rm": "1",
        "custom": "Upgrade all users!",  # Custom command to correlate to some function later (optional)
    }
    paypalform = PayPalPaymentsForm(initial=paypal_dict)
    invoiceform = InvoiceForm()
    template_context = {
        'amounts': donation_amounts,
        'paypalform': paypalform,
        'invoiceform': invoiceform
    }

    return render(request, template_name, template_context)


def render_sbb_ticker_order(request):
    template_name = 'public_site/sbb_ticket_order.html'
    template_context = {
        'form': SbbTicketOrderForm(),
        'donation_url': reverse('home:donation:home')
    }

    if 'id' in request.GET:
        dropoff = Dropoff.objects.get(id=int(request.GET['id']))
        if dropoff:
            template_context.update({'dropoff': dropoff})
    else:
        dropoff = None

    if request.method == 'POST':
        form = SbbTicketOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.dropoff = dropoff
            order.save()

            email_context = {
                'dropoff': dropoff,
                'firstname': order.first_name,
                'lastname': order.last_name,
                'amount': order.amount,
                'address': u"{}, {}".format(order.address, order.zip),
                'email': order.email,
                'phone': order.phone,
                'note': order.note,
                'url': request.build_absolute_uri(reverse('admin:public_site_sbbticketorder_change', args=[order.pk]))
            }

            subject = 'Neue SBB Ticket Bestellung'

            send_mail('email/sbb_ticket_order.txt', subject, [ORDER_RECEIVER], email_context)

            template_context['success'] = True
        else:
            template_context['form'] = form

    return render(request, template_name, template_context)


def render_walkthrough_template(request):
    template_name = 'public_site/walkthrough.html'
    template_context = {
        'form': WalkthroughRequestForm(),
        'contact_form': ContactRequestForm()
    }

    partials = {
        'collection': 'public_site/partials/walkthroughs/collectionpoint.html',
        'company': 'public_site/partials/walkthroughs/company.html',
        'school': 'public_site/partials/walkthroughs/school.html',
        'voluntary': 'public_site/partials/walkthroughs/voluntary.html',
        'bicycle': 'public_site/partials/walkthroughs/bicycle.html'
    }

    template_context.update({
        'partial': partials.get(resolve(request.path).url_name, 'nothing')
    })

    if request.method == 'POST':
        if 'sammelanlass' in request.path:
            form = WalkthroughRequestForm(request.POST)
            if form.is_valid():
                walkthrough = form.save()

                email_context = {
                    'data': walkthrough,
                    'url': request.build_absolute_uri(
                        reverse('admin:public_site_walkthroughrequest_change', args=[walkthrough.pk])),
                }

                subject = 'Neue Sammelanlassanfrage'
                send_mail('email/walkthrough_request.txt', subject, [ORDER_RECEIVER], email_context)
                template_name = 'public_site/walkthrough-send.html'
            else:
                template_context['form'] = form
        else:
            form = ContactRequestForm(request.POST)
            if form.is_valid():
                contact_request = form.save()
                email_context = {
                    'data': contact_request,
                    'url': request.build_absolute_uri()
                }
                subject = 'Neue Anfrage über Kontaktformular'
                if 'send_to_mail' in request.POST:
                    receiver = request.POST['send_to_mail']
                else:
                    receiver = ORDER_RECEIVER
                send_mail('email/contact.txt', subject, [receiver], email_context)
                template_name = 'public_site/walkthrough-send.html'
            else:
                template_context['contact_form'] = form

    return render(request, template_name, template_context)


def order_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoiceorder = form.save()

            email_context = {
                'firstname': form.cleaned_data['first_name'],
                'lastname': form.cleaned_data['last_name'],
                'address': u"{}, {}".format(form.cleaned_data['address'], form.cleaned_data['zip']),
                'comment': form.cleaned_data['comment'],
                'number_invoices': form.cleaned_data['number_invoices'],
                'donation_amount': form.cleaned_data['donation_amount'],
                'url': request.build_absolute_uri(
                    reverse('admin:public_site_invoiceorder_change', args=[invoiceorder.pk])),
            }

            subject = 'Neue ESR Bestellung'

            send_mail('email/invoice_order.txt', subject, [ORDER_RECEIVER], email_context)
            return redirect(form.cleaned_data['invoice_redirect_url'])
        else:
            # TODO: track error with rollbar
            return redirect('/')


def thank_you(request):
    template_name = 'public_site/donation-thank-you.html'
    return render(request, template_name, {})


def thank_you_paypal(request):
    template_name = 'public_site/donation-thank-you.html'
    return render(request, template_name, {'paypal': True})


def render_about_us_template(request):
    template_name = 'public_site/ueber-uns.html'
    template_context = {}

    if References.objects.count() > 0:
        template_context.update({
            'references': References.objects.filter(active=True).order_by('-sorting')
        })

    if TeamMember.objects.count() > 0:
        template_context.update({
            'team': TeamMember.objects.filter(active=True).order_by('-sorting')
        })

    return render(request, template_name, template_context)


def render_personal_tracking(request, tracking_no=''):
    template_name = 'public_site/my-tracking.html'
    template_context = {}

    fb_app_id = getattr(settings, 'FACEBOOK_APP_ID', '')

    try:
        tracking = Tracking.objects.get(tracking_no=tracking_no.upper())
        tracking_events = TrackingEvent.objects.filter(tracking=tracking.id).order_by('-datetime')

        template_context.update({
            'tracking': tracking,
            'tracking_events': tracking_events,
        })
    except Tracking.DoesNotExist:
        # Ticket Order
        template_context.update({
            'tracking': False
        })

    return render(request, template_name, template_context)


def render_tracking(request):
    template_name = 'public_site/tracking.html'

    last_events = Tracking.objects.all().values('last_event')
    data = {}
    keynames = {
        1: 'tracking_erstellt',
        2: 'eingang_velafrica_partner',
        4: 'containerverlad',
        5: 'ankunft_afrika',
        6: 'verkauf',
        7: 'zerlegung',
        8: 'export'
    }
    for id in last_events:
        last_event_event_type = TrackingEvent.objects.get(id=id.get('last_event')).event_type
        keyname = keynames.get(last_event_event_type.id, last_event_event_type.name)
        if keyname in data:
            data[keyname] += 1
        else:
            data[keyname] = 1

    data['weg_afrika'] = data.get('export', 0) + data.get('containerverlad', 0)

    tracking_created_id = 1

    data['tracking_erstellt'] = TrackingEvent.objects.filter(event_type_id=tracking_created_id).count()
    data['total'] = Tracking.get_tracked_velo_count(this_year=True, without_initial=True)

    template_context = {
        'data': data
    }

    return render(request, template_name, template_context)


def render_partners(request):
    template_name = 'public_site/partner.html'

    if 'afrika' in request.path:
        choice = 1
        section_id = 'africa'
    elif 'schweiz' in request.path:
        choice = 2
        section_id = 'swiss'

    all = Partner.objects.filter(country=choice).order_by('-teaserd')
    teaserd = all[:4]
    rest = all[4:]

    template_context = {
        'section_id': section_id,
        'teaserd': teaserd,
        'partners': rest
    }

    return render(request, template_name, template_context)


def render_impressum_template(request):
    template_name = 'public_site/impressum.html'
    return render(request, template_name, {})


def render_agenda(request):
    template_name = 'public_site/agenda.html'
    template_context = {}

    events = Event.objects.filter(active=True).all()

    coll_events = list()
    for collectionevent in CollectionEvent.objects.filter(date_end__gte=timezone.now().date().strftime('%Y-%m-%d')) \
            .exclude(event__address=None):
        new_event = Event(
            name=collectionevent.event.name,
            active=True,
            category=collectionevent.event.category,
            address=collectionevent.event.address,
            description=collectionevent.event.description,
            organizer=collectionevent.event.host
        )
        if collectionevent.date_start == collectionevent.date_end:
            date = u"{}".format(collectionevent.date_start.strftime('%d.%m.%Y'))
        else:
            date = u"{} - {}".format(collectionevent.date_start.strftime('%d.%m'),
                                     collectionevent.date_end.strftime('%d.%m.%Y'))
        new_event.date = date
        new_event.id = -1 * collectionevent.id
        coll_events.append(new_event)

    all_events = list(chain(events, coll_events))
    template_context['events'] = all_events
    return render(request, template_name, template_context)


def render_specific_agenda(request, event_id):
    template_name = 'public_site/agenda_detail.html'
    template_context = {}

    if "-" in event_id:
        event_id = int(event_id.replace('-', ''))
        coll_event = CollectionEvent.objects.filter(pk=event_id).first()
        if coll_event:
            event = Event(
                name=coll_event.event.name,
                active=True,
                category=coll_event.event.category,
                address=coll_event.event.address,
                description=coll_event.event.description,
                organizer=coll_event.event.host
            )
        if coll_event.date_start == coll_event.date_end:
            date = u"{}".format(coll_event.date_start.strftime('%d.%m'))
        else:
            date = u"{} - {}".format(coll_event.date_start.strftime('%d.%m'), coll_event.date_end.strftime('%d.%m'))
        template_context['datetime'] = u"{}, {}".format(date, coll_event.time)
    else:
        event = Event.objects.filter(pk=event_id).first()

    if not event:
        return redirect(reverse('home:agenda:index'))

    template_context['event'] = event

    return render(request, template_name, template_context)


def render_supporter(request):
    template_name = 'public_site/supporter.html'
    template_context = {
        'supporter': Supporter.objects.filter(active=True).order_by('-sorting')
    }

    return render(request, template_name, template_context)


def render_impact(request):
    template_name = 'public_site/impact.html'
    return render(request, template_name,{})
