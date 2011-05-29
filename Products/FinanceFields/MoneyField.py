"""MoneyField is a custom Archetypes Field for the representation of
Money in an archetypes schema.

$Id: MoneyField.py 33 2005-07-04 21:12:23Z roche $
"""
from types import TupleType
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import ReferenceField, ObjectField, DecimalWidget
from Products.Archetypes.Field import STRING_TYPES, decode, encode
from Products.Archetypes.Registry import registerField

from MoneyWidget import MoneyWidget
from Currency import CURRENCIES
from Money import Money, parseString
from fixedpoint import FixedPoint


class MoneyField(ObjectField):
    """A field for storing Money"""
    __implements__ = ObjectField.__implements__

    _properties = ObjectField._properties.copy()
    _properties.update({
        'type': 'Money',
        'widget': MoneyWidget,
        'default_currency_method': '',
        'use_global_currency': False,
        })

    security  = ClassSecurityInfo()

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        """
        Check if value is an actual Money value. If not, attempt
        to convert it to one; otherwise, set to None. Assign all
        properties passed as kwargs to object.

        field.set( Money(10, 'ZAR') )
        field.set( money_instance )

        """
        if value is not None:
            if type(value) in STRING_TYPES:
                cur, value = parseString(decode(value, instance))
                if self.use_global_currency:
                    cur = self.getGlobalCurrency()
                else:
                    if cur is None:
                        cur = self.getDefaultCurrency(instance)
                value = Money(value, cur)

            assert isinstance(value, Money), (
                'value must be Money instance. value == %s' % value)

        ObjectField.set(self, instance, value, **kwargs)

    def getDefaultCurrency(self, instance):
        """
        Retrieves default currency if 'default_currency_method'
        specified.

        XXX: Get the default currency from the locale if no default
        method provided.
        """
        if self.default_currency_method and \
            hasattr(instance, self.default_currency_method):
            method = getattr(instance, self.default_currency_method)
            return method()
        else:
            props_tool = getToolByName(self, 'portal_properties')
            sheet = props_tool.get('financial_properties', {})
            symbol = sheet.getProperty('default_currency', None)
            return CURRENCIES.get(symbol, '')


    security.declarePublic('getGlobalCurrency')
    def getGlobalCurrency(self):
        props_tool = getToolByName(self, 'portal_properties')
        sheet = props_tool.get('financial_properties', {})
        return sheet.getProperty('default_currency', 'USD')


registerField(MoneyField,
              title='Money',
              description=('Used for storing Money'))

