from django.contrib import admin
import datetime


from .models import AdvUser
from .utilities import send_activation_notification


def send_activation_notification(modeladmin, request, queryset):
    for rec in queryset:
        if not rec.is_activated:
            send_activation_notification(rec)

    modeladmin.message_user(request, 'Листи відправлені')


send_activation_notification.short_description = 'Відправка листа з активації'


class NoneActivatedFilter(admin.SimpleListFilter):
    title = 'Пройшли активацію?'
    parameter_name = 'actstate'

    def lookups(self, request, model_admin):
        return (
            ('activated', 'Пройшли'),
            ('threedays', 'Не Пройшли більше ніж 3 діб'),
            ('weeks', 'Не пройшли більше тижня'),
        )

    def queryset(self, request, queryset):
        val = self.value()
        if val == 'activated':
            return queryset.filter(is_active=True, is_activated=True)
        elif val == 'threedays':
            d = datetime.date.today() - datetime.timedelta(days=3)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)
        elif val == 'weeks':
            d = datetime.date.today() - datetime.timedelta(weeks=1)
            return queryset.filter(is_active=False, is_activated=False,
                                   date_joined__date__lt=d)


class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = (NoneActivatedFilter,)
    fields = (
        ('username', 'email'), ('first_name', 'last_name'),
        ('send_messages', 'is_active', 'is_activated'),
        ('is_staff', 'is_superuser'),
        ('groups', 'user_permissions'),
        ('last_login', 'date_joined'),
    )
    readonly_fields = ('last_login', 'date_joined')
    actions = (send_activation_notification,)


admin.site.register(AdvUser, AdvUserAdmin)
