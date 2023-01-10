from django.db import models
from .abstract_models import *


class FormOfTheCabin(models.Model):
    form_of_the_cabin = models.TextField(null=True, verbose_name='Форма рубки',)

    def __str__(self):
        a = str(self.form_of_the_cabin.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Форма рубки'
        verbose_name_plural = 'Формы рубки'


class TypeOfCabin(models.Model):
    type_of_cabin = models.TextField(null=True, verbose_name='Тип рубки')

    def __str__(self):
        a = str(self.type_of_cabin.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Тип рубки'
        verbose_name_plural = 'Типы рубки'


class TreeSpecies(models.Model):
    tree_species = models.CharField(max_length=255, null=True, verbose_name='Порода дерева')

    def __str__(self):
        a = str(self.tree_species.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Порода дерева'
        verbose_name_plural = 'Породы деревьев'


class OrganizationValidityPeriod(ValidityPeriod, models.Model):
    pass

    def __str__(self):
        a = 'Период действия организации ' + str(self.start_date.__str__()) + ' ' + str(self.end_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия организации'
        verbose_name_plural = 'Периоды действия организаций'


class Organization(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name='Организация')
    validity_period = models.ForeignKey(OrganizationValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия')

    def __str__(self):
        a = str(self.title.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class DetailsOfTheOrganizationValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        a = 'Период действия реквизитов организации ' + str(self.start_date.__str__()) + ' ' + str(self.end_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия реквизитов организации'
        verbose_name_plural = 'Периоды действия реквизитов организаций'


class DetailsOfTheOrganization(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, verbose_name='Организация')
    inn = models.IntegerField(null=True, verbose_name='ИНН')
    kpp = models.IntegerField(null=True, verbose_name='КПП')
    ogrn = models.IntegerField(null=True, verbose_name='ОГРН')
    okpo = models.IntegerField(null=True, verbose_name='ОКПО')
    email = models.CharField(max_length=255, null=True, verbose_name='электронная почта')
    validity_period = models.ForeignKey(DetailsOfTheOrganizationValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период дейсвтия реквизитов организации')

    def __str__(self):
        a = str(self.organization.__str__()) + ', ОГРН ' + str(self.ogrn.__str__()) + \
            str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Реквизиты организации'
        verbose_name_plural = 'Реквизиты организаций'


class BankDetailValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        if self.end_date:
            a = 'действующие с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'действуют с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия банковских реквизитов организации'
        verbose_name_plural = 'Периоды действия банковских реквизитов организаций'


class BankDetail(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True,
                                     verbose_name='Организация')
    bank_title = models.TextField(null=True, verbose_name='Название банка')
    payment_account = models.IntegerField(null=True, verbose_name='Расчетный счет')
    corset = models.IntegerField(null=True, verbose_name='Корреспандентский счет')
    bik = models.IntegerField(null=True, verbose_name='БИК')
    validity_period = models.ForeignKey(BankDetailValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия банковских реквизитов')

    def __str__(self):
        a = str(self.organization.__str__()) + ', Банк ' + str(self.bank_title.__str__()) + '  '+\
            str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Банковские реквизиты организации'
        verbose_name_plural = 'Банковские реквизиты организаций'


class OrganizationAddressValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        if self.end_date:
            a = 'действующие с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'действуют с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия адреса организации'
        verbose_name_plural = 'Периоды действия адресов организаций'


class OrganizationAddress(Address, models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True,
                                     verbose_name='Организация')
    validity_period = models.ForeignKey(OrganizationAddressValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия адреса организации')

    def __str__(self):
        a = str(self.organization.__str__()) + ', адрес: ' + str(super().__str__()) + '  ' +\
            str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес организации'
        verbose_name_plural = 'Адреса организаций'


class ForestryValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        if self.end_date:
            a = 'действующие с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'действуют с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия отдела(лесничества)'
        verbose_name_plural = 'Периоды действия отделов (лесничеств)'


class Forestry(models.Model):
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True,
                                     verbose_name='Организация')
    title = models.CharField(max_length=255, null=True, verbose_name='Нзвание отдела (лесничества)')
    validity_period = models.ForeignKey(ForestryValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия отдела (лесничества) организации')

    def __str__(self):
        a = str(self.organization.__str__()) + ', отдел: ' + str(self.title.__str__()) + ' лесничество ' +\
            str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Отдел (лесничество)'
        verbose_name_plural = 'Отделы (лесничества)'


class DepartmentAddressValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        if self.end_date:
            a = 'действующие с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'действуют с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия адреса отдела(лесничества)'
        verbose_name_plural = 'Периоды действия адресов отделов (лесничеств)'


class DepartmentAddress(Address, models.Model):
    forestry = models.ForeignKey('Forestry', on_delete=models.CASCADE, null=True, verbose_name='Отдел (лесничество)')
    validity_period = models.ForeignKey(DepartmentAddressValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия адреса отдела (лесничества) организации')

    def __str__(self):
        a = str(self.forestry.__str__()) + ' адрес: ' + str(super().__str__()) + '  ' +\
            str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес отдела (лесничества) организации'
        verbose_name_plural = 'Адреса отделов (лесничеств) организаций'


class RepresentativeOfTheDepartmentAtValidityPeriod(ValidityPeriod):
    pass

    def __str__(self):
        if self.end_date:
            a = 'действующие с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'действуют с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия представителя отдела по адресу'
        verbose_name_plural = 'Периоды действия представителей отделов по адресу'


class RepresentativeOfTheDepartmentAt(PersonAbstr, models.Model):
    department_address = models.ForeignKey(DepartmentAddress, on_delete=models.CASCADE, null=True, verbose_name='Адрес отдела')
    validity_period = models.ForeignKey(RepresentativeOfTheDepartmentAtValidityPeriod, on_delete=models.CASCADE, null=True,
                                        verbose_name='Период действия представителя отдела (лесничества) организации')

    def __str__(self):
        a = str(self.second_name.__str__()) + ' ' + str(self.first_name.__str__()) + ' '\
        + str(self.patronymic.__str__()) + ' ' + str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Представитель отдела (лесничества) организации'
        verbose_name_plural = 'Представители отделов (лесничеств) организаций'


class Position(models.Model):
    title = models.TextField(null=True, verbose_name='Название должности')
    representative_of_the_department_at = models.ManyToManyField(RepresentativeOfTheDepartmentAt, blank=True,
                                        verbose_name='Представитель отдела (лесничества)')

    def __str__(self):
        a = str(self.title.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Должность представителя отдела'
        verbose_name_plural = 'Должности педставителей отделов'