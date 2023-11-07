from trytond.pool import PoolMeta

class Dunning(metaclass=PoolMeta):
    __name__ = 'account.dunning'

    @classmethod
    def create_dunning_cron(cls):
        cls.generate_dunnings()


class Cron(metaclass=PoolMeta):
    __name__ = 'ir.cron'

    @classmethod
    def __setup__(cls):
        super(Cron, cls).__setup__()
        cls.method.selection.append(
            ('account.dunning|create_dunning_cron',
            "Create dunning"),
            )