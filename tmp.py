with open('./requirements.txt', 'r') as _:
    data = _.read()

d = ',\n'.join([f'\'{e}\'' for e in data.split('\n')])

print(d)
