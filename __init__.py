# This file is part account_dunning_automation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import dunning

def register():
    Pool.register(
        dunning.Dunning,
        dunning.Cron,
        module='account_dunning_automation', type_='model')
