from unittest import TestCase
from Products.FinanceFields.Money import parseString
from Products.FinanceFields.Money import parseString
from Products.FinanceFields.fixedpoint import FixedPoint
from Products.FinanceFields.Currency import CURRENCIES

class TestMoney(TestCase):

    def test_parseString(self):
        s = '1000.00'
        self.assertEqual(parseString(s),
            (None, FixedPoint('1000.00')))

        s = 'R 1000.00'
        self.assertEqual(parseString(s),
            (CURRENCIES['ZAR'], FixedPoint('1000.00')))

        s = '(R 1000.00)'
        self.assertEqual(parseString(s),
            (CURRENCIES['ZAR'], FixedPoint('-1000.00')))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMoney))
    return suite
