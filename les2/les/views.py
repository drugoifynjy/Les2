from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models.functions import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View


from .forms import *
from .models import *


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login/login.html'
    success_url = reverse_lazy('main_menu')


def logout_user(request):
    logout(request)
    return redirect('login')


class MainMenu(View):
    template_name = 'les/main_menu.html'

    def get(self, request, *args, **kwargs):

        form = {
                'title': 'арм лес'}
        return render(request, self.template_name, context=form)


class OrganizationsView(ListView):
    model = Organization
    template_name = 'organizations/organizations_list.html'
    context_object_name = 'organizations'
    paginate_by = 10
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = 'Организации'
        return context


class OrganizationAdd(CreateView):
    template_name = 'organizations/organization_add.html'

    def get(self, request, *args, **kwargs):
        form_add_organization = AddOrganization()
        form = {'form_add_organization': form_add_organization,
                'title': 'Добавить заявителя'}
        return render(request, self.template_name, context=form)

    def post(self, request, *args, **kwargs):
        form_add_organization = AddOrganization(request.POST)

        form = {'form_add_organization': form_add_organization,
                'title': 'Добавить организацию'}
        if form_add_organization.is_valid():
            form_add_organization.save()
            return redirect('organizations_list')
        return render(request, self.template_name, context=form)


class OrganizationMod(View):
    pass


class Sobnushdi(View):
    template_name = 'sobnushdi/sobnushdi.html'

    def get(self, request, *args, **kwargs):

        form = {
                'title': 'Собственные нужды'}
        return render(request, self.template_name, context=form)


class PersonView(ListView):
    model = Person
    template_name = 'sobnushdi/person/persons_list.html'
    context_object_name = 'pers'
    paginate_by = 10
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        for person in self.object_list:
            if person.date_of_bird:
                person.date_of_bird = person.date_of_bird.strftime("%d.%m.%Y")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявители'
        return context


class PersonAdd(CreateView):
    template_name = 'sobnushdi/person/person_add.html'

    def get(self, request, *args, **kwargs):
        form_add_person = AddPerson()
        form_add_passport = AddPersonPassport()
        form_add_residence_address = AddPersonResidenceAddress()
        form_add_person_representative = AddRepresentativePerson()
        form_add_passport_representative = AddRepresentativePassport()
        form_add_residence_address_representative = AddRepresentativeResidenceAddress()
        form = {'form_add_person': form_add_person,
                'form_add_passport': form_add_passport,
                'form_add_residence_address': form_add_residence_address,
                'form_add_person_representative': form_add_person_representative,
                'form_add_passport_representative': form_add_passport_representative,
                'form_add_residence_address_representative': form_add_residence_address_representative,
                'title': 'Добавить заявителя'}
        return render(request, self.template_name, context=form)

    def post(self, request, *args, **kwargs):
        form_add_person = AddPerson(request.POST)
        form_add_passport = AddPersonPassport(request.POST)
        form_add_residence_address = AddPersonResidenceAddress(request.POST)
        form_add_person_representative = AddRepresentativePerson(request.POST)
        form_add_passport_representative = AddRepresentativePassport(request.POST)
        form_add_residence_address_representative = AddRepresentativeResidenceAddress(request.POST)
        form = {'form_add_person': form_add_person,
                'form_add_person_passport': form_add_passport,
                'form_add_person_residence_address': form_add_residence_address,
                'form_add_representative': form_add_person_representative,
                'form_add_representative_passport': form_add_passport_representative,
                'form_add_representative_residence_address': form_add_residence_address_representative,
                'title': 'Добавить заявителя'}
        if form_add_person.is_valid() and form_add_passport.is_valid() and form_add_residence_address.is_valid():
            passport = form_add_passport.save()
            adr = form_add_residence_address.save()
            pers = form_add_person.save(commit=False)
            pers.passport = passport
            pers.residence_address = adr
            pers.save()
            if form_add_person.cleaned_data.get('there_is_a_representative'):
                if form_add_person_representative.is_valid() and form_add_passport_representative.is_valid()\
                        and form_add_residence_address_representative.is_valid():
                    adr_representative = form_add_residence_address_representative.save()
                    passp_representative = form_add_passport_representative.save()
                    pers_representative = form_add_person_representative.save(commit=False)
                    pers_representative.residence_address = adr_representative
                    pers_representative.passport = passp_representative
                    pers_representative.person = pers
                    pers_representative.save()
            return redirect('persons_list')
        return render(request, self.template_name, context=form)


