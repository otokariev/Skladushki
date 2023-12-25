from django.contrib import admin

from .models import Account, About, Contacts, Sex

admin.site.register(Account)
admin.site.register(About)
admin.site.register(Contacts)
admin.site.register(Sex)
