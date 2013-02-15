class Media:

    def mostrar(self, inf):
        print inf

    def mostrarMedia(self, inf):
        if inf > 7:
            print "Aprovado"
        elif inf < 7:
            print "Reprovado"
        else:
            print "De Recuperacao"

