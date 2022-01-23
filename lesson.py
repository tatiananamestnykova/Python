int_item = 10
comp_item = 18
mult_int = int_item * 2
item_2 = 1
item_3 = 0
item_4 = 0
item_5 = 1
usd_item = 6.77
usd_usd_rate = 1
eur_item = 8.42
usd_eur_rate = 0.86
uah_item = 294.1
usd_uah_rate = 26.23
chf_item = 11.3
usd_chf_rate = 0.91
rub_item = 950
usd_rub_rate = 71.88
byn_item = 32.76
usd_byn_rate = 2.46

if mult_int > comp_item:
    print('Переменная mult_int >', comp_item)
div_int = int_item / 2
if div_int < comp_item:
    print('Переменная div_int <', comp_item)
item_1 = 10 + int_item

if item_1 < comp_item:
    print('Переменная item_1 <', comp_item)
else:
    print('Переменная item_1 >=', comp_item)

if item_2:
    print('Переменная item_2 =', item_2)
else:
    print('Переменная item_2 =', item_3)

if item_3:
    print('Переменная item_3 =', item_2)
else:
    print('Переменная item_3 =', item_3)

if item_5:
    print('Переменная item_5 =', item_5)
else:
    print('Переменная  item_5 =', item_4)

if item_4:
    print('Переменная item_4 =', item_5)
else:
    print('Переменная item_4 =', item_4)

currency_convertor = item_2
item_2 = 1

if currency_convertor:
    currency_usd = usd_item
    target_currency = eur_item
    target_currency_amount = 50
    currency_result = 0


if target_currency == 'eur':
    currency_result = target_currency_amount * usd_eur_rate
    print(target_currency_amount, eur_item, '=', currency_result, usd_item)

elif target_currency == 'uah':
    currency_result = target_currency_amount * usd_uah_rate
    print(target_currency_amount, uah_item, '=', currency_result, usd_item)

else:
    print('Unknow currency')
    print('Переменная currency_convertor = ', item_3)