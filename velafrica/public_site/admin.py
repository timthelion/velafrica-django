# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.html import format_html
from .models import DonationAmount, InvoiceOrder, SbbTicketOrder, WalkthroughRequest, \
    Content, TeamMember, References, ContactRequest, Partner, Event, EventDateTime, Supporter


class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['country']


class ContentAdminFilledFilter(admin.SimpleListFilter):
    title = 'Befüllt'
    parameter_name = 'filled'

    def lookups(self, request, model_admin):
        return (
            ('true', 'Ja'),
            ('false', 'Nein'),
        )

    def queryset(self, request, queryset):

        if self.value() == 'true':
            return queryset.all().exclude(value__isnull=True).exclude(value__exact='')
        elif self.value() == 'false':
            return queryset.all().filter(value='')
        else:
            return queryset.all()


class ContentAdmin(admin.ModelAdmin):
    search_fields = ['path', 'key', 'description', 'value']
    list_filter = ('language', 'path', ContentAdminFilledFilter)
    list_display = ['__str__', 'description', 'is_filled_column']

    def is_filled_column(self, object):
        source = 'yes' if object.value else 'no'
        return format_html(u'<img src="/static/admin/img/icon-{}.svg" alt="{}"'.format(source, source))
    is_filled_column.short_description = 'Befüllt'


class TeamMemberAdmin(admin.ModelAdmin):
    ordering = ('-sorting',)
    search_fields = ['name']
    list_filter = ('sorting',)


class ReferenceAdmin(admin.ModelAdmin):
    ordering = ('-sorting',)
    search_fields = ['name']
    list_filter = ('sorting',)


class SupporterAdmin(admin.ModelAdmin):
    ordering = ('-sorting',)
    search_fields = ['name']
    list_filter = ('sorting',)


class EventDateTimeInline(admin.TabularInline):
    model = EventDateTime
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = [EventDateTimeInline]


admin.site.register(Content, ContentAdmin)
admin.site.register(DonationAmount)
admin.site.register(Event, EventAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(References, ReferenceAdmin)
admin.site.register(InvoiceOrder)
admin.site.register(SbbTicketOrder)
admin.site.register(WalkthroughRequest)
admin.site.register(ContactRequest)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Supporter, SupporterAdmin)
