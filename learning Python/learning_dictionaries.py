wife = {'name': 'Kailey', 'eyes': 'blue'}

wife_name = wife['name']
wife['husband'] = 'Joel'

wife_sib = wife.get('siblings', "No siblings found")

for key, value in wife.items():
    print(value)
    # print(value)