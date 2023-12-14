


# DEKLARACIJA / INICIJALIZACIJA
vehicle_db = {
    1: ['Kamion', 'Iveco', 'OS 001 ZZ', 2015, 45_000.00],
    2: ['Kamion', 'Iveco', 'OS 002 ZZ', 2015, 47_000.00],
    3: ['Tegljač', 'MAN', 'RI 001 ZZ', 2018, 78_000.00],
    4: ['Tegljač', 'MAN', 'RI 002 ZZ', 2020, 97_000.00],
    5: ['Kombi', 'Mercedes Benz', 'ST 001 ZZ', 2013, 12_000.00],
    6: ['Kombi', 'Volkswagen', 'ST 002 ZZ', 2021, 35_000.00],
    7: ['Dostavno vozilo', 'Volkswagen', 'ZG 001 ZZ', 2010, 9_000.00],
    8: ['Dostavno vozilo', 'Volkswagen', 'ZG 002 ZZ', 2010, 9_300.00]
    
}  
# GLAVNI DIO PROGRAMA -> MAIN


header_top_line = f'{'ID':<5}{'Tip':<25}{'Proizvođač':<25}{'Registarska':<15}{'Godina':<20}{'Cijena':>15}'   #:+<34 dodaje + znak umjesto razmaka
header_bottom_line = f'{'':<5}{'':<25}{'':<25}{'oznaka':<15}{'prve registracije':<20}{'(EUR)':>15}'  
# header_bottom_line = f'{'':<5}{'':<25}{'':<25}{'oznaka':<15}{'prve registracije':<len{'prve registracije'}}{'(EUR)':>15}'  
# header_top_line = f'ID\tTip\t\tProizvođač\tRegistarska\tGodina prve registracije\tCijena'
# header_bottom_line = f'  \t   \t\t          \toznaka\t\tprve registracije\t\t(EUR)'

print(header_top_line)
print(header_bottom_line)
print('-' * 108)

for key, value in vehicle_db.items():
    print(f'{key:<5}', end='')
    # for item in value:
        # print(item, end='\t\t')
    print(f'{value[0]:<25}', end='')
    print(f'{value[1]:<25}', end='')
    print(f'{value[2]:<15}', end='')
    print(f'{value[3]:<20}', end='')
    print(f'{value[4]:>15.2f} EUR', end='\n')
    


# ZAVRSETAK - POSPREMANJE


