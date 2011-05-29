"""FixedPointField is an archetypes field that can be used to represent
fixed point values.

$Id: CustomFields.py 33 2005-07-04 21:12:23Z roche $
"""
from types import TupleType
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.public import ObjectField, DecimalWidget
from Products.Archetypes.Registry import registerField

from MoneyWidget import MoneyWidget
from Currency import CURRENCIES
from Money import Money, parseString
from fixedpoint import FixedPoint


class FixedPointField(ObjectField):
    """A field for storing fixed point values"""
    __implements__ = ObjectField.__implements__

    _properties = ObjectField._properties.copy()
    _properties.update({
        'type' : 'FixedPoint',
        'widget' : DecimalWidget,
        'validators' : ('isDecimal'),
        })

    security  = ClassSecurityInfo()

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        """
        Check if value is an actual FixedPoint value. If not, attempt to
        convert it to one; Raise an error if value is a float. Assign
        all properties passed as kwargs to object.

        field.set( FixedPoint(10))
        field.set( FixedPointInstance)

        """
        assert type(value) != type(0.00)

        if not value is None and not isinstance(value, FixedPoint):
            value = FixedPoint(value)

        ObjectField.set(self, instance, value, **kwargs)


registerField(FixedPointField,
              title='FixedPoint',
              description=('Used for storing FixedPoint'))