class PersonMod(View):
    template_name = 'sobnushdi/person/person_mod.html'

    def get(self, request, pk, *args, **kwargs):
        pers = get_object_or_404(Person, pk=pk)
        date_of_bird = str(pers.date_of_bird)
        date_of_issue = str(pers.passport.date_of_issue)
        form_mod_person = AddPerson(initial={'date_of_bird': date_of_bird}, instance=pers)
        form_mod_passport = AddPersonPassport(initial={'date_of_issue': date_of_issue}, instance=pers.passport)
        form_mod_residence_address = AddPersonResidenceAddress(instance=pers.residence_address)
        form_mod_person_representative = AddRepresentativePerson()
        form_mod_passport_representative = AddRepresentativePassport()
        form_mod_residence_address_representative = AddRepresentativeResidenceAddress()
        if pers.there_is_a_representative:
            pers_representative = get_object_or_404(RepresentativePerson, person__pk=pk)
            form_mod_person_representative = AddRepresentativePerson(instance=pers_representative)
            form_mod_passport_representative = AddRepresentativePassport(instance=pers_representative.passport)
            form_mod_residence_address_representative = AddRepresentativeResidenceAddress(
                                                                instance=pers_representative.residence_address)
        form = {'form_mod_person': form_mod_person,
                'form_mod_passport': form_mod_passport,
                'form_mod_residence_address': form_mod_residence_address,
                'form_mod_person_representative': form_mod_person_representative,
                'form_mod_representative_passport': form_mod_passport_representative,
                'form_mod_representative_residence_address': form_mod_residence_address_representative,
                'pk': pk,
                'title': 'Изменить данные заявителя'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        pers = get_object_or_404(Person, pk=pk)
        pers_passport = pers.passport
        pers_address = pers.residence_address
        form_mod_person = AddPerson(request.POST, instance=pers)
        form_mod_passport = AddPersonPassport(request.POST, instance=pers_passport)
        form_mod_residence_address = AddPersonResidenceAddress(request.POST, instance=pers_address)
        form_mod_person_representative = AddRepresentativePerson(request.POST)
        form_mod_passport_representative = AddRepresentativePassport(request.POST)
        form_mod_residence_address_representative = AddRepresentativeResidenceAddress(request.POST)
        if pers.there_is_a_representative:
            pers_representative = get_object_or_404(RepresentativePerson, person__pk=pk)
            pers_representative_passport = pers_representative.passport
            pers_representative_address = pers_representative.residence_address
            form_mod_person_representative = AddRepresentativePerson(request.POST, instance=pers_representative)
            form_mod_passport_representative = AddRepresentativePassport(request.POST,
                                                                         instance=pers_representative_passport)
            form_mod_residence_address_representative = AddRepresentativeResidenceAddress(request.POST,
                                                                                          instance=pers_representative_address)
        form = {'form_mod_person': form_mod_person,
                'form_mod_passport': form_mod_passport,
                'form_mod_residence_address': form_mod_residence_address,
                'form_mod_person_representative': form_mod_person_representative,
                'form_mod_representative_passport': form_mod_passport_representative,
                'form_mod_representative_residence_address': form_mod_residence_address_representative,
                'pk': pk,
                'title': 'Изменить данные заявителя'}
        if form_mod_person.is_valid() and form_mod_passport.is_valid() and form_mod_residence_address.is_valid():
            if form_mod_person_representative.is_valid() and form_mod_passport_representative.is_valid() \
                    and form_mod_residence_address_representative.is_valid():
                print(pers.there_is_a_representative)

                if form_mod_person.cleaned_data.get('there_is_a_representative'):
                    adr_representative = form_mod_residence_address_representative.save()
                    passp_representative = form_mod_passport_representative.save()
                    pers_representative = form_mod_person_representative.save(commit=False)
                    pers_representative.residence_address = adr_representative
                    pers_representative.passport = passp_representative
                    pers_representative.person = pers
                    pers_representative.save()
                elif pers.there_is_a_representative:
                    if pers_representative:
                        pers_representative_passport.save()
                        pers_representative_address.save()
                        pers_representative.save()
                elif not form_mod_person.cleaned_data.get('there_is_a_representative'):
                    if pers_representative:
                        pers_representative_passport.delete()
                        pers_representative_address.delete()
                        pers_representative.delete()
            pers_passport.save()
            pers_address.save()
            pers.save()
            return redirect('persons_list')

        return render(request, self.template_name, context=form)


class StatementsView(ListView):
    model = Statement
    template_name = 'sobnushdi/statements/statements_list.html'
    context_object_name = 'statements'
    paginate_by = 10
    ordering = '-pk'

    # persons = Person.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        for statement in self.object_list:
            statement.date = statement.date.strftime("%d.%m.%Y")
        context = super().get_context_data(**kwargs)
        context['title'] = 'Заявления'
        return context


class StatementAdd(CreateView):
    template_name = 'sobnushdi/statements/statement_add.html'

    def get(self, request, pk, *args, **kwargs):
        today = str(datetime.now())[0:10]  # Текущая дата без времени для вставки в форму ввода даты заявления
        form_add_statement = AddStatement(initial={'date': today})
        person = Person.objects.get(pk=pk)
        form_add_heated_promise = AddHeatedPromise(instance=person.residence_address)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'pk': pk,
                'person': person,
                'title': 'Добавить заявление'}

        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        form_add_statement = AddStatement(request.POST)
        form_add_heated_promise = AddHeatedPromise(request.POST)
        person = Person.objects.get(pk=pk)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() \
                and form_add_heated_promise.is_valid():
            heated_promise = form_add_heated_promise.save()
            statement = form_add_statement.save(commit=False)
            statement.organization = Organization.objects.get(selected=True)
            person.save()
            statement.heated_promise = heated_promise
            statement.person = person
            statement.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)


