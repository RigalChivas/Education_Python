fruits = ['apple', 'banana', 'cherry']

quantities = [100, 70, 50]

available = [True, False, True]

ftuit_qtys_zip = zip(fruits, quantities, available)

print(ftuit_qtys_zip)  # <zip object at 0x7f8b1c1b3b40>

print(type(ftuit_qtys_zip))  # <class 'zip'>

ftuit_qtys_zip = list(ftuit_qtys_zip)

print(ftuit_qtys_zip)  # [('apple', 100), ('banana', 70), ('cherry', 50)]