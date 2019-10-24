from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from .views import JournalsView, EntriesView, AjaxEntriesView

urlpatterns = [
    path('journals/', JournalsView.as_view()),
    path('journals/<str:journal_title>/', EntriesView.as_view()),
    path('journals/<str:journal_title>/<int:pk>/', AjaxEntriesView.as_view())
]