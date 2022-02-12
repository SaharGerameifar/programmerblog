from django.urls import path

from .views import contact_page


app_name = 'contactus'
urlpatterns = [
    path('contact_us', contact_page, name="contact"),
]
