from Products.Archetypes.utils import DisplayList

ADD_CONTENT_PERMISSION = 'Add FinanceFields content'
PROJECTNAME = "FinanceFields"
GLOBALS = globals()
I18N_DOMAIN = 'plone_accounting'
SKINS_DIR = 'skins'

from AccessControl import allow_module
allow_module('Products.FinanceFields.config')
allow_module('Products.FinanceFields.Money')

from Currency import CURRENCIES

l = DisplayList()
for cur in CURRENCIES.values():
    symbol = cur.int_currency_symbol
    l.add(symbol, symbol, symbol)
l._itor.sort()
CURRENCY_DISPLAY_LIST = l
