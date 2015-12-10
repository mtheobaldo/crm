from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Count
import datetime
from itertools import chain
from django.conf import settings

from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage
# Create your views here.

#the search query
def search(request):
    if request.method == 'GET':
        if request.GET.get('q'):
            contact_results = []
            opp_results =  []
            note_results = []
            search_words = "%s" % (request.GET.get('q'))
            search_word_list = search_words.split(' ')
            for search_word in search_word_list:
                print search_word
                contact_firstname = Contact.objects.filter(first_name__icontains = search_word)
                contact_lastname = Contact.objects.filter(last_name__icontains = search_word)
                contact_company = Contact.objects.filter(company__name__icontains = search_word)
                opp_firstname = Opportunity.objects.filter(contact__first_name__icontains = search_word)
                opp_lastname = Opportunity.objects.filter(contact__last_name__icontains = search_word)
                opp_stage = Opportunity.objects.filter(stage__name__icontains = search_word)
                contact_results = contact_results + list(contact_firstname) + list(contact_lastname) + list(contact_company)
                opp_results = opp_results + list(opp_firstname) + list(opp_lastname) + list(opp_stage)
                call_note = CallLog.objects.filter(note__icontains = search_word)
                reminder_note = Reminder.objects.filter(note__icontains = search_word)
                note_results = note_results + list(call_note) + list(reminder_note)

        return render_to_response('crm/search_results.html', {'search':search_words, 'contacts': contact_results, 'opps': opp_results, 'notes': note_results}, context_instance=RequestContext(request))

    return render_to_response('crm/search_results.html', context_instance=RequestContext(request))

class Dashboard(ListView):
    model = Opportunity
    template_name = "crm/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        #Adding OpportunityStages to the templates' context
        context["opportunity_stages"] = OpportunityStage.objects.all().order_by('-time_stamp')
        context["reminders"] = Reminder.objects.all().order_by('-date')[:5]
        context["stage_by_opp"] = Stage.objects.annotate(opp_count = Count('opportunity'))
	context['opportunity_list'] = Opportunity.objects.all().order_by('-create_date')[:5]

        return context



## Call Views ##
class ListCallView(ListView):
	model = CallLog
	paginate_by = 10

class ViewCallView(DetailView):
	model = CallLog

class CreateCallView(CreateView):
	model = CallLog
	fields = ['opportunity', 'note']
	def get_success_url(self):
		return reverse('crm:dashboard')

	def form_valid(self, form):
		call = form.save(commit=False)
		call.user = self.request.user
		call.save()
		return super(CreateCallView, self).form_valid(form)

class DeleteCallView(DeleteView):
	model = CallLog
	def get_success_url(self):
		return reverse('crm:dashboard')

####################End######################


## Stage Views ##
class ListStageView(ListView):
	model = Stage
	paginate_by = 10

class ViewStageView(DetailView):
	model = Stage

class CreateStageView(CreateView):
	model = Stage
	fields = ['name', 'order', 'description', 'value']
	def get_success_url(self):
		return reverse('crm:dashboard')

class UpdateStageView(UpdateView):
	model = Stage
	fields = ['name', 'order', 'description', 'value']
	def get_success_url(self):
		return reverse('crm:dashboard')

class DeleteStageView(DeleteView):
	model = Stage
	def get_success_url(self):
		return reverse('crm:dashboard')

####################End######################


## Company Views ##
class ListCompanyView(ListView):
	model = Company
	paginate_by = 10

class ViewCompanyView(DetailView):
	model = Company

class UpdateCompanyView(UpdateView):
	model = Company
	fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
	def get_success_url(self):
		return reverse('crm:dashboard')

class CreateCompanyView(CreateView):
	model = Company
	fields = ['name', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
	def get_success_url(self):
		return reverse('crm:dashboard')

class DeleteCompanyView(DeleteView):
	model = Company
	def get_success_url(self):
		return reverse('crm:dashboard')

####################End######################


## Contact Views ##
class ListContactView(ListView):
	model = Contact
	paginate_by = 10

class ViewContactView(DetailView):
	model = Contact

class UpdateContactView(UpdateView):
	model = Contact
	fields = ['company', 'first_name', 'last_name', 'email', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
	def get_success_url(self):
		return reverse('crm:dashboard')

class CreateContactView(CreateView):
	model = Contact
	fields = ['company', 'first_name', 'last_name', 'email', 'address1', 'address2', 'city', 'state', 'zipcode', 'country', 'phone']
	def get_success_url(self):
		return reverse('crm:dashboard')

class DeleteContactView(DeleteView):
	model = Contact
	def get_success_url(self):
		return reverse('crm:dashboard')
####################End######################


## Reminder Views ##
class ListReminderView(ListView):
	model = Reminder
	paginate_by = 10

class ViewReminderView(DetailView):
	model = Reminder

class CreateReminderView(CreateView):
	model = Reminder
	fields = ['opportunity', 'date', 'note']
	def get_success_url(self):
		return reverse('crm:dashboard')

class UpdateReminderView(UpdateView):
	model = Reminder
	fields = ['note', 'completed']
	def get_success_url(self):
		return reverse('crm:dashboard')


class DeleteReminderView(DeleteView):
	model = Reminder
	def get_success_url(self):
		return reverse('crm:dashboard')

####################End######################


## Campaign Views ##
class ListCampaignView(ListView):
	model = Campaign
	paginate_by = 10

class ViewCampaignView(DetailView):
	model = Campaign

class CreateCampaignView(CreateView):
	model = Campaign
	fields = ['name', 'description']
	def get_success_url(self):
		return reverse('crm:dashboard')

class UpdateCampaignView(UpdateView):
	model = Campaign
	fields = ['name', 'description']
	def get_success_url(self):
		return reverse('crm:dashboard')


class DeleteCampaignView(DeleteView):
	model = Campaign
	def get_success_url(self):
		return reverse('crm:dashboard')

####################End######################


## Opportunity Views ##
class ListOpportunityView(ListView):
	model = Opportunity
	paginate_by = 10

class ViewOpportunityView(DetailView):
	model = Opportunity

class CreateOpportunityView(CreateView):
	model = Opportunity
	fields = ['stage', 'company', 'contact', 'value', 'source', 'user']
	def get_success_url(self):
		return reverse('crm:dashboard')

class UpdateOpportunityView(UpdateView):
	model = Opportunity
	fields = ['stage', 'company', 'contact', 'value', 'source', 'user']
	def get_success_url(self):
		return reverse('crm:dashboard')

	def form_valid(form, self):
		opp = form.save(commit= false)
		if opp.stage.value != self.get_object().stage.value:

			o = OpportunityStage()
			o.opportunity = self.get_object()
			o.user = self.request.user
			o.save()
		return super(UpdateOpportunityView, self).form_valid(form)


class DeleteOpportunityView(DeleteView):
	model = Opportunity
	def get_success_url(self):
		return reverse('crm:dashboard')

##########################################

##OpportunityStage View##
class CreateOpportunityStageView(CreateView):
	model = OpportunityStage
	fields = ['opportunity','stage']
	def get_success_url(self):
		return reverse('crm:dashboard')

	def form_valid(form, self):
		opstage = form.save(commit=False)
		opstage.user = User.objects.get(user=self.request.user)
		opstage.opportunity.stage = opstage.stage
		opstage.save()
		return super(CreateOpportunityStageView, self).form_valid(form)



class ReportsView(ListView):
	model = Report

