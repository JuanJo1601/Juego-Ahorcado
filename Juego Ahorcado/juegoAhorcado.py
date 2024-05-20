class Ahorcado:

    def __init__(self, palabras):
        self.palabras = palabras
        self.intentos_max = 6
        self.iniciar_nueva_partida()
    
    def iniciar_nueva_partida(self):
        self.palabra = list((self.palabras))        
        self.guiones = ['_'] * len(self.palabra)
        self.intentos = self.intentos_max
        self.letras_usadas = []
        self.terminado = False
    
    def validar_letra(self, letra):
        Letra = letra
        if Letra in self.letras_usadas:
            return "La letra ya fue utilizada."
        self.letras_usadas.append(Letra)
        letra_encontrada = False
        for i in range(len(self.palabra)):
            if self.palabra[i] == Letra:
                self.guiones[i] = Letra
                letra_encontrada = True
        if letra_encontrada:
            if '_' not in self.guiones:
                self.terminado = True
                return 'Has ganado'
            return "¡Correcto!"
        else:
            self.intentos -= 1
            if self.intentos == 0:
                self.terminado = True
                return 'Has sido ahorcado'
            return "Incorrecto."

    def jugar(self):
        while not self.terminado:
            self.mostrar_estado()
            letra = input("Escoge una letra: ")
            if len(letra) != 1:
                print("Por favor, introduce solo una letra.")
                continue
            mensaje = self.validar_letra(letra)
            print(mensaje)
        print("Juego terminado.")