from django.conf.urls import url

from email_notifications import views

urlpatterns = [
    url(r'^email/', views.EmailView.as_view()),

]