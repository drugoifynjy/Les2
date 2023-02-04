from django.db import models
from .abstract_models import *


class FormOfTheCabin(models.Model):
    form_of_the_cabin = models.TextField(null=True, blank=True, verbose_name='Форма рубки',)

    def __str__(self):
        a = str(self.form_of_the_cabin.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Форма рубки'
        verbose_name_plural = 'Формы рубки'


class TypeOfCabin(models.Model):
    type_of_cabin = models.TextField(null=True, blank=True, verbose_name='Вид рубки')

    def __str__(self):
        a = str(self.type_of_cabin.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Вид рубки'
        verbose_name_plural = 'Виды рубки'


class TreeSpecies(models.Model):
    tree_species = models.CharField(max_length=255, null=True, verbose_name='Порода дерева')

    def __str__(self):
        a = str(self.tree_species.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Порода дерева'
        verbose_name_plural = 'Породы деревьев'


class OrganizationValidityPeriod(ValidityPeriod):

    def __str__(self):
        a = 'Период действия организации ' + str(self.start_date.__str__()) + ' ' + str(self.end_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия организации'
        verbose_name_plural = 'Периоды действия организаций'


class Organization(models.Model):
    title = models.CharField(max_length=255, null=True, verbose_name='Название')
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

    def __str__(self):
        a = 'Период действия реквизитов организации ' + str(self.start_date.__str__()) + ' ' + \
            str(self.end_date.__str__())

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


class OrganizationAddress(Address):
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
    number = models.SmallIntegerField(verbose_name='Номер отдела', null=True)
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


class DepartmentAddress(Address):
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


class RepresentativeOfTheDepartmentAt(PersonAbstr):
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


class PowerOfAttorneyOfTheRepresentativeValidityPeriod(ValidityPeriod):

    def __str__(self):
        if self.end_date:
            a = 'Доверенность действует с ' + str(self.start_date.__str__()) + ' по ' + (self.end_date.__str__())
        else:
            a = 'Доверенность действует с ' + str(self.start_date.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Период действия доверенности представителя отдела по адресу'
        verbose_name_plural = 'Периоды действия доверенностей представителей отделов по адресу'


class PowerOfAttorneyOfTheRepresentative(models.Model):
    representative_of_the_department_at = models.ForeignKey(RepresentativeOfTheDepartmentAt, on_delete=models.CASCADE, blank=True,
                                                                 verbose_name='Представитель отдела (лесничества)')
    validity_period = models.ForeignKey(PowerOfAttorneyOfTheRepresentativeValidityPeriod, on_delete=models.CASCADE,
                                        null=True,
                                        verbose_name='Период действия доверенности представителя отдела (лесничества)')

    def __str__(self):
        a = str(self.representative_of_the_department_at.__str__()) + ' ' + str(self.validity_period.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Доверенность представителя отдела'
        verbose_name_plural = 'Доверенности педставителей отделов'


class DistrictForestry(models.Model):
    department_address = models.ForeignKey(DepartmentAddress, on_delete=models.CASCADE, null=True,
                                           verbose_name='Отдел (адрес отдела)')
    title = models.TextField(null=True, verbose_name='Название')

    def __str__(self):
        a = str(self.title.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Участковое лесничество'
        verbose_name_plural = 'Участковые лесничества'


class Tract(models.Model):
    district_forestry = models.ForeignKey(DistrictForestry, on_delete=models.CASCADE, null=True,
                                           verbose_name='Участковое лесничество')
    title = models.TextField(null=True, verbose_name='Название')

    def __str__(self):
        a = str(self.title.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Урочище'
        verbose_name_plural = 'Урочища'


class Quarter(models.Model):
    tract = models.ForeignKey(Tract, on_delete=models.CASCADE, null=True, verbose_name='Урочище')
    number = models.SmallIntegerField(null=True, verbose_name='Номер квартала')

    def __str__(self):
        a = 'квартал №' + str(self.number.__str__())

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Квартал'
        verbose_name_plural = 'Квартала'


class Plot(models.Model):
    quarter = models.ForeignKey(Quarter, on_delete=models.CASCADE, null=True,
                                           verbose_name='Квартал')
    number = models.TextField(null=True, verbose_name='Номер делянки')
    area = models.FloatField(null=True, verbose_name='Площадь')
    form_of_the_cabin = models.ForeignKey(FormOfTheCabin, on_delete=models.SET_NULL, null=True, verbose_name='форма рубки')
    type_of_cabin = models.ForeignKey(TypeOfCabin, on_delete=models.SET_NULL, null=True, verbose_name='Вид рубки')
    section = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Выдел')
    type_of_forestry = models.CharField(blank=True, null=True, max_length=100, verbose_name='Хозяйство',
                                        default='мягколиственное')
    business = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Деловая')
    firewood = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Дровяная')
    brushwood = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Хворост(неликвид)')
    total = models.PositiveIntegerField(blank=True, null=True, default=0, verbose_name='Всего')
    cost = models.FloatField(blank=True, null=True, default=0, verbose_name='Стоимость')
    cost_in_words = models.CharField(blank=True, null=True, max_length=500, default='ноль руб. 00 коп.',
                                     verbose_name='Стоимость прописью')

    def __str__(self):
        a = 'Деляна №' + ' ' + str(self.number.__str__()) + ' ' + \
            str(self.quarter.tract.district_forestry.title.__str__()) +\
             ' участковое лесничество, урочище ' + str(self.quarter.tract.__str__() + ' ' + str(self.quarter.__str__()))

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Делянка'
        verbose_name_plural = 'Делянки'


class PlotWoodSpecies(models.Model):
    """Количество-качество по породе в делянке"""
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, null=True, verbose_name='Делянка')
    name = models.ForeignKey(TreeSpecies, on_delete=models.SET_NULL, null=True, verbose_name='Порода')
    number_of_trees = models.IntegerField(blank=True, null=True, default=0, verbose_name='Количество деревьев')
    large = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Крупная')
    average = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Средняя')
    small = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Мелкая')
    firewood = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Дровяная')
    brushwood = models.PositiveSmallIntegerField(blank=True, null=True, default=0, verbose_name='Хворост(неликвид)')
    price = models.FloatField(blank=True, null=True, default=0, verbose_name='Цена')

    def __str__(self):
        a = str(self.plot.__str__()) + ' ' + str(self.name.tree_species)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Данные по породе в делянке'
        verbose_name_plural = 'Данные по породам в делянках'


class HeatedPremise(Address, models.Model):
    """Отапливаемое помещение"""
    cadastral_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Кадастровый номер')

    def __str__(self):
        if self.apartment_number:
            a = str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__()) + ' кв. ' + \
                str(self.apartment_number.__str__())
        else:
            a = str(self.locality.__str__()) + ' ул. ' + \
                str(self.street.__str__()) + ' д. ' + \
                str(self.house_number.__str__())
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес отапливаемого помещения'
        verbose_name_plural = 'Адреса отапливаемых помещений'


class PersonResidenceAddress(Address):

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес проживания заявителя'
        verbose_name_plural = 'Адреса проживания заявителей'


class RepresentativeResidenceAddress(Address):

    class Meta:
        ordering = ['id']
        verbose_name = 'Адрес проживания представителя заявителя'
        verbose_name_plural = 'Адреса проживания представителей заявителей'


class PersonPassport(Passport):
    class Meta:
        ordering = ['id']
        verbose_name = 'Паспортные данные заявителя'
        verbose_name_plural = 'Паспортные данные заявителей'


class RepresentativePassport(Passport):
    class Meta:
        ordering = ['id']
        verbose_name = 'Паспортные данные представителя заявителя'
        verbose_name_plural = 'Паспортные данные представителей заявителей'


class Person(PersonAbstr):
    residence_address = models.OneToOneField(PersonResidenceAddress, on_delete=models.CASCADE,
                                             blank=True, null=True, verbose_name='Адрес проживания')
    passport = models.OneToOneField(PersonPassport, on_delete=models.CASCADE,
                                    blank=True, null=True, verbose_name='паспортные данные')
    there_is_a_representative = models.BooleanField(verbose_name='есть представитель', default=False)

    def __str__(self):
        a = str(self.second_name)+' '+str(self.first_name)+' '+str(self.patronymic) + " - заявитель"
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'ФИО заявителя'
        verbose_name_plural = 'ФИО заявтиелей'


class RepresentativePerson(PersonAbstr):
    """Представитель заявителя по доверенности"""
    residence_address = models.OneToOneField(RepresentativeResidenceAddress, on_delete=models.CASCADE,
                                               blank=True, null=True, verbose_name='Адрес регистрации')
    passport = models.OneToOneField(RepresentativePassport, on_delete=models.CASCADE,
                                      blank=True, null=True, verbose_name='паспортные данные')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='Заявитель')

    def __str__(self):
        a = str(self.second_name)+' '+str(self.first_name)+' '+str(self.patronymic) + " - представитель заявителя" +\
            self.person.__str__()

        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'ФИО представителя заявтиля'
        verbose_name_plural = 'ФИО представителей заявителей'


class Statement(models.Model):
    """Заявление"""

    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Заявитель')
    number_statement = models.PositiveSmallIntegerField(verbose_name='Номер заявления')
    date = models.DateField(blank=True, null=True, verbose_name='Дата заявления')
    heated_promise = models.OneToOneField(HeatedPremise, on_delete=models.SET_NULL, blank=True,
                                          null=True, verbose_name='Адрес отапливаемого помещения')
    quantity = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество по заявлению')

    def __str__(self):
        num = str(self.number_statement)
        data = str(self.date)
        a = str('№  ' + num + ' от ' + data)
        return a

    class Meta:
        ordering = ['id']
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'


class Contract(models.Model):
    """Договор"""
    statement = models.OneToOneField(Statement, on_delete=models.CASCADE, verbose_name='Заявление')
    number_decree = models.CharField(max_length=7, verbose_name='номер распоряжения')
    date_decree = models.DateField(blank=True, null=True, verbose_name='дата распоряжения')
    number = models.CharField(max_length=7, blank=True, null=True, verbose_name='номер договора')
    date = models.DateField(blank=True, null=True, verbose_name='Дата договора')
    the_end_date_of_the_export_of_wood = models.DateField(blank=True, null=True,
                                                          verbose_name='Дата окончания вывоза древесины')
    end_date_of_wood_harvesting = models.DateField(blank=True, null=True, verbose_name='Дата окончания заготовки')
    plot = models.OneToOneField(Plot, on_delete=models.CASCADE, verbose_name='Делянка')

    def __str__(self):
        b = 'Договор № ' + str(self.number)
        return b

    class Meta:
        ordering = ['id']
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


