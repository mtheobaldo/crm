from django.conf.urls import include, url
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required
from .models import Report, Stage, Company, Contact, Opportunity, Reminder, CallLog
from django.views.generic import TemplateView

urlpatterns = [
    ###Dashboard###
    url(r'^dashboard/$', login_required(TemplateView.as_view(template_name="CRM/dashboard.html")), name="dashboard"),
    url(r'^search/$', login_required(views.search), name="search"),
    url(r'^reports/$', login_required(views.ReportsView.as_view()), name="reports"),
	###Calls###
    url(r'^call/(?P<pk>\d+)/$', login_required(views.ViewCallView.as_view()), name="callinfo"),
    url(r'call/all/$', login_required(views.ListCallView.as_view()), name="calllist"),
    url(r'call/create/$', login_required(views.CreateCallView.as_view()), name="callcreate"),
    url(r'call/update/(?P<pk>\d+)/$', login_required(views.DeleteCallView.as_view()), name="callupdate"),
    url(r'call/delete/(?P<pk>\d+)/$', login_required(views.DeleteCallView.as_view()), name="calldelete"),
    ###Companies###
    url(r'^company/(?P<pk>\d+)/$', login_required(views.ViewCompanyView.as_view()), name="companyinfo"),
    url(r'company/all/$', login_required(views.ListCompanyView.as_view()), name="companylist"),
    url(r'company/create/$', login_required(views.CreateCompanyView.as_view()), name="companycreate"),
    url(r'company/delete/(?P<pk>\d+)/$', login_required(views.DeleteCompanyView.as_view()), name="companydelete"),
    url(r'company/update/(?P<pk>\d+)/$', login_required(views.UpdateCompanyView.as_view()), name="companyupdate"),
    ###Stage###
    url(r'^stage/(?P<pk>\d+)/$', login_required(views.ViewStageView.as_view()), name="stageinfo"),
    url(r'stage/all/$', login_required(views.ListStageView.as_view()), name="stagelist"),
    url(r'stage/create/$', login_required(views.CreateStageView.as_view()), name="stagecreate"),
    url(r'stage/delete/(?P<pk>\d+)/$', login_required(views.DeleteStageView.as_view()), name="stagedelete"),
    url(r'stage/update/(?P<pk>\d+)/$', login_required(views.UpdateStageView.as_view()), name="stageupdate"),
    ###Contact###
    url(r'^contact/(?P<pk>\d+)/$', login_required(views.ViewContactView.as_view()), name="contactinfo"),
    url(r'contact/all/$', login_required(views.ListContactView.as_view()), name="contactlist"),
    url(r'contact/create/$', login_required(views.CreateContactView.as_view()), name="contactcreate"),
    url(r'contact/delete/(?P<pk>\d+)/$', login_required(views.DeleteContactView.as_view()), name="contactdelete"),
    url(r'contact/update/(?P<pk>\d+)/$', login_required(views.UpdateContactView.as_view()), name="contactupdate"),
    ###Reminder###
    url(r'^reminder/(?P<pk>\d+)/$', login_required(views.ViewReminderView.as_view()), name="reminderinfo"),
    url(r'reminder/all/$', login_required(views.ListReminderView.as_view()), name="reminderlist"),
    url(r'reminder/create/$', login_required(views.CreateReminderView.as_view()), name="remindercreate"),
    url(r'reminder/delete/(?P<pk>\d+)/$', login_required(views.DeleteReminderView.as_view()), name="reminderdelete"),
    url(r'reminder/update/(?P<pk>\d+)/$', login_required(views.UpdateReminderView.as_view()), name="reminderupdate"),
    ###Opportunity###
    url(r'^opportunity/(?P<pk>\d+)/$', login_required(views.ViewOpportunityView.as_view()), name="opportunityinfo"),
    url(r'opportunity/all/$', login_required(views.ListOpportunityView.as_view()), name="opportunitylist"),
    url(r'opportunity/create/$', login_required(views.CreateOpportunityView.as_view()), name="opportunitycreate"),
    url(r'opportunity/delete/(?P<pk>\d+)/$', login_required(views.DeleteOpportunityView.as_view()), name="opportunitydelete"),
    url(r'opportunity/update/(?P<pk>\d+)/$', login_required(views.UpdateOpportunityView.as_view()), name="opportunityupdate"),
    ###Campaigns###
    url(r'^campaign/(?P<pk>\d+)/$', login_required(views.ViewCampaignView.as_view()), name="campaigninfo"),
    url(r'campaign/all/$', login_required(views.ListCampaignView.as_view()), name="campaignlist"),
    url(r'campaign/create/$', login_required(views.CreateCampaignView.as_view()), name="campaigncreate"),
    url(r'campaign/delete/(?P<pk>\d+)/$', login_required(views.DeleteCampaignView.as_view()), name="campaigndelete"),
    url(r'campaign/update/(?P<pk>\d+)/$', login_required(views.UpdateCampaignView.as_view()), name="campaignupdate"),
]

	# ### y ###
 #    url(r'^ x /(?P<pk>\d+)/$', login_required(views.View y View.as_view()), name=" x info"),
 #    url(r' x /all/$', login_required(views.List y View.as_view()), name=" x list"),
 #    url(r' x /create/$', login_required(views.Create y View.as_view()), name=" x create"),
 #    url(r' x /delete/$', login_required(views.Delete y View.as_view()), name=" x delete"),
 #    url(r' x /update/$', login_required(views.Update y View.as_view()), name=" x update"),