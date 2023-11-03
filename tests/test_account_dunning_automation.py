# This file is part account_dunning_automation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest


from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class AccountDunningAutomationTestCase(ModuleTestCase):
    'Test Account Dunning Automation module'
    module = 'account_dunning_automation'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            AccountDunningAutomationTestCase))
    return suite
