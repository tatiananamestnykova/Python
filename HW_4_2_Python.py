import time
# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли,
# выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.
#
#
# amount_money = 10
# while True:
#     input_value = input('input your value:')
#     summ_money = int(input_value) * 26.35
#     print('summ_money = ', summ_money, 'usd')
#     if summ_money > 10:
#       break
# D:\python\python.exe D:/work/p_inter/Python/HW_4_Python.py
# input your value:2
# summ_money =  52.7 usd
#
# Process finished with exit code 0


# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится ответ в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

usd_uah_rate = 28.69
eur_uah_rate = 32.41
chf_uah_rate = 31.22
gbp_uah_rate = 38.75
cny_uah_rate = 4.53
amount_uah = 10

while True:
    input_value = input('input you value:')
    sum_usd = input_value * usd_uah_rate
    print('sum_usd:', sum_usd, usd)
    if sum_usd > 10:
     break

# sum_eur =
# sum_chf =
# sum_gbp =
# sum_cny =