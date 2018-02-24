from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from company.models import Company
from store.models import Store



@login_required
def user_home_page(request):

	user_companies = Company.objects.filter(owner=request.user.profile)
	if len(user_companies) == 0:
		return HttpResponseRedirect(reverse_lazy("company:add_company"))

	elif len(user_companies) == 1:
		user_company = Company.objects.get(owner=request.user.profile)
		stores = user_company.stores.all()
		if len(stores) == 1:
			store = Store.objects.get(company=user_company)
			return HttpResponseRedirect(reverse_lazy("store:dashboard", kwargs={"store_slug":store.slug }))
		elif len(stores) > 1:
			return HttpResponseRedirect(reverse_lazy("company:stores_list", kwargs={ "owner_slug": user_company.owner.slug , "company_slug": user_company.slug}))
		elif len(stores) < 1:
			return HttpResponseRedirect(reverse_lazy("company:add_store", kwargs={"company_slug": user_company.slug}))

	elif len(user_companies) > 1:
		return HttpResponseRedirect(reverse_lazy("company:list_companies", kwargs={"owner_slug": request.user.profile.slug }))



	raise Http404
