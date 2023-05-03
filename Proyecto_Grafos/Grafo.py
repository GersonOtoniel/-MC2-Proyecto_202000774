import sys

class grafo:
    def __init__(self):
        self.listavertices = []
        self.listaaristas = []

    def agregarvertice(self, v):
        self.listavertices.append(v)

    def agregararista(self, a):
        self.listaaristas.append(a)


    def dist(self,inicio):
        listadistancias=[]
        listavisitadoe=[]
        listaprevios=[]

        for i in range(len(self.listavertices)):
            listadistancias.append(self.listavertices[i].distancia)
            listavisitadoe.append(self.listavertices[i].visitado)
            listaprevios.append(self.listavertices[i].predecesor)
            if inicio.nombre == self.listavertices[i].nombre:
                listadistancias[i]=0
                listavisitadoe[i]=True
                listaprevios[i]=None

        for i in self.listaaristas:
            for j in inicio.la:
                if (inicio.nombre==i.desde.nombre and j.nombre==i.hacia.nombre):
                    distancia = i.distancia
                    listadistancias[self.listavertices.index(i.hacia)]=distancia
                    listaprevios[self.listavertices.index(i.hacia)]=inicio

        for bol in listavisitadoe:
            for bol2 in listavisitadoe:
                nmin = sys.maxsize
                if bol2 == False:
                    for nm in range(len(listadistancias)):
                        if listadistancias[nm]<nmin and listavisitadoe[nm]==False:
                            nmin=listadistancias[nm]

                    temp = nmin
                    indice=listadistancias.index(temp)
            listavisitadoe[indice] = True

            for i in self.listaaristas:
                for w in self.listavertices[indice].la:
                    if self.listavertices[indice].nombre==i.desde.nombre and w.nombre==i.hacia.nombre:
                        nuevad = listadistancias[indice]+i.distancia
                        nom = i.hacia.nombre
                        for p in self.listavertices:
                            if p.nombre== nom:
                                pos = self.listavertices.index(p)
                        if nuevad<listadistancias[pos]:
                            listadistancias[pos]=nuevad
                            listaprevios[pos]=i.desde
        return listadistancias, listaprevios



class Vertice:
    def __init__(self, nombre, x, y):
        self.la = []
        self.nombre = nombre
        self.x = x
        self.y = y
        self.distancia = sys.maxsize
        self.predecesor=None
        self.visitado=False

    def __str__(self):
        return str(self.la)

    def vecino(self,ver_ad):
        self.la.append(ver_ad)

class Arista:
    def __init__(self, desde, hacia,distancia, x0, y0, x1, y1) -> None:
        self.desde = desde
        self.hacia = hacia
        self.distancia=distancia
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1