from django.apps import AppConfig


class ProposalsConfig(AppConfig):
    name = "pyconcz_2016.proposals"
    verbose_name = "Conference Proposals"

    def ready(self):
        # Register proposal forms
        from pyconcz_2016.proposals.config import proposals
        from pyconcz_2016.proposals.pyconcz2016_config import (
            TalksConfig, WorkshopsConfig)
        proposals.register(TalksConfig)
        proposals.register(WorkshopsConfig)

        # Register signals
        from django.db.models.signals import post_save
        from pyconcz_2016.proposals.models import Talk, Workshop
        from pyconcz_2016.proposals.slack import notify_slack
        post_save.connect(notify_slack, sender=Talk)
        post_save.connect(notify_slack, sender=Workshop)
