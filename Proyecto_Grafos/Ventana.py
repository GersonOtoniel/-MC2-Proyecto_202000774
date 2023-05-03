from tkinter import *
from Grafo import *
import math
from threading import Thread
import time
from tkinter import messagebox
from PIL import Image, ImageTk

graf = grafo()
ancho = 30

pantalla_principal = Tk()
pantalla_principal.state('zoomed')
canvas = Canvas(pantalla_principal, height=650, bg="black", cursor='arrow')
canvas.pack(fill=BOTH, expand=YES)
li=[]
img = Image.open('D:\Desktop\SAN CARLOS\MateComputo2\Proyecto_Grafos\Bola.png')
bola = ImageTk.PhotoImage(img)


def dobleclick(event):
    ingresardatos = Toplevel()
    ingresardatos.title('Agregar Punto')
    nombre = Label(ingresardatos,text='Ingresar Nombre')
    nombre.grid(row=0, column=0)
    nombre1 = Entry(ingresardatos)
    nombre1.grid(row=0,column=1)
    
    agregar = Button(ingresardatos, text='Agregar', command=lambda:agregarVertice(event.x, event.y, nombre1.get(), ingresardatos))
    agregar.grid(row=3, columnspan=2)


def agregarVertice(x, y, nombre, ventana):
    vertice = Vertice(nombre, x, y)
    graf.agregarvertice(vertice)
    ventana.destroy()
    actualizar()


def crearArista():
    arista = Toplevel()
    arista.title('Crear Arista')
    lista1 = Listbox(arista,exportselection=0)
    lista2 = Listbox(arista,exportselection=0)
    for i in graf.listavertices:
        lista1.insert(END, i.nombre)
        lista2.insert(END, i.nombre)
    lista1.pack(side=LEFT)
    lista2.pack(side=LEFT)
    label1 = Label(arista,text='Desde')
    label1.pack()
    texto1 = Entry(arista)
    texto1.pack()
    label2 = Label(arista, text='Hacia')
    label2.pack()
    texto2 = Entry(arista)
    texto2.pack()
    crearA = Button(arista,text='Crear Arista', command=lambda:Creararista(texto1.get(), texto2.get(), arista))
    crearA.pack()
    CrearB = Button(arista,text='Arista', command=lambda:Creararista(lista1.get(lista1.curselection()),lista2.get(lista2.curselection()),arista))
    CrearB.pack()

    def Creararista(v1,v2,pantalla):
        for i in graf.listavertices:
            if (v1== i.nombre):
                a = i
                for i in graf.listavertices:
                    if (v2== i.nombre):
                        b=i
                        a.vecino(b)
                        d = distancias(a,b)
                        agregar(a,b,d,a.x,a.y,b.x,b.y)
        actualizar()


def agregar(desde, hacia,distancia,x0,y0,x1,y1):
    temp = Arista(desde,hacia,distancia,x0,y0,x1,y1)
    graf.agregararista(temp)
    actualizar()
    

def VentanaCamino():
    ventana = Toplevel()
    ventana.title('Mostrar Camino')
    desde = Listbox(ventana,exportselection=0)
    hasta = Listbox(ventana,exportselection=0)
    for i in graf.listavertices:
        desde.insert(END, i.nombre)
        hasta.insert(END,i.nombre)
    desde.grid(row=1,column=0)
    hasta.grid(row=1,column=1)
    boton = Button(ventana,text='Camino', command=lambda:Camino(desde.get(desde.curselection()),hasta.get(hasta.curselection()),ventana))
    boton.grid(row=1,column=2)



def Camino(desde,hasta,camino):
    try:
        for v in graf.listavertices:
            if desde==v.nombre:
                ld,lp = graf.dist(v)
        lc=[]
        for i in range(len(graf.listavertices)):
            if lp[i]!=None:
                if hasta == graf.listavertices[i].nombre:
                    lc.append(graf.listavertices[i])
                    lc.append(lp[i])
                    lc = rec(lp[i],lc,lp)
        camino.destroy()
        mostrarcamino(list(reversed(lc)),li)
        hmc = Thread(target=mostrarcamino,args=(list(reversed(lc)),li))
        hmc.start()
        hm = Thread(target=movimiento, args =(list(reversed(lc)),bola))
        hm.start()
    except:
        messagebox.showerror('ERROR','Camino no encontrado')


def rec(vdestino,lc,lp):
    for i in range(len(graf.listavertices)):
        if vdestino == graf.listavertices[i]:
            if lp[i]!=None:
                lc.append(lp[i])
                rec(lp[i],lc,lp)
    return lc


def distancias(a,b):
    distancia = math.sqrt(math.pow(b.x-a.x,2)+math.pow(b.y-a.y,2))
    return round(distancia,2)


