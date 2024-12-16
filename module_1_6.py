#Словари
my_dict = {'Саян': 1994, 'Александр': 1999, 'Николай': 1984, 'Владимир': 1980}
print(my_dict)
print(my_dict['Николай'])
print(my_dict.get('Андрей','Такого ключа нет'))
my_dict.update({'Виктория': 1996, 'Людмила': 1995})
print(my_dict)
my_dict.pop('Саян')
print(my_dict)
#Множества
my_set = {1, 2, 3, 'World', 3.14, 3, True, 'NewYear', 'World', 2}
print(my_set)
my_set.add(6)
my_set.add('Urban')
print(my_set)
my_set.remove(2)
print(my_set)
