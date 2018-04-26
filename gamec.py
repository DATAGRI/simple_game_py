class jugador (object):
    nombre = []
    vida = []
    danio = []
    defensa = []
    moral = []

    def ing_dat (self):
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

run = jugador()
run.ing_dat()



                     
                
              
        
