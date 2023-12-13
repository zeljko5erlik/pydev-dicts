vehicles_fleet_lists = []
vehicles_info = ['ID', 'Tip', 'Proizvođač', 'Registarska oznaka', 'Godina prve registracije', 'Cijena u EUR']

fleet_number = int(input('Unesite broj vozila vaše firme: '))
print()

for number in range(fleet_number):
    fleet_vehicle_info = {}
    for vehicle_info in vehicles_info:
        input_info = input(f'Unesite {vehicle_info} {number + 1}. vozila: ')

        fleet_vehicle_info[vehicle_info] = input_info
        
    vehicles_fleet_lists.append(fleet_vehicle_info)
    print()

print(vehicles_info[0], '\t', vehicles_info[1], '\t' * 2 , vehicles_info[2], '\t' * 2, vehicles_info[3], '\t', vehicles_info[4], '\t', vehicles_info[5], sep='', end='\n')
# message = vehicles_info[0] + '\t' + vehicles_info[1] + '\t' * 2 + vehicles_info[2] + ('\t' * 2) + vehicles_info[3] + '\t' + vehicles_info[4] + '\t' + vehicles_info[5]
# print(message)
print('_' * 116)
print()
for vehicle in vehicles_fleet_lists:
    print(f'{vehicle[vehicles_info[0]]:<7} {vehicle[vehicles_info[1]]:<15} {vehicle[vehicles_info[2]]:<20} \t {vehicle[vehicles_info[3]]:<15} \t \t {vehicle[vehicles_info[4]]:<4} \t \t \t {vehicle[vehicles_info[5]]}', end='\n')
print()
