from trytond.model import fields
from trytond.pool import PoolMeta


class Level(metaclass=PoolMeta):
    __name__ = 'account.dunning.level'
    wait_automatically = fields.Boolean('Move to Waiting Automatically',
        help='If checked, the dunning will be moved to waiting state when '
        'computed from cron.')
    send_email = fields.Boolean('Send Email', help='If checked, an e-mail will '
        'be sent to the party when the dunning is computed. A trigger must be '
        'created.')

    @staticmethod
    def default_wait_automatically():
        return True


class Dunning(metaclass=PoolMeta):
    __name__ = 'account.dunning'

    @classmethod
    def create_dunning_cron(cls):
        cls.generate_dunnings()
        to_process = []
        for dunning in cls.search([('state', '=', 'draft')]):
            if dunning.level.wait_automatically:
                to_process.append(dunning)
        if to_wait:
            cls.process(to_wait)


class Cron(metaclass=PoolMeta):
    __name__ = 'ir.cron'

    @classmethod
    def __setup__(cls):
        super(Cron, cls).__setup__()
        cls.method.selection.append(
            ('account.dunning|create_dunning_cron',
                "Create dunning"),
            )
