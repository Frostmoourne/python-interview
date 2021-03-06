"""
Задание 5*.Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции
реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца,
кроме первого и последнего. Например, при сроке вклада в 6 месяцев
пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.

Примечание: используем функциональный подход (не ООП)
Пример: 10 тыс на 24 мес, пополнение - по 100
chargable_deposit(10000, 24, 100)
к концу срока: 13739.36
"""