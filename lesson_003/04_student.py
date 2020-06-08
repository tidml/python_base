# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000


def money_requested_from_parents():
    expenses = 12000
    total_expenses = 0
    total_amount_of_educational_grant = educational_grant * 10
    x = 0
    while x < 10:
        x += 1
        total_expenses += expenses
        expenses += (expenses * 0.03)
    if total_amount_of_educational_grant < total_expenses:
        requested_money = total_expenses - total_amount_of_educational_grant
        print(f'Студенту надо попросить {round(requested_money, 2)} рублей')
    else:
        print('Студенту хватает денег')


money_requested_from_parents()

#зачет!