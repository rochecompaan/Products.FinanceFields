from Products.Archetypes.public import *

class CurrencyField(ObjectField):
    """A field that stores currency"""
    _properties = Field._properties.copy()
    _properties.update({
        'type' : 'currency',
        'default': None,
        })

    def set(self, instance, value, **kwargs):
        """Convert passed-in value to a currency. If failure, set value to
        None."""
        if value=='':
            value=None
        elif value is not None:
            # should really blow if value is not valid
            __traceback_info__ = (self.getName(), instance, value, kwargs)
            value = float(value)

        ObjectField.set(self, instance, value, **kwargs)

