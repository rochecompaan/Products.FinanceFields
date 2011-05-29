from types import StringType
from Products.Archetypes.Widget import ReferenceWidget, TypesWidget
from Products.Archetypes.Registry import registerWidget
from Money import Money

class MoneyWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "money",
        'size' : '8',
        'maxlength' : '255',
        })

    def process_value(self, value, instance, field, form):
        """ Value should be a Money instance in all cases except when
            there was an error on post. When an error occurs, try to
            construct a Money instance from the request.
        """
        if isinstance(value, Money):
            return value
        elif form.has_key(field.getName()):
            value, empty = self.process_form(instance, field, form)
            return value

    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False):
        """ handle money input """
        name = field.getName()
        amount = form.get(name, 0)
        if amount:
            if field.use_global_currency:
                currency = field.getGlobalCurrency()
            else:
                currency = form.get('%s_currency' % name)
            value = Money(amount, currency)
        else:
            value = None
        return value, {}


registerWidget(MoneyWidget,
               title='Money',
               description=('Renders a widget for entering monetary values'),
               used_for=('Products.FinanceFields.MoneyField.MoneyField',)
               )

