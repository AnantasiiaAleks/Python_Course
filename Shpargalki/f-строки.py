name = "John"
print(f'Hi, {name}.') #- Hi, John.
print('Hi, %s.' % name) #- Hi, John
print('{} Hi, {}'.format(name[:2], name)) #- Hi, {name}
print('{b} Hi, {a}'.format(b=name[:2], a=name)) #- Hi, {name}