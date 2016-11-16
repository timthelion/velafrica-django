from django.conf.urls import include, url
from .views import order_invoice
from django.conf.urls import url
from .views import render_template, render_donation_template, \
                   render_map_template, order_invoice, \
                   thank_you, thank_you_paypal, render_sbb_ticker_order, \
                   render_walkthrough_template, render_about_us_template

donations = [
    url(r'^$', render_donation_template, name='home'),
    url(r'^orderinvoice/$', order_invoice, name='order_invoice'),
    url(r'^thank-you/$', thank_you, name='thank_you'),
    url(r'^thank-you-paypal/$', thank_you_paypal, name='thank_you_paypal'),
]

map = [
    url(r'^$', render_map_template, name='home'),
]

walkthroughs = [
    url(r'^sammelanlass/$', render_walkthrough_template, name='collection'),
    url(r'^frewillig/$', render_walkthrough_template, name='voluntary'),
    url(r'^firmen/$', render_walkthrough_template, name='company'),
    url(r'^schulen/$', render_walkthrough_template, name='school'),
]

urlpatterns = [
    url(r'^$', render_template, name='home'),
    url(r'^donation/', include(donations, namespace='donation')),
    url(r'^map/', include(map, namespace='map')),
    url(r'^sbb-ticket-order/$', render_sbb_ticker_order, name='sbbticket'),
    url(r'^mitmachen/', include(walkthroughs, namespace='walkthroughs')),
    url(r'^ueber-uns/$', render_about_us_template, name='ueberuns'),
]
