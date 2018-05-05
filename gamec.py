import random as ram


class jugador (object):
    nombre = []
    vida = []
    danio = []
    defensa = []
    moral = []

    def ing_dat(self):
        print('\n###ingrese nombre del campeon ###')
        nomb = str(input('\nnombre campeon: '))
        self.nombre.append(nomb)

        print('\n###ingrese vida del campeon ###')
        life = int(input('vida total de campeon: '))
        self.vida.append(life)

        print('###ingrese danio del campeon ###')
        dan = int(input('cantidad de danio del campeon: '))
        self.danio.append(dan)

        print('###ingrese defensa del campeon ###')
        defe = int(input('ingrese cantidad de defensa: '))
        self.defensa.append(defe)

        print('###ingrese moral del campeon ###')
        mor = int(input('ingrese cantidad de moral:'))
        self.moral.append(mor)

    def hab_pat_vol(self, x, y):
        # i = int(input('\ningrese 0 para campeon1: \ningrese 1 para campeon2:'))
        if x == 0 or x == 1:
            pat_vol = self.danio[x] + 30
            self.danio[x] = pat_vol

            aument_mor = self.moral[x] + 5
            self.moral[x] = aument_mor

            if y != x:
                self.vida[y] = self.vida[y] - self.danio[x]

            if self.vida[0] > 100 and self.vida[1] > 100:
                print('\n resultado de la lucha, el jugador ',
                      self.nombre[0], 'cuenta con ', self.vida[0], ' de vida')
                print('\n resultado de la lucha, el jugador ',
                      self.nombre[1], 'cuenta con ', self.vida[1], ' de vida')

    def hab_ganch_hig(self):
        i = int(input('\ningrese 1 para campeon1: \ningrese 2 para campeon2:'))
        if i == 1 or i == 2:
            ganch_hig = self.danio[i] + 70
            self.danio[i] = ganch_hig

            aument_mor = self.moral[i] + 15
            self.moral[i] = aument_mor
        else:
            print('solo hay 2 jugadores, mas nada!!')

    def pelea_sin_hab(self):
        if self.nombre[0] != self.nombre[1]:
            print('Que comienze la lucha!! entre ',
                  self.nombre[0], 'y ', self.nombre[1])

            if self.danio[0] > self.danio[1]:
                print('el jugador ', self.nombre[0],
                      'mayor daño que ', self.nombre[1])
                dism_vida = self.vida[1] - self.danio[0]
                self.vida[1] = self.vida[1] - dism_vida
            elif self.danio[1] > self.danio[0]:
                print('jugador ', self.nombre[1],
                      'mayor daño que ', self.nombre[0])
                dism_vida1 = self.vida[0] - self.danio[1]
                self.vida[1] = self.vida[1] - dism_vida1

            if self.vida[0] > self.vida[1]:
                print('jugador ', self.nombre[0], 'ha ganado')
            else:
                print(self.nombre[1], 'ha ganado')

    def pelea_con_hab(self):
        print('presione el numero 0 para ataque del campeon: ',
                      self.nombre[0], 'o 1 para el campeon: ', self.nombre[1])
        x = int(input('opcion: '))

        if x == 0:
            y=1
        else:
            y=0

        # print(x)
        self.hab_pat_vol(x, y)


run=jugador()
count=2

while count > 0:
    count=count - 1
    run.ing_dat()
# run.pelea_sin_hab()

if run.nombre[0] != run.nombre[1]:
    print('Que comienze la lucha!! entre ', run.nombre[0], 'y ', run.nombre[1])
    counter=100
    while counter > 0:
        counter=counter - 1
        run.pelea_con_hab()
else:
    print('\nLos nombres de los jugadores no deben ser iguales')
