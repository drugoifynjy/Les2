from django.contrib import admin

from .models import *

admin.site.register(FormOfTheCabin)
admin.site.register(TypeOfCabin)

admin.site.register(BankDetail)

admin.site.register(DetailsOfTheOrganization)
admin.site.register(OrganizationValidityPeriod)
admin.site.register(BankDetailValidityPeriod)
admin.site.register(DetailsOfTheOrganizationValidityPeriod)
admin.site.register(OrganizationAddressValidityPeriod)
admin.site.register(ForestryValidityPeriod)
admin.site.register(DepartmentAddressValidityPeriod)
admin.site.register(OrganizationAddress)
admin.site.register(TreeSpecies)
admin.site.register(LocalityType)
admin.site.register(Organization)
admin.site.register(Forestry)
admin.site.register(DepartmentAddress)
