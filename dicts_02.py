employee_123456 = {
    'employee_id' : '123456',
    'first_name' : 'Pero',
    'last_name' : 'Peric',
    'email' : 'pero.peric@example.com'
    # 'address' : {
    #     'street' : 'Ilica 123'
    #     'postal_code' : '10000'
    # }
}

employee_654321 = {
    'employee_id' : '123456',
    'first_name' : 'Pero',
    'last_name' : 'Peric',
    'email' : 'pero.peric@example.com'
}

employees = []
employees.append(employee_123456)
employees.append(employee_654321)

for employee in employees:
    #print(employee)
    for key, value in employee.items():
        print(key, value)
    print()

