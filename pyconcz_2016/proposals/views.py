from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import redirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.utils.timezone import now

from pyconcz_2016.proposals.config import proposals


def proposal_create(request, *, key):
    try:
        config = proposals.get_config(key)
    except KeyError:
        raise Http404

    context = RequestContext(request, {'proposal_config': config})

    right_now = now()
    if config.date_start > right_now:
        return TemplateResponse(request, 'proposals/proposal_before.html', context)
    elif config.date_end < right_now:
        return TemplateResponse(request, 'proposals/proposal_after.html', context)

    ProposalForm = modelform_factory(config.model, exclude=['note', 'date'])

    if request.method.lower() == 'post':
        form = ProposalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='cfp_success', key=key)

    else:
        form = ProposalForm()

    context['form'] = form
    return TemplateResponse(request, 'proposals/proposal_form.html', context)


def proposal_success(request, *, key):
    context = RequestContext(request, {'proposal_config_key': key})
    return TemplateResponse(request, 'proposals/proposal_success.html', context)


def proposal_about(request, *, key):
    try:
        config = proposals.get_config(key)
    except KeyError:
        raise Http404

    context = RequestContext(request, {'proposal_config': config})
    return TemplateResponse(request, config.template_about, context)
