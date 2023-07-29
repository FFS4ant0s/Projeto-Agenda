from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),  # type:ignore
    path('', views.index, name='index'),  # type:ignore

    # contact (CRUD)
    path('<int:contact_id>/', views.contact, name='contact'), # type:ignore
]