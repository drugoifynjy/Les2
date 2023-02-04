from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('', MainMenu.as_view(), name='main_menu'),
    path('sobnushdi/', Sobnushdi.as_view(), name='sobnushdi'),
    path('sobnushdi/persons_list/', PersonView.as_view(), name='persons_list'),
    path('sobnushdi/person_add/', PersonAdd.as_view(), name='person_add'),
    path('sobnushdi/person_mod/<int:pk>/edit', PersonMod.as_view(), name='person_mod'),

    path('statements_list/', StatementsView.as_view(), name='statements_list'),
    path('statements/statement_add/<int:pk>', StatementAdd.as_view(), name='statement_add'),
    path('statements/statement_mod/<int:pk>', StatementMod.as_view(), name='statement_mod'),

    path('organizations/', OrganizationsView.as_view(), name='organizations_list'),
    path('organizations/organization_add/', OrganizationAdd.as_view(), name='organization_add'),
    path('organizations/organization_mod/<int:pk>', OrganizationMod.as_view(), name='organization_mod'),

]