def mostrarcamino(lc,li):
    num = ancho/2
    for aris in li:
        canvas.delete(aris)
    del li[:]
    for i, j in zip(lc,lc[1:]):
        time.sleep(0.5)
        if i.x>=j.x and i.y>j.y:
            a = canvas.create_line(i.x+num, i.y, j.x+ancho,j.y+num,width=3, fill='DarkGoldenrod1',arrow='last',smooth=True)
            li.append(a)

        if i.x>j.x and i.y<j.y:
            a = canvas.create_line(i.x+num, i.y+ancho, j.x+ancho, j.y+num, width=3,fill='DarkGoldenrod1',arrow='last',smooth=True)
            li.append(a)

        if i.x<=j.x and i.y>j.y:
            a = canvas.create_line(i.x + num, i.y, j.x, j.y + num, width=3,fill='DarkGoldenrod1', arrow='last',smooth=True)
            li.append(a)

        if i.x<j.x and i.y<j.y:
            a = canvas.create_line(i.x+num, i.y+ancho,j.x,j.y+num,width=3,fill='DarkGoldenrod1',arrow='last',smooth=True)
            li.append(a)


def movimiento(lc,bola):
    if(len(lc)!=0):
        num = ancho / 2
        canvas.delete("obj")
        canvas.create_image(lc[0].x + num, lc[0].y + num,image=bola, tag="obj")
        # m = round((lc[1].y-lc[0].y)/(lc[1].x-lc[0].x),4)|
        aumento = 2
        tiempo=0.0001

        for i, j in zip(lc, lc[1:]):
            cords = canvas.coords("obj")
            h1 = Thread(args=(cords[0],cords[1],lc))
            h1.start()
            time.sleep(tiempo)
            if i.x >= j.x and i.y > j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, -aumento):
                    pos = canvas.coords("obj")
                    if pos[0] > j.x+num:
                        canvas.move("obj", -aumento, -aumento * m)
                        canvas.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x > j.x and i.y < j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, -aumento):
                    pos = canvas.coords("obj")
                    if pos[0] > j.x+num:
                        canvas.move("obj", -aumento, -aumento * m)
                        canvas.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x <= j.x and i.y > j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, aumento):
                    pos = canvas.coords("obj")
                    if pos[0] < j.x+num:
                        canvas.move("obj", aumento, aumento * m)
                        canvas.update()
                        time.sleep(tiempo)
                    else:
                        break
            if i.x < j.x and i.y < j.y:
                m = (j.y - i.y) / (j.x - i.x)
                for x in range(i.x, j.x, aumento):
                    pos = canvas.coords("obj")
                    if pos[0] < j.x+num:
                        canvas.move("obj", aumento, aumento * m)
                        canvas.update()
                        time.sleep(tiempo)
                    else:
                        break
    else:
        messagebox.showerror("ERROR","No se puede calcular la ruta")



def actualizar():
    num = ancho/2
    canvas.delete('all')
    for i in range(len(graf.listavertices)):
        canvas.create_oval(graf.listavertices[i].x, graf.listavertices[i].y, graf.listavertices[i].x+ancho,graf.listavertices[i].y+ancho, fill='white', width=0)
        #canvas.create_oval(graf.listavertices[i].x+5, graf.listavertices[i].y+5, graf.listavertices[i].x+ancho-5, graf.listavertices[i].y+ancho-5,fill='black', activefill='green', width=0)  


    for i in range(len(graf.listaaristas)):

        if graf.listaaristas[i].x0 >= graf.listaaristas[i].x1 and graf.listaaristas[i].y0 > graf.listaaristas[i].y1:
            canvas.create_line(graf.listaaristas[i].x0 + num, graf.listaaristas[i].y0, graf.listaaristas[i].x1 + ancho, graf.listaaristas[i].y1 + num,
                               width=3, fill="white", arrow="last", smooth=True)
        if graf.listaaristas[i].x0 > graf.listaaristas[i].x1 and graf.listaaristas[i].y0 < graf.listaaristas[i].y1:
            canvas.create_line(graf.listaaristas[i].x0 + num, graf.listaaristas[i].y0 + ancho, graf.listaaristas[i].x1 + ancho,
                               graf.listaaristas[i].y1 + num, width=3, fill="white", arrow="last", smooth=True)
        if graf.listaaristas[i].x0 <= graf.listaaristas[i].x1 and graf.listaaristas[i].y0 > graf.listaaristas[i].y1:
            canvas.create_line(graf.listaaristas[i].x0 + num, graf.listaaristas[i].y0, graf.listaaristas[i].x1, graf.listaaristas[i].y1 + num, width=3,
                               fill="white", arrow="last", smooth=True)
        if graf.listaaristas[i].x0 < graf.listaaristas[i].x1 and graf.listaaristas[i].y0 < graf.listaaristas[i].y1:
            canvas.create_line(graf.listaaristas[i].x0 + num, graf.listaaristas[i].y0 + ancho, graf.listaaristas[i].x1, graf.listaaristas[i].y1 + num,
                               width=3, fill="white", arrow="last", smooth=True)




    for i in range(len(graf.listavertices)):
        nombre = str(graf.listavertices[i].nombre)
        if len(nombre) > 5:
            nombre = nombre[0:4] + ".."
        canvas.create_text(graf.listavertices[i].x + num, graf.listavertices[i].y + num, text=nombre, fill="black", font=("bold",17))


canvas.bind("<Double-1>", dobleclick)
botonRelacionar = Button(canvas, text='Crear relacion', font=('Arial', 12), command=crearArista)  
botonRelacionar.place(x=10,y=10)
botoncamino = Button(canvas,text='Mostar Camino', font=('Arial',12), command=VentanaCamino )
botoncamino.place(x=10,y=50)



pantalla_principal.mainloop()