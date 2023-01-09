from django.contrib import admin

from .models import *

admin.site.register(FormOfTheCabin)
admin.site.register(TypeOfCabin)

admin.site.register(BankDetail)
admin.site.register(DepartmentAddress)
admin.site.register(DetailsOfTheOrganization)

admin.site.register(TreeSpecies)
admin.site.register(LocalityType)
admin.site.register(Organization)
admin.site.register(ValidityPeriod)
admin.site.register(Forestry)