units_sold = int(input("Units sold: "))


if units_sold <= 10:
    print('Very bad day.')
elif units_sold > 10 and units_sold <= 30:
    print('Regular day. ')
else:
    print('Very good day. ')