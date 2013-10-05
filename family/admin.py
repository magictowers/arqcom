from django.contrib import admin
from family.models import Person,Family,FamilyRole,Contact,ContactType


admin.site.register(Person)
admin.site.register(Family)
admin.site.register(FamilyRole)
admin.site.register(Contact)
admin.site.register(ContactType)