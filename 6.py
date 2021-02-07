# Создать структуру товарав. Сделать вывод аналитики по всем праметрам. Повторяющиеся наипенования единиц упразднить.
data = []
ask = input('Want to add vew product? Y/N')
id = 0
while ask == 'Y':
    id = id + 1
    name = input('Enter product name.')
    cost = int(input('Enter product cost.'))
    quantity = int(input('Enter product quantity.'))
    units = input('Enter product units.')
    product = (id, {'name' : name, 'cost' : cost, 'quantity' : quantity, 'units' : units})
    data.append(tuple(product))
    ask = input('Want to add vew product? Yes/None')
analytic = {'name': [], 'cost' : [], 'quantity' : [], 'units' : set()}
for i in data:
    analytic['name'].append(i[1]['name'])
    analytic['cost'].append(i[1]['cost'])
    analytic['quantity'].append(i[1]['quantity'])
    analytic['units'].add(i[1]['units'])
print(analytic)

