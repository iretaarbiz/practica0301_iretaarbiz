import cProfile
def capitalizado(fichero, nombre):
    with open(fichero, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        for i in range(len(lineas)):
            lineasep = lineas[i].split(',')
            lineasep[0] = lineasep[0].split(' ')
            lineasep[0] = lineasep[0][0]
            lineasep[1] = lineasep[1][:-2]
            lineasep[0] = lineasep[0].title()
            if lineasep[0].lower() == nombre.lower():
                return lineasep[0]
capitalizado('50.csv', 'ricardo')
def letradni(fichero, nombre):
    letrasdni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    with open(fichero, 'r', encoding='utf-8') as file:
        lineas = file.readlines()
        for i in range(len(lineas)):
            lineasep = lineas[i].split(',')
            lineasep[0] = lineasep[0].split(' ')
            lineasep[0] = lineasep[0][0]
            lineasep[1] = lineasep[1][:-2]
            lineasep[0] = lineasep[0].title()
            if lineasep[0].lower() == nombre.lower():
                restodni = int(lineasep[1]) % 23
                return letrasdni[restodni]

print("Nombre:", capitalizado('50.csv', 'ricardo'), "\nLetra DNI:", letradni('50.csv', 'ricardo'))
print("Nombre:", capitalizado('1000.csv', 'ricardo'), "\nLetra DNI:", letradni('1000.csv', 'ricardo'))

cProfile.run(capitalizado('50.csv', 'ricardo'))
cProfile.run(capitalizado('1000.csv', 'ricardo'))
cProfile.run(letradni('50.csv', 'ricardo'))
cProfile.run(letradni('1000.csv', 'ricardo'))

