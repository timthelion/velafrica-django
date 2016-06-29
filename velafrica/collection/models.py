# -*- coding: utf-8 -*-
from datetime import timedelta, date
from django.utils import timezone
from django.db import models
from simple_history.models import HistoricalRecords
from velafrica.organisation.models import Organisation, Municipality

def get_default_task_status():
    """
    just here for migrations, delete later
    """
    pass


class EventCategory(models.Model):
    """
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name = "Event Kategorie"
        verbose_name_plural = "Event Kategorien"


class Event(models.Model):
    """
    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, verbose_name="Beschreibung")
    category = models.ForeignKey(EventCategory, verbose_name="Kategorie")
    yearly = models.BooleanField(default=False, verbose_name="Jährlich wiederkehrend?")
    host = models.CharField(max_length=255, verbose_name="Veranstalter")
    municipality = models.ForeignKey(Municipality, verbose_name="Ort")
    address = models.TextField(blank=True)

    def __unicode__(self):
        return u"{}".format(self.name)

    class Meta:
        verbose_name = "Event"


class Task(models.Model):
    """
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{}".format(self.name)


class CollectionEvent(models.Model):
    """
    """
    date_start = models.DateField()
    date_end = models.DateField()
    event = models.ForeignKey(Event)
    time = models.CharField(max_length=255, blank=True, verbose_name="Veloannahme", help_text="Zeit für Veloannahme")
    notes = models.TextField(blank=True, verbose_name="weitere Infos", help_text="Weitere Infos / Bemerkungen")

    # logistics
    presence_velafrica = models.BooleanField(default=False, verbose_name="Präsenz Velafrica?")
    presence_velafrica_info = models.TextField(
        blank=True, 
        help_text="Infos zur Präsenz von Velafrica am Event",
        verbose_name="Präsenz Velafrica")
    collection = models.TextField(
        blank=True,
        help_text="Infos zur Abholung der Velos",
        verbose_name="Abtransport")
    processing = models.ForeignKey(
        Organisation,
        verbose_name="Velo Verarbeitung",
        related_name="processing_organisation")
    collection_partner_vrn = models.ForeignKey(
        Organisation, 
        blank=True, 
        null=True,
        verbose_name="Abtransport durch VRN Partner",
        help_text="Velafrica Partner der die Velos abholt",
        related_name="collection_organisation")
    collection_partner_other = models.CharField(
        max_length=255, 
        blank=True, 
        verbose_name="Abtransport durch andere Organisation",
        help_text="Wenn die Velos nicht von einem Velafrica Partner abgeholt werden, bitte hier eintragen von wem")
    collection_partner_confirmed = models.BooleanField(default=False, verbose_name="Transport Partner bestätigt?")

    # marketing
    website = models.URLField(blank=True, help_text="Website des Events")

    # results
    feedback = models.BooleanField(default=False, verbose_name="Feedback eingeholt?")
    velo_amount = models.IntegerField(default=0, verbose_name="Anzahl gesammelte Velos")
    people_amount = models.IntegerField(default=0, verbose_name='Anzahl Helfer vor Ort')
    hours_amount = models.IntegerField(default=0, verbose_name='Geleistete Stunden', help_text="Anzahl geleistete Stunden von allen Helfern zusammen")
    money_amount = models.IntegerField(default=0, verbose_name='Gesammeltes Geld', help_text="Betrag in CHF der am Event gesammelt wurde")
    additional_results = models.TextField(blank=True, verbose_name="weitere Resultate", help_text="Zusätzliche Resultate / Erkenntnisse")

    def get_status_logistics(self):
        if self.collection_partner_confirmed:
            return "success"
        else:
            return "danger"

    def get_status_marketing(self):
        print "HALLOOOO"
        tasks_count = self.taskprogress_set.all().count()
        print tasks_count
        if tasks_count == 0:
            return "danger"
        else:
            success_count = 0
            for t in self.taskprogress_set.all():
                if t.status:
                    success_count += 1
            if tasks_count == success_count:
                return "success"
            else:
                return "warning"

    def get_status_results(self):
        if self.feedback:
            return "success"
        return "danger"

    def __unicode__(self):
        return u"{} ({} bis {})".format(self.event.name, self.date_start, self.date_end)

    class Meta:
        verbose_name = "Sammelanlass"
        verbose_name_plural = "Sammelanlässe"


class TaskProgress(models.Model):
    """
    """
    collection_event = models.ForeignKey(CollectionEvent)
    task = models.ForeignKey(Task)
    notes = models.TextField(blank=True, verbose_name="Notizen")
    status = models.BooleanField(default=False, verbose_name="Erledigt?")

    def __unicode__(self):
        return u"{}: {}".format(self.task, self.status)

    class Meta:
        verbose_name = "Task Fortschritt"
        verbose_name_plural = "Task Fortschritte"