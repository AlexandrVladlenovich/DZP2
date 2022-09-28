import random
def mixList(list):
    random.shuffle(list)
    print(f'Перемешанный список: {list}')

list = input('Введите через пробел название позиций списка: ').split()
print(f'Исходный список: {list}')
res = mixList(list)