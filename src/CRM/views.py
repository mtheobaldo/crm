from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, View
from .models import Report, Stage, Company, Contact, Opportunity, Reminder, CallLog, Campaign
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.


## Call Views ##
class ListCallView(ListView):
	model = CallLog
	paginate_by = 10

class ViewCallView(DetailView):
	model = CallLog

class CreateCallView(CreateView):
	model = CallLog
	fields = ['opportunity', 'note']

	# def form_valid(self, form):
	# 	call = form.save(commit=False)
	# 	call.user = self.request.user
	# 	call.save()
	# 	return super(CreateCallView, self).form_valid(form)

class DeleteCallView(DeleteView):
	model = Company
	#success_url = reverse_lazy('')

####################End######################


## Stage Views ##
class ListStageView(ListView):
	model = Stage
	paginate_by = 10

class ViewStageView(DetailView):
	model = Stage

class CreateStageView(CreateView):
	model = Stage
	fields = ['name, order, description, value']

class UpdateStageView(UpdateView):
	model = Stage
	fields = ['name, order, description, value']

class DeleteStageView(DeleteView):
	model = Stage
	#success_url = reverse_lazy('')

####################End######################


## Company Views ##
class ListCompanyView(ListView):
	model = Company
	paginate_by = 10

class ViewCompanyView(DetailView):
	model = Company

class UpdateCompanyView(UpdateView):
	model = Company
	fields = ['name, website, address1, address2, city, zipcode, country, phone']

class CreateCompanyView(CreateView):
	model = Company
	fields = ['name, website, address1, address2, city, zipcode, country, phone']

class DeleteCompanyView(DeleteView):
	model = Company
	#success_url = reverse_lazy('')

####################End######################


## Contact Views ##
class ListContactView(ListView):
	model = Contact
	paginate_by = 10

class ViewContactView(DetailView):
	model = Contact

class UpdateContactView(UpdateView):
	model = Contact
	fields = ['company ,first_name, last_name, email, address1, address2, city, zipcode, country, phone']

class CreateContactView(CreateView):
	model = Contact
	fields = ['company ,first_name, last_name, email, address1, address2, city, zipcode, country, phone']

class DeleteContactView(DeleteView):
	model = Contact
	#success_url = reverse_lazy('')

####################End######################


## Reminder Views ##
class ListReminderView(ListView):
	model = Reminder
	paginate_by = 10

class ViewReminderView(DetailView):
	model = Reminder

class CreateReminderView(CreateView):
	model = Reminder
	fields = ['opportunity, date, note']

class UpdateReminderView(UpdateView):
	model = Reminder
	fields = ['note, completed']


class DeleteReminderView(DeleteView):
	model = Reminder
	#success_url = reverse_lazy('')

####################End######################


## Campaign Views ##
class ListCampaignView(ListView):
	model = Campaign
	paginate_by = 10

class ViewCampaignView(DetailView):
	model = Campaign

class CreateCampaignView(CreateView):
	model = Campaign
	fields = ['name, description']

class UpdateCampaignView(UpdateView):
	model = Campaign
	fields = ['name, description']


class DeleteCampaignView(DeleteView):
	model = Campaign
	#success_url = reverse_lazy('')

####################End######################


## Opportunity Views ##
class ListOpportunityView(ListView):
	model = Opportunity
	paginate_by = 10

class ViewOpportunityView(DetailView):
	model = Opportunity

class CreateOpportunityView(CreateView):
	model = Opportunity
	fields = ['stage, company, contact, value, source, user, create_date']

class UpdateOpportunityView(UpdateView):
	model = Opportunity
	fields = ['stage, company, contact, value, source, user, create_date']


class DeleteOpportunityView(DeleteView):
	model = Opportunity
	#success_url = reverse_lazy('')

####################End######################


