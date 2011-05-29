""" Money extends FixedPoint with currency information

    NOTE: We do not allow any operations with floats
"""

RCS_id='$Id: Money.py 189 2005-10-08 07:07:58Z roche $'

import re
import string
from fixedpoint import FixedPoint
from Currency import Currency, CURRENCIES, SYMBOLS_MAP
from types import StringType, UnicodeType, StringTypes, FloatType, \
    IntType

float_pat = '(-){0,1}\d+(\.\d+){0,1}'
#money_pos_pat = '[A-Z]{1,3}\s%s' % float_pat
money_pos_pat = '[^0-9]{1,3}\s%s' % float_pat
money_neg_pat = '\(%s\)' % money_pos_pat
money_pat = '%s|%s' % (money_neg_pat, money_pos_pat)

float_re = re.compile(float_pat)
money_pos_re = re.compile(money_pos_pat)
money_neg_re = re.compile(money_neg_pat)
money_re = re.compile(money_pat)

class InvalidMoneyString(Exception):
    pass

# Nice recipe for formatting number with commas from:
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/498181
def thousands_commas(amount):
    temp = "%.2f" % amount
    profile=re.compile(r"(\d)(\d\d\d[.,])")
    while 1:
        temp, count = re.subn(profile, r"\1,\2", temp)
        if not count:
            break
    return temp

def parseString(s):
    # remove commas
    s = s.replace(',', '')
    if not (money_re.match(s) or float_re.match(s)):
        raise InvalidMoneyString(s)
    if money_neg_re.match(s):
        # strip the brackets
        s = s[1:-1]
        cur, value = s.split()
        # add minus symbol to fixedpoint value
        s = '%s -%s' % (cur, value)
    if money_re.match(s):
        cur, value = s.split()
        if CURRENCIES.has_key(cur):
            cur = CURRENCIES[cur]
        elif SYMBOLS_MAP.has_key(cur):
            cur = SYMBOLS_MAP[cur]
    else:
        cur = None
        value = s
    return cur, FixedPoint(value)

class Money:

    __allow_access_to_unprotected_subobjects__ = 1

    def __init__(self, amount, currency):
        __traceback_info__ = (amount, currency)
        assert not isinstance(amount, FloatType), str(amount)
        if isinstance(amount, StringTypes) and len(amount) > 0:
            amount = self._decode(amount)
        if not isinstance(amount, FixedPoint):
            amount = FixedPoint(amount)
        self.amt = amount
        if isinstance(currency, StringTypes):
            currency = CURRENCIES[currency]
        assert isinstance(currency, Currency), (
            str(currency), type(currency))
        self.ccy = currency

    def _decode(self, repr):
        """ If we get e.g. '(SYM 123)' """
        cur, amount = parseString(repr)
        return amount

    def __repr__(self):
        symbol = self.ccy.currency_symbol or \
            self.ccy.int_currency_symbol
        return '%s %s' % (symbol, thousands_commas(self.amt))

    __str__ = __repr__

    def __len__(self):
    	return len(self.__str__())

    def amount(self):
        return self.amt

    def currency(self):
        return self.ccy

    def __neg__(self):
        return Money(-self.amt, self.ccy)

    def __add__(self, other):
        assert not isinstance(other, FloatType), str(other)
        if isinstance(other, Money):
            assert self.ccy == other.currency(), (
                'currency mismatch', `self`, `other`)
            return Money(self.amt+other.amount(), self.ccy)
        else:
            return Money(self.amt+other, self.ccy)

    def __sub__(self, other):
        assert not isinstance(other, FloatType), str(other)
        if isinstance(other, Money):
            assert self.ccy == other.currency(), (
                'currency mismatch', `self`, `other`)
            return Money(self.amt-other.amount(), self.ccy)
        else:
            return Money(self.amt-other, self.ccy)

    def __mul__(self, other):
        assert not isinstance(other, FloatType), str(other)
        if isinstance(other, Money):
            raise TypeError, 'multiplying monetary quantities'
        else:
            return Money(self.amt*other, self.ccy)

    def __div__(self, other):
        assert not isinstance(other, FloatType)
        q, r = divmod(self, other)
        #if r != Money(0, self.ccy):
        #    raise RuntimeError, 'rounding is necessary: %s/%s' % (self.__repr__(), str(other))
        if isinstance(other, Money):
            assert self.ccy == other.currency(), (
                'currency mismatch', `self`, `other`)
            return Money(self.amt/other.amount(), self.ccy)
        else:
            return Money(self.amt/other, self.ccy)

    def __divmod__(self, other):
        if isinstance(other, Money):
            other = other.amt
        q, r = self.amt.__divmod__(other)
        return Money(q, self.ccy), Money(r, self.ccy)

    def __cmp__(self, other):
        if not isinstance(other, (StringType, UnicodeType, IntType, Money )):
            return -1
        if isinstance(other, StringTypes) and not money_re.match(other):
            return -1
        if not isinstance(other, Money):
            other = Money(other, self.ccy)
        return cmp(self.amt, other.amt)

    def __hash__(self):
        return str(self)

    def copy(self):
        return Money(self.amt, self.ccy)

    __copy__ = copy

    def __neg__(self):
        return Money(-self.amt, self.ccy)

    def __abs__(self):
        if self.amt >= 0:
            return self.copy()
        else:
            return -self

    __radd__=__add__
    __rsub__=__sub__
    __rmul__=__mul__
    __rdiv__=__div__

