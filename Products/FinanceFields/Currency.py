#!/usr/bin/python
# -*- coding: latin-1 -*-
"""Basic currency class and list of currencies.

$Id: Currency.py 129 2005-09-24 12:16:51Z roche $
"""

class Currency:
    """ Currency information 
    """

    __allow_access_to_unprotected_subobjects__ = 1

    def __init__(self, int_currency_symbol, currency_symbol,
            currency_name, country_name, country_code='',
            decimal_point=',', thousands_sep='.', 
            mon_grouping=[3, 3, 0], positive_sign='', negative_sign='-',
            frac_digits=2, int_frac_digits=2):
        self.int_currency_symbol = int_currency_symbol
        self.currency_symbol = currency_symbol
        self.currency_name = currency_name
        self.country_name = country_name
        self.country_code = country_code
        self.decimal_point = decimal_point
        self.thousands_sep = thousands_sep
        self.mon_grouping = mon_grouping
        self.positive_sign = positive_sign
        self.negative_sign = negative_sign
        self.frac_digits = frac_digits
        self.int_frac_digits = int_frac_digits

    def __cmp__(self, other):
        return cmp(self.int_currency_symbol, other.int_currency_symbol)


_currencies = (
('AED','United Arab Emirates','Dirhams',''),
('AFA','Afghanistan','Afghanis',''),
('ALL','Albania','Leke',''),
('AMD','Armenia','Drams',''),
('ANG','Netherlands Antilles','Guilders',''),
('AOA','Angola','Kwanza',''),
('ARS','Argentina','Pesos',''),
('AUD','Australia','Dollars','$'),
('AWG','Aruba','Guilders',''),
('AZM','Azerbaijan','Manats',''),
('BAM','Bosnia and Herzegovina','Convertible Marka',''),
('BBD','Barbados','Dollars','$'),
('BDT','Bangladesh','Taka',''),
('BGN','Bulgaria','Leva',''),
('BHD','Bahrain','Dinars',''),
('BIF','Burundi','Francs',''),
('BMD','Bermuda','Dollars','$'),
('BND','Brunei Darussalam','Dollars','$'),
('BOB','Bolivia','Bolivianos',''),
('BRL','Brazil','Brazil Real',''),
('BSD','Bahamas','Dollars','$'),
('BTN','Bhutan','Ngultrum',''),
('BWP','Botswana','Pulas',''),
('BYR','Belarus','Rubles',''),
('BZD','Belize','Dollars','$'),
('CAD','Canada','Dollars','$'),
('CDF','Congo/Kinshasa','Congolese Francs',''),
('CHF','Switzerland','Francs',''),
('CLP','Chile','Pesos',''),
('CNY','China','Yuan Renminbi',''),
('COP','Colombia','Pesos',''),
('CRC','Costa Rica','Colones',''),
('CUP','Cuba','Pesos',''),
('CVE','Cape Verde','Escudos',''),
('CYP','Cyprus','Pounds',''),
('CZK','Czech Republic','Koruny',''),
('DJF','Djibouti','Francs',''),
('DKK','Denmark','Kroner',''),
('DOP','Dominican Republic','Pesos',''),
('DZD','Algeria','Algeria Dinars',''),
('EEK','Estonia','Krooni',''),
('EGP','Egypt','Pounds',''),
('ERN','Eritrea','Nakfa',''),
('ETB','Ethiopia','Birr',''),
('EUR','Euro Member Countries','Euro',''),
('FJD','Fiji','Dollars','$'),
('FKP','Falkland Islands (Malvinas)','Pounds',''),
('GBP','United Kingdom','Pounds',unichr(163)),
('GEL','Georgia','Lari',''),
('GGP','Guernsey','Pounds',''),
('GHC','Ghana','Cedis',''),
('GIP','Gibraltar','Pounds',''),
('GMD','Gambia','Dalasi',''),
('GNF','Guinea','Francs',''),
('GTQ','Guatemala','Quetzales',''),
('GYD','Guyana','Dollars','$'),
('HKD','Hong Kong','Dollars','HK$'),
('HNL','Honduras','Lempiras',''),
('HRK','Croatia','Kuna',''),
('HTG','Haiti','Gourdes',''),
('HUF','Hungary','Forint',''),
('IDR','Indonesia','Rupiahs',''),
('ILS','Israel','New Shekels',unichr(8362)),
('IMP','Isle of Man','Pounds',''),
('INR','India','Rupees',unichr(8360)),
('IQD','Iraq','Dinars',''),
('IRR','Iran','Rials',''),
('ISK','Iceland','Kronur',''),
('JEP','Jersey','Pounds',''),
('JMD','Jamaica','Dollars','$'),
('JOD','Jordan','Dinars',''),
('JPY','Japan','Yen',unichr(165)),
('KES','Kenya','Shillings',''),
('KGS','Kyrgyzstan','Soms',''),
('KHR','Cambodia','Riels',''),
('KMF','Comoros','Francs',''),
('KPW','Korea (North)','Won',unichr(8361)),
('KRW','Korea (South)','Won',unichr(8361)),
('KWD','Kuwait','Dinars',''),
('KYD','Cayman Islands','Dollars','$'),
('KZT','Kazakstan','Tenge',''),
('LAK','Laos','Kips',''),
('LBP','Lebanon','Pounds',''),
('LKR','Sri Lanka','Rupees',unichr(8360)),
('LRD','Liberia','Dollars','L$'),
('LSL','Lesotho','Maloti',''),
('LTL','Lithuania','Litai',''),
('LVL','Latvia','Lati',''),
('LYD','Libya','Dinars',''),
('MAD','Morocco','Dirhams',''),
('MDL','Moldova','Lei',''),
('MGA','Madagascar','Ariary',''),
('MKD','Macedonia','Denars',''),
('MMK','Myanmar (Burma)','Kyats',''),
('MNT','Mongolia','Tugriks',''),
('MOP','Macau','Patacas',''),
('MRO','Mauritania','Ouguiyas',''),
('MTL','Malta','Liri',''),
('MUR','Mauritius','Rupees',unichr(8360)),
('MVR','Maldives (Maldive Islands)','Rufiyaa',''),
('MWK','Malawi','Kwachas',''),
('MXN','Mexico','Pesos',''),
('MYR','Malaysia','Ringgits',''),
('MZM','Mozambique','Meticais',''),
('NAD','Namibia','Dollars','N$'),
('NGN','Nigeria','Nairas',unichr(8358)),
('NIO','Nicaragua','Gold Cordobas',''),
('NOK','Norway','Krone',''),
('NPR','Nepal','Nepal Rupees',unichr(8360)),
('NZD','New Zealand','Dollars','$'),
('OMR','Oman','Rials',''),
('PAB','Panama','Balboa',''),
('PEN','Peru','Nuevos Soles',''),
('PGK','Papua New Guinea','Kina',''),
('PHP','Philippines','Pesos',''),
('PKR','Pakistan','Rupees',unichr(8360)),
('PLN','Poland','Zlotych',''),
('PYG','Paraguay','Guarani',''),
('QAR','Qatar','Rials',''),
('ROL','Romania','Lei',''),
('RUR','Russia','Rubles',''),
('RWF','Rwanda','Rwanda Francs',''),
('SAR','Saudi Arabia','Riyals',''),
('SBD','Solomon Islands','Dollars','SI$'),
('SCR','Seychelles','Rupees',unichr(8360)),
('SDD','Sudan','Dinars',''),
('SEK','Sweden','Kronor',''),
('SGD','Singapore','Dollars','S$'),
('SHP','Saint Helena','Pounds',''),
('SIT','Slovenia','Tolars',''),
('SKK','Slovakia','Koruny',''),
('SLL','Sierra Leone','Leones',''),
('SOS','Somalia','Shillings',''),
('SPL','Seborga','Luigini',''),
('SRG','Suriname','Guilders',''),
('STD','S\xe3o Tome and Principe','Dobras',''),
('SVC','El Salvador','Colones',''),
('SYP','Syria','Pounds',''),
('SZL','Swaziland','Emalangeni',''),
('THB','Thailand','Baht',unichr(3647)),
('TJS','Tajikistan','Somoni',''),
('TMM','Turkmenistan','Manats',''),
('TND','Tunisia','Dinars',''),
('TOP','Tonga',"Pa'anga",''),
('TRL','Turkey','Liras',unichr(8356)),
('TTD','Trinidad and Tobago','Dollars','$'),
('TVD','Tuvalu','Tuvalu Dollars','$'),
('TWD','Taiwan','New Dollars','NT$'),
('TZS','Tanzania','Shillings',''),
('UAH','Ukraine','Hryvnia',''),
('UGX','Uganda','Shillings',''),
('USD','United States of America','Dollars','$'),
('UYU','Uruguay','Pesos',''),
('UZS','Uzbekistan','Sums',''),
('VEB','Venezuela','Bolivares',''),
('VND','Viet Nam','Dong',unichr(8363)),
('VUV','Vanuatu','Vatu',''),
('WST','Samoa','Tala',''),
('XAF','Communauté Financière Africaine BEAC','Francs',''),
('XAG','Silver','Ounces',''),
('XAU','Gold','Ounces',''),
('XCD','East Caribbean Dollars','Dollars','$'),
('XDR','International Monetary Fund (IMF) Special Drawing Rights','',''),
('XOF','Communauté Financière Africaine BCEAO','Francs',''),
('XPD','Palladium Ounces','',''),
('XPF','Comptoirs Français du Pacifique','Francs',''),
('XPT','Platinum','Ounces',''),
('YER','Yemen','Rials',''),
('YUM','Yugoslavia','New Dinars',''),
('ZAR','South Africa','Rand','R'),
('ZMK','Zambia','Kwacha',''),
('ZWD','Zimbabwe','Zimbabwe Dollars','$'),
)

CURRENCIES = {}
SYMBOLS_MAP = {}
for int_symbol, co_name, cur_name, symbol in _currencies:
    cur = Currency(int_symbol, symbol, cur_name, co_name)
    CURRENCIES[int_symbol] = cur
    if symbol:
        SYMBOLS_MAP[symbol] = cur

# xxx: Let USD win the dollar wars until we find a solution	
SYMBOLS_MAP['$'] = 'USD'