class StatementMod(View):
    template_name = 'sobnushdi/statements/statement_mod.html'

    def get(self, request, pk, *args, **kwargs):
        stat = Statement.objects.get(pk=pk)
        date = str(stat.date)
        form_add_statement = AddStatement(initial={'date': date}, instance=stat)
        form_add_heated_promise = AddHeatedPromise(instance=stat.heated_promise)
        person = stat.person
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'pk': pk,
                'title': 'Добавить заявление'}
        return render(request, self.template_name, context=form)

    def post(self, request, pk, *args, **kwargs):
        stat = Statement.objects.get(pk=pk)
        person = stat.person
        heated_promise = stat.heated_promise
        form_add_statement = ModStatement(request.POST, instance=stat)
        form_add_heated_promise = AddHeatedPromise(request.POST, instance=stat.heated_promise)
        form = {'form_add_statement': form_add_statement,
                'form_add_heated_promise': form_add_heated_promise,
                'person': person,
                'pk': pk,
                'title': 'Добавить заявление'}
        if form_add_statement.is_valid() and form_add_heated_promise.is_valid():
            stat.organization = Organization.objects.get(selected=True)
            heated_promise.save()
            person.save()
            stat.save()
            return redirect('statements_list')
        else:
            form_p = form
        return render(request, self.template_name, context=form_p)