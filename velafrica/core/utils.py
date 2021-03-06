import googlemaps
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

# initialize client
gmaps = None
apiKey = getattr(settings, 'GMAP_API_KEY', '')
if (apiKey != ''):
    gmaps = googlemaps.Client(key=apiKey)
else:
    print("No GMAP_API_KEY set. Google map functionality not available.")



def get_geolocation(address):
    """
    Returns a dict of latitude (lat) and longitude (lng), which represents the first result received by Google Geocoding
    """
    if gmaps == None:
        return None
    geocode_result = gmaps.geocode(address)
    if geocode_result:
        return geocode_result[0]['geometry']['location']
    else:
        return None


def get_googlemaps_url_place(address):
    """
    """
    return u"https://maps.google.ch/maps/place/{}".format(address)


def get_distance(origin, destination):
    """
    Returns the distance in metres between two destinations.
    """
    if gmaps and origin and destination:
        distance_result = gmaps.distance_matrix(origin, destination, mode="driving")
        print(distance_result)
        if distance_result:
            return distance_result['rows'][0]['elements'][0]['distance']['value']
    else:
        return None


def get_googlemaps_url_distance(origin, destination):
    """
    """
    return u"https://maps.google.ch/maps/dir/{}/{}".format(origin, destination)


def send_mail(template, subject, receiver, context):
    """

    :param template:
    :param subject:
    :param receiver:
    :param context:
    :return:
    """
    content = get_template(template).render(context)
    # copied from tracking handlers
    from_name = getattr(settings, 'EMAIL_FROM_NAME', 'Velafrica Tracking')
    from_email = getattr(settings, 'EMAIL_FROM_EMAIL', 'tracking@velafrica.ch')
    sender = u"{} <{}>".format(from_name, from_email)
    msg = EmailMultiAlternatives(subject, content, sender, receiver)
    msg.attach_alternative(content, 'text/html')
    msg.send()
