values = [1, 23, 42, 'asdfg']
print(values)
transformed_values = list(map(lambda x: x, values))
print(transformed_values)
if values == transformed_values:
 print('ok')
else:
 print('fail')
