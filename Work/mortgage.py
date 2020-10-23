# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_pay = 1000
month = 0
extra_payment_start_month = int(input('when we start extra payment: '))
extra_payment_end_month = int(input('when we end extra payment: '))
extra_payment = int(input('how much extra payment is: '))

while principal > 0:
    month += 1

    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - (payment+extra_payment)
        total_paid += payment+extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment

    if principal < 0:
        overpay = abs(principal)
        total_paid -= overpay
        principal += overpay

    print(month, total_paid, principal)

print('Total paid', total_paid)