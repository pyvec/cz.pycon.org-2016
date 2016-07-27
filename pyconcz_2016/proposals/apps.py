from django.apps import AppConfig



class ProposalsConfig(AppConfig):
    name = "pyconcz_2016.proposals"
    verbose_name = "Conference Proposals"

    def ready(self):
        from pyconcz_2016.proposals.config import proposals
        from pyconcz_2016.proposals.pyconcz2016_config import (
            TalksConfig, WorkshopsConfig)
        proposals.register(TalksConfig)
        proposals.register(WorkshopsConfig)
