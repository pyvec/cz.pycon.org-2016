from django.contrib import admin

from pyconcz_2016.proposals.admin import EntryAdmin


class Proposals:
    configs = {}

    def register(self, config):
        self.configs[config.key] = config

        admin.site.register(
            config.model,
            getattr(config, 'admin', EntryAdmin)
        )

    def get_config(self, key):
        return self.configs[key]


proposals = Proposals()

