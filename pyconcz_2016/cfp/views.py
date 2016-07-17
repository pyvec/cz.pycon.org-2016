from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.utils.timezone import now

from pyconcz_2016.cfp.models import Proposal, Cfp


def proposal_create(request, *, slug):
    cfp = get_object_or_404(Cfp, slug=slug)

    context = RequestContext(request, {'cfp': cfp})

    right_now = now()
    if cfp.date_start > right_now:
        return TemplateResponse(request, 'cfp/proposal_before.html', context)
    elif cfp.date_end < right_now:
        return TemplateResponse(request, 'cfp/proposal_after.html', context)

    ProposalForm = modelform_factory(Proposal, exclude=['cfp', 'date'])

    if request.method.lower() == 'post':
        form = ProposalForm(request.POST)
        form.instance.cfp = cfp

        if form.is_valid():
            form.save()
            return redirect(to='cfp_success', slug=slug)

    else:
        form = ProposalForm()

    context['form'] = form
    return TemplateResponse(request, 'cfp/proposal_form.html', context)


def proposal_success(request, *, slug):
    context = RequestContext(request, {'cfp_slug': slug})
    return TemplateResponse(request, 'cfp/proposal_success.html', context)
