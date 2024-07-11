
first,second,third=123,456,789#присваиваем переменным соответсвующие значения
print(int(first))
print(int(second))
print(int(third))
if first==second and second==third:# если условие :фест равно секонд И секонд рано фед выполняется то:
    print(3)# выводим на консоль  цифру 3
elif first==second or first==third:# не выполнем это условие если верно первое
    print(2)
else:#  иначе  выводим .....
    print(0)# выводим цифру 0
first,second,third=42,69,42# меняем значения у переменных и дальше как выше по алгоритму
print(int(first))
print(int(second))
print(int(third))
if first==second and second==third:
    print(3)
elif first==second or first==third:
    print(2)
else:
    print(0)








def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
