from django.contrib import admin

from pyconcz_2016.proposals.admin import ProposalAdmin


class Proposals:
    configs = {}

    def register(self, config):
        self.configs[config.key] = config

        admin.site.register(config.model, ProposalAdmin)

    def get_config(self, key):
        return self.configs[key]


proposals = Proposals()

