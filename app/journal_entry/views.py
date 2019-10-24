import django
from django.shortcuts import render_to_response, render, redirect
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
import datetime


from .models import Journal, Entry
from .forms import CreateJournalForm, CreateEntryForm

class JournalsView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'login_required'

    def get(self, request):
        journals = Journal.objects.filter(owner=request.user)
        return render(request, 'journals.html', {
            'journals': journals,
            'form': CreateJournalForm})

    def post(self, request):
        data = request.POST.copy()
        data['owner'] = request.user.pk

        form = CreateJournalForm(data=data)
        journals = Journal.objects.filter(owner=request.user)

        if form.is_valid():
            # check first if name is already taken by another journal of the user
            try:
                journals.get(name=form.cleaned_data['name'])
                return JsonResponse({'error': 'Journal already exists!'})
            except ObjectDoesNotExist:
                form.save()
                return JsonResponse({'success': 'journal created'})

        return render(request, 'journals.html', {
            'journals': journals,
            'form': form})

class EntriesView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'login_required'

    def get(self, request, *args, **kwargs):
        # acquire first the journal specified using the part 
        # of the url that has <str:journal_title>
        journal = Journal.objects.get(name=kwargs['journal_title'])
        entries = Entry.objects.filter(journal=journal)
        
        # TODO: acquire last plan_tom entry and display it in plan_today

        return render(request, 'entry.html', {
            'entries': entries, 
            'journal': journal,
            'form': CreateEntryForm})
            
    def post(self, request, *args, **kwargs):   
        # copy the POST body as direct modification of the POST is prohibited
        data = request.POST.copy()
        # add current journal to specify what journal does this entry belong
        journal = Journal.objects.get(name=kwargs['journal_title'])
        entries = Entry.objects.filter(journal=journal)

        data['journal'] = journal.pk
        try:
            entry = entries.get(date_created=datetime.date.today())
            form = CreateEntryForm(data=data, instance=entry)
        
        except ObjectDoesNotExist:
            form = CreateEntryForm(data=data)

        if form.is_valid():
                
            form.save()
            return render(request, 'entry.html', {
                'entries': entries, 
                'journal': journal,
                'form': CreateEntryForm})

        return JsonResponse({'errors': form.errors}, status=400)
            
    def delete(self, request, *args, **kwargs):
        journal = Journal.objects.get(name=kwargs['journal_title'])
        journal.delete()

        return JsonResponse(
            {
                'delete': 'success'
            },
            status=200
        )

class AjaxEntriesView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'login_required'

    def get(self, request, *args, **kwargs):
        journal = Journal.objects.get(name=kwargs['journal_title'])
        entry = Entry.objects.filter(journal=journal).get(pk=kwargs['pk'])

        return JsonResponse(model_to_dict(entry))