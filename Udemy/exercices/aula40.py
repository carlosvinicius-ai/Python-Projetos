"""
Iterando strings com while
"""

count = 0
name = 'Lebron James'
new_name = ''

while count < len(name):
    new_name += f'*{name[count]}'
    count += 1


print(name)
print(new_name)
