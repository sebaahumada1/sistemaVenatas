import os
import time
from datetime import date,datetime
from tkinter import *
from tkinter import messagebox
import sqlite3
import pygame
import matplotlib.pyplot as plt
from tkinter import ttk


raiz=Tk()
conexion=sqlite3.connect("base.db")


raiz.title("Trabajo Final")
raiz.geometry('580x440')
raiz.title("Trabajo Final")
raiz.resizable(0,0)
ventanaAgregar = None
listadoCompras=[]

def toxica():

    
    
    pygame.mixer.pre_init(44100, -16, 1024)
    #pygame.mixer.music.set_volume(0.5)
    pygame.init()
    pygame.mixer.get_init()
    pygame.mixer.music.load('sonido/toxica.mp3')
    pygame.mixer.music.play(1)
    pygame.mixer.music.rewind()
    pygame.init()




color_fondo = 'Skyblue4'
white = 'white'
raiz.config(bg=color_fondo)



 #====FRAME LOGIN=====
login = Frame(raiz, bg="#440c29")
login.place(width=580, height=440,x=0,y=0)
toxica()



fondoLog=PhotoImage(file="imagenes/fondoPet.png")
imagenPet=Label(login,image=fondoLog)
imagenPet.place(x=0,y=0)



#====Objetos del login====

placeholder = StringVar()
placeholder.set('Nombre de Usuario')

contraseña_placeholder = StringVar()
contraseña_placeholder.set('Contraseña')

tituloLogin = Label(login,text="Pet Shop Login ")








usuarioEntry = Entry(login)
contraseñaEntry = Entry(login)

def contacto():
    sonido()
    messagebox.showwarning("Contacto","Contacte a ADMIN para ingresar. \n \n Whatsapp: 2615928607 \n \n E-mail: sahumada256@gmail.com")
    
contacto = Button(login,text="Contacto",command=contacto)


#==== Configuraciones de objetos de login=====

tituloLogin.place(x=10,y=10, width=560, height=100)
tituloLogin.config(font="Ubuntu 30 normal", fg='white', bg=color_fondo)

usuarioEntry.place(x=110,y= 150,width=350, height=50)
usuarioEntry.config(textvariable=placeholder, font="Ubuntu 15 normal",bg=color_fondo,border=3,fg=white)

contraseñaEntry.place(x=110,y=220, width=350, height=50)
contraseñaEntry.config(textvariable=contraseña_placeholder, font="Ubuntu 15 normal",bg=color_fondo, fg=white,bd=3,)
cand=PhotoImage(file="imagenes/candado1.png")
candado=Label(login,image=cand)
candado.place(x=55,y=220)

usua=PhotoImage(file="imagenes/user1.png")
us=Label(login,image=usua)
us.place(x=55,y=150)
def show(evento):
    contraseñaEntry.config(show="*")
    contraseñaEntry.delete(0,END)
contraseñaEntry.bind("<Button-1>",show)

def borrarUsuario(evento):
    usuarioEntry.delete(0,END)
usuarioEntry.bind("<Button-1>",borrarUsuario)


contacto.place(x=140, y=350, width=300,height=40)
contacto.config(font="Ubuntu 15 normal",bg=color_fondo,fg='white',border=3)
miFrame1=Frame(raiz,width=600,height=600)
def ingreso():
    sonido()
    
    
    if(usuarioEntry.get() == "seba" and contraseñaEntry.get() == "admin"):
        login.place_forget()
        
        raiz.geometry("600x600")
        miFrame1.place(x=0,y=0)
        

        
    else:
        messagebox.showwarning("Sistema","Error, ingreso mal usuario o Contraseña")

BotonEntrar= Button(login,text="Iniciar sesion",command=ingreso)

BotonEntrar.place(x=140, y=290, width=300,height=40,)
BotonEntrar.config(font="Ubuntu 15 normal",bg="white",fg=color_fondo,border=2,)


##frame ingreso a pagina principal creado para luego ingresar con botonIngreso

frameIngresandoPaginaPrincipal=Frame(raiz,width=600,height=600,bg="wheat3")

#frameBotones.

frameBotones=Frame(frameIngresandoPaginaPrincipal,width=600,height=100,bg="wheat4")
frameBotones.place(x=0,y=500)

## Frames..
frameClientes=Frame(width=600,height=600,bg="#949992")

fondoClien=PhotoImage(file="Imagenes/pajarito.png")
fondoClientes=Label(frameClientes,image=fondoClien)
fondoClientes.place(x=0,y=0)

frameProveedores=Frame(width=600,height=600,bg="cadetblue4")
fondoProv=PhotoImage(file="Imagenes/pez.png")
fondoProveedores=Label(frameProveedores,image=fondoProv)
fondoProveedores.place(x=0,y=0)
frameCompra=Frame(width=600,height=600,bg="black")
frameVenta=Frame(width=600,height=600,bg="orange")
frameArticulos=Frame(width=600,height=600,bg="cadetblue4")

artIm=PhotoImage(file="Imagenes/articulos.png")
arti=Label(frameArticulos,image=artIm)
arti.place(x=0,y=0)


def sonido ():
    pygame.mixer.pre_init(44100, -16, 1024)
    pygame.init()
    pygame.mixer.get_init()
    pygame.mixer.music.load('sonido/botonsonido.mp3')
    pygame.mixer.music.play(1)
    pygame.mixer.music.rewind()
    pygame.init()

def cerrarFrames():
    frameClientes.place_forget()
    frameProveedores.place_forget()
    frameCompra.place_forget()
    frameVenta.place_forget()
    frameArticulos.place_forget()

def volver1():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    pygame.mixer.pre_init(44100, -16, 1024)
    pygame.init()
    pygame.mixer.get_init()
    pygame.mixer.music.load('sonido/botonsonido.mp3')
    pygame.mixer.music.play(1)
    pygame.mixer.music.rewind()
    pygame.init()
    borrarEntry()

botonVolver=Button(frameClientes,text="Volver",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=volver1)
botonVolver.place(x=10,y=550)

def volver2():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    sonido()
    

botonVolver2=Button(frameProveedores,text="Volver",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=volver2)
botonVolver2.place(x=10,y=550)
def volver3():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    sonido()

botonVolver3=Button(frameCompra,text="Volver",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=volver3)
botonVolver3.place(x=10,y=550)

def volver4():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    sonido()
botonVolver4=Button(frameVenta,text="Volver",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=volver4)
botonVolver4.place(x=10,y=550)

def volver5():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    sonido()

botonVolver5=Button(frameArticulos,text="Volver",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=volver5)
botonVolver5.place(x=10,y=550)

def borrarEntryCliente():
    entryClientesRazon.delete(0,END)
    entryClientesCuit.delete(0,END)
    entryClientesDireccion.delete(0,END)
    entryClientesLocalidad.delete(0,END)        
    entryClientesProvincia.delete(0,END)
    entryClientesCodigo.delete(0,END)
    entryClientesTelefono.delete(0,END)
    entryClientesIva.delete(0,END)


#Botones
def cliente():
    cerrarFrames()
    frameClientes.place(x=0,y=0)
    sonido()

botonCliente=Button(frameBotones,text="Clientes",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=cliente)
botonCliente.place(x=10,y=35)

def efecto(evento):
    botonCliente.config(bg="#FF9F01",fg="white")
botonCliente.bind("<Enter>",efecto)
def sacar(evento):
    botonCliente.config(bg="white",fg="black")
botonCliente.bind("<Leave>",sacar)


def proveedor():
    cerrarFrames()
    frameProveedores.place(x=0,y=0)
    sonido()
    
botonProveedores=Button(frameBotones,text="Proveedores",font=("Calibri",15,"bold italic"),width=10,relief="flat",command=proveedor)
botonProveedores.place(x=105,y=35)

def efecto(evento):
    botonProveedores.config(bg="#FF9F01",fg="white")
botonProveedores.bind("<Enter>",efecto)
def sacar(evento):
    botonProveedores.config(bg="white",fg="black")
botonProveedores.bind("<Leave>",sacar)


def compra():
    cerrarFrames()
    sonido()
    fecha = date.today()
    hora = datetime.now()
    fechaActual = fecha.strftime("%d-%m-%Y")
    #horaExacta = f"{hora.hour}{hora.minute}{hora.second}"
    #fechaHora = fecha.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")
    ventana = Tk()
    ventana.title("Sistema Compra")
    ventana.geometry("600x600")
    ventana.resizable(0,0)
    ventana.config(bg="gray22")
    fuente = {'font':("Calibri",15)}
    colorFrame={'bg':'#7B241C'}
    #fon=PhotoImage(file="Imagenes/imas.png")
    #fona=Label(ventana,image=fon)
    #fona.place(x=0,y=0)
    estiloEntrada={'bg':'#A93226','fg':'snow','padx':'20','pady':'10'}
    extra={'padx':'20','pady':'10'}
    estiloBoton = {'bg':'#F1948A','fg':'white','relief':'flat','bd':'5','font':'("Calibri",15)'}
    frameBotones = Frame(ventana,**colorFrame)
    frameBotones.pack(side=BOTTOM,fill=X)
    
    frameListadoCompra = Frame(ventana,**colorFrame)
    frameListadoCompra.pack(side=LEFT,fill=BOTH,expand=1)

    #ListadoCompra
    labelCompra = Label(frameListadoCompra,**estiloEntrada,**fuente,text="Listado de Compra")
    labelCompra.pack(fill=X)
    tablaCompra = ttk.Treeview(frameListadoCompra)
    tablaCompra.pack(fill=BOTH,padx=20,pady=10)
    tablaCompra["columns"] =("detalle","precio","cantidad","subtotal","iva","total")
    tablaCompra.column("#0",width=50,stretch=0)
    tablaCompra.column("detalle",width=80,)
    tablaCompra.column("precio",width=50)
    tablaCompra.column("cantidad",width=50)
    tablaCompra.column("subtotal",width=50)
    tablaCompra.column("iva",width=50)
    tablaCompra.column("total",width=50)
    
    tablaCompra.heading("#0",text="Código")
    tablaCompra.heading("detalle",text="Detalle")
    tablaCompra.heading("precio",text="Precio")
    tablaCompra.heading("cantidad",text="Cantidad")
    tablaCompra.heading("subtotal",text="Subtotal")
    tablaCompra.heading("iva",text="IVA")
    tablaCompra.heading("total",text="Total")
    #Agregar articulo
    def agregarArticulo():
        global ventanaAgregar
        def cerrarTop():
            global ventanaAgregar
            ventanaAgregar.destroy()
            ventanaAgregar = None
        if ventanaAgregar == None:
            ventanaAgregar = Toplevel()
            ventanaAgregar.geometry("600x700")
            ventanaAgregar.title("Agregar articulo")

            frameArticulos = Frame(ventanaAgregar,**colorFrame)
            frameArticulos.pack(side=LEFT,fill=BOTH,expand=1)
            frameBuscador = Frame(frameArticulos,**colorFrame)
            frameBuscador.pack(fill=X)
            frameListado = Frame(frameArticulos,**colorFrame)
            frameListado.pack(fill=BOTH)
            frameNuevoArticulo = Frame(frameArticulos,**colorFrame)
            frameInfoArticulo = Frame(frameArticulos,**colorFrame)
            frameInfoArticulo.pack(fill=BOTH)
            #NuevoLabel
            labelNuevo = Label(frameNuevoArticulo,text="Nuevo Artículo",**fuente,**estiloEntrada)
            labelNuevo.pack()
            frameEntry = Frame(frameNuevoArticulo,**colorFrame)
            frameEntry.pack(fill=BOTH,expand=1)
            frameBotonesNuevoArticulo= Frame(frameNuevoArticulo,**colorFrame)
            frameBotonesNuevoArticulo.pack(side=BOTTOM,fill=X,expand=1)
            
            #Buscador
            labelBuscador = Label(frameBuscador,**estiloEntrada,**fuente,text="Busqueda")
            labelBuscador.pack(side=LEFT,anchor=W)
            entryBuscador = Entry(frameBuscador,**fuente)
            entryBuscador.pack(side=LEFT,fill=X,anchor=W,pady=20,padx=10)
            #Listado
            tablaArticulos = ttk.Treeview(frameListado)
            tablaArticulos.pack(fill=BOTH,padx=20,pady=10)
            tablaArticulos["columns"] =("Marca","Modelo")
            tablaArticulos.column("#0",width=50,stretch=0)
            tablaArticulos.column("Marca",width=80)
            tablaArticulos.column("Modelo",width=80)
            tablaArticulos.heading("#0",text="Código")
            tablaArticulos.heading("Marca",text="Marca")
            tablaArticulos.heading("Modelo",text="Modelo")
            #carga tabla desde base
            conexion=sqlite3.connect("base.db")
            tabla=conexion.cursor()
            sql= "SELECT * FROM stock"
            tabla.execute(sql)
            listadoArticulos = tabla.fetchall()
            tabla.close()
            conexion.close()
            for dato in listadoArticulos:
                
                tablaArticulos.insert("",END,text=dato[0],values=(dato[1],dato[2]))

            def infoArticulo(evento):
                 
                index= tablaArticulos.item(tablaArticulos.selection())['text']
                detalles=tablaArticulos.item(tablaArticulos.selection())['values']
                auxDetalles=f"{detalles[0]} {detalles[1]}"
                entryCodigo.config(state="normal")
                entryDetalle.config(state="normal")
                entryCodigo.delete(0,END)
                entryCodigo.insert(END,index)
                entryDetalle.delete(0,END)
                entryDetalle.insert(END,auxDetalles)
                entryCantidad.delete(0,END)
                entryPrecio.delete(0,END)
                entryIva.delete(0,END)
                entryCodigo.config(state="readonly")
                entryDetalle.config(state="readonly")
            tablaArticulos.bind("<<TreeviewSelect>>",infoArticulo)
            #EntryArticulo
            labelCodigo = Label(frameInfoArticulo,text="Código",**fuente,**colorFrame,**extra)
            entryCodigo = Entry(frameInfoArticulo,**fuente,state="readonly")
            labelDetalle = Label(frameInfoArticulo,text="Detalle",**fuente,**colorFrame,**extra)
            entryDetalle = Entry(frameInfoArticulo,**fuente,state="readonly")
            labelCantidad = Label(frameInfoArticulo,text="Cantidad",**fuente,**colorFrame,**extra)
            entryCantidad = Entry(frameInfoArticulo,**fuente)
            labelPrecio = Label(frameInfoArticulo,text="Precio",**fuente,**colorFrame,**extra)
            entryPrecio = Entry(frameInfoArticulo,**fuente)
            labelIva = Label(frameInfoArticulo,text="IVA",**fuente,**colorFrame,**extra)
            entryIva = Entry(frameInfoArticulo,**fuente)
            labelCodigo.grid(row=0,column=0,sticky=W)
            entryCodigo.grid(row=0,column=1,sticky=W)
            labelDetalle.grid(row=1,column=0,sticky=W)
            entryDetalle.grid(row=1,column=1,sticky=W)
            labelCantidad.grid(row=2,column=0,sticky=W)
            entryCantidad.grid(row=2,column=1,sticky=W)
            labelPrecio.grid(row=3,column=0,sticky=W)
            entryPrecio.grid(row=3,column=1,sticky=W)
            labelIva.grid(row=4,column=0,sticky=W)
            entryIva.grid(row=4,column=1,sticky=W)

            #EntrysArticuloNuevo crear ARTICULOO!!!!!!!!!!!!!!!!!!!!!!!

            
            labelMarca = Label(frameEntry,text="Marca",**fuente,**estiloEntrada)
            entryMarca = Entry(frameEntry,**fuente)
            labelModelo = Label(frameEntry,text="Modelo",**fuente,**estiloEntrada)
            entryModelo = Entry(frameEntry,**fuente)
            labelCategoria = Label(frameEntry,text="Categoria",**fuente,**estiloEntrada)
            entryCategoria = Entry(frameEntry,**fuente)
            labelMarca.grid(row=0,column=0,sticky=W)
            labelModelo.grid(row=1,column=0,sticky=W)
            labelCategoria.grid(row=2,column=0,sticky=W)
            entryMarca.grid(row=0,column=1)
            entryModelo.grid(row=1,column=1)
            entryCategoria.grid(row=2,column=1)

            labelStock = Label(frameEntry,text="Stock",**fuente,**estiloEntrada)
            entryStock = Entry(frameEntry,**fuente)
            labelCosto = Label(frameEntry,text="Precio Costo",**fuente,**estiloEntrada)
            entryCosto = Entry(frameEntry,**fuente)
            labelVenta = Label(frameEntry,text="Precio Venta",**fuente,**estiloEntrada)
            entryVenta = Entry(frameEntry,**fuente)


            labelStock.grid(row=3,column=0,sticky=W)
            labelCosto.grid(row=4,column=0,sticky=W)
            labelVenta.grid(row=5,column=0,sticky=W)


            entryStock.grid(row=3,column=1)
            entryCosto.grid(row=4,column=1)
            entryVenta.grid(row=5,column=1)

            
            def guardarNuevoArticulo():
                datos=(entryMarca.get(),entryModelo.get(),entryCategoria.get(),entryStock.get(),entryCosto.get(),entryVenta.get())
                conexion=sqlite3.connect("base.db")
                tabla=conexion.cursor()
                sql="INSERT INTO stock (marcaArticulo,modeloArticulo,categoriaArticulo,stockArticulo,precioCosto,precioVenta)VALUES(?,?,?,?,?,?)"
                tabla.execute(sql,datos)
                conexion.commit()
                tabla.close
                messagebox.showinfo("Articulo","Se Guardo correctamente el nuevo artículo")

            botonGuardar = Button(frameBotonesNuevoArticulo,command=guardarNuevoArticulo,text="Guardar Articulo",**estiloBoton)
            botonGuardar.pack(side=RIGHT,padx=20,pady=20,ipadx=30)
                

            def volverBuscador():
                frameBuscador.pack(fill=X)
                frameListado.pack(fill=BOTH)
                frameInfoArticulo.pack(fill=BOTH)
                botonIngresarArticulo.pack(side=BOTTOM,pady=(20),ipadx=30,ipady=10)
                frameNuevoArticulo.pack_forget()            
            botonVolver = Button(frameBotonesNuevoArticulo,command=volverBuscador,text="Volver",**estiloBoton)
            botonVolver.pack(side=LEFT,padx=20,pady=20,ipadx=30)
            


            
            
            def nuevoArticulo():
                frameBuscador.pack_forget()
                frameListado.pack_forget()
                frameInfoArticulo.pack_forget()
                botonIngresarArticulo.pack_forget()
                frameNuevoArticulo.pack(fill=BOTH,expand=1)

           
                
                
                
            botonNuevoArticulo = Button(frameBuscador,command=nuevoArticulo,text="Crear articulo",**estiloBoton)
            botonNuevoArticulo.pack(side=RIGHT,ipadx=30,ipady=5,padx=(0,20))
            def ingresarArticulo():
                entryCodigo.config(state="normal")
                entryDetalle.config(state="normal")
                codigoArt = entryCodigo.get()
                detalles= entryDetalle.get()
                cantidad= entryCantidad.get()
                precioUnitario=float(entryPrecio.get())
                subtotal = int(precioUnitario) * int(cantidad)
                
                iva = entryIva.get()
                total = subtotal+float(iva)
                tablaCompra.insert("",END,text=codigoArt,values=(detalles,"$"+str(precioUnitario),cantidad,subtotal,iva,total))
                entryCodigo.config(state="readonly")
                entryDetalle.config(state="readonly")
                datos = [codigoArt,
                         precioUnitario,
                         cantidad,
                         subtotal,
                         iva,
                         total]
                listadoCompras.append(datos)
                #print(listadoCompras)
                
            botonIngresarArticulo = Button(frameArticulos,command=ingresarArticulo,text="Ingresar Articulo",**estiloBoton)
            botonIngresarArticulo.pack(side=BOTTOM,pady=(20),ipadx=30,ipady=10)

            
            ventanaAgregar.protocol("WM_DELETE_WINDOW",cerrarTop)
        
            
    botonAgregarArticulo = Button(frameListadoCompra,command=agregarArticulo,text="Agregar Articulo",**estiloBoton)
    botonAgregarArticulo.pack(ipadx=30,ipady=10)
    #Botones
    def compraArticulo():
        print("Calcular subtotal,iva,total")
        total = 0
        iva= 0
        subtotal=0
        for articulo in listadoCompras:
            total = total + articulo[5]
            iva= iva + float(articulo[4])
            subtotal= subtotal+ float(articulo[3])
        print("Guardar la compra BD ")
        fechaCompra = fecha.strftime("%d-%m-%Y")
        datos = (fechaCompra,total)
        conexion=sqlite3.connect("base.db")
        tabla = conexion.cursor()
        sqlGuardar= "INSERT INTO compras(fechaCompra,totalCompra) VALUES(?,?)"
        tabla.execute(sqlGuardar,datos)
        conexion.commit()
        sqlMax = "SELECT MAX(numeroCompra) FROM Compras"
        tabla.execute(sqlMax)
        datosBuscados = tabla.fetchall()
        ultimaCompra = datosBuscados[0][0]
        for articulo in listadoCompras:
            print("Actualizar el stock")
            cantidadNueva = int(articulo[2])
            idArticulo = (articulo[0],)
            tabla.execute("SELECT stockArticulo FROM stock WHERE idArticulo=?",idArticulo)
            stockArticulo = tabla.fetchall()
            
            nuevoStock = float(stockArticulo[0][0]) + float(cantidadNueva)
            actualizarStock = (nuevoStock,articulo[0])
            conexion=sqlite3.connect("base.db")
            tabla = conexion.cursor()
            sql= "UPDATE stock SET stockArticulo=? WHERE idArticulo=?"
            tabla.execute(sql,actualizarStock)
            conexion.commit()
            print("Guardar cada compra articulo BD")
            datosArticulos=(ultimaCompra,articulo[0],articulo[5])
            tabla.execute("INSERT INTO articulosCompras(numeroCompra,idArticulo,total) VALUES(?,?,?)",datosArticulos)
            conexion.commit()
        tabla.close()
        conexion.close()
        print("Ticket")
        fechaVenta = date.today()
        horaVenta = datetime.now()
        fechaActual2 = fechaVenta.strftime("%d-%m-%Y")
        horaActual2 = horaVenta.strftime("%H %M %S")
        nombreArchivo = f" Ticket {fechaActual2} {horaActual2}.txt"
        escribir = open(nombreArchivo,"w")
        escribir.write("BIENVENIDOS!\n")
        escribir.write("PET SHOP PATITAS\n")
        escribir.write("FECHA:"+fechaActual2)
        escribir.write("\n")
        escribir.write("HORA Venta:"+horaActual2)

        escribir.write("\n")
        escribir.write("-------------------------------------\n")
        escribir.write("Compra del dia:\n")
        for articulo in listadoCompras:
            art=f"ID Articulo:{articulo[0]}  X {articulo[2]}    ${articulo[3]} \n"
            escribir.write(art)
            #subtotal=f"{articulo[3]}"
        escribir.write("\n")
                
               
                
        
        escribir.write("SUB-TOTAL:$ "+str(subtotal))
        
        escribir.write("\n")

        #iva=f"{articulo[4]}"
        escribir.write("IVA:$ "+str(iva))

        escribir.write("\n")
                
        #total=f"{articulo[5]}"
                
        escribir.write("TOTAL:$ "+str(total))
                
        escribir.write("\n\n")
        escribir.write("CUIT: 2401112349-93\n")
        escribir.write("Av. Tucuman 342 Lujan de Cuyom Mendoza\n")
            
        escribir.write("****GRACIAS POR SU COMPRA!****\n")
        escribir.write("\n")
        escribir.write("ticket no valido como factura.")
        escribir.close()

        os.startfile(nombreArchivo,"print")
                
        

            
    botonComprar = Button(frameBotones,text="Comprar",command=compraArticulo,**estiloBoton)
    botonComprar.pack(fill=X,ipady=20)
   

botonCompra=Button(frameBotones,text="Compras",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=compra)
botonCompra.place(x=220,y=35)
def efecto(evento):
    botonCompra.config(bg="#FF9F01",fg="white")
botonCompra.bind("<Enter>",efecto)
def sacar(evento):
    botonCompra.config(bg="white",fg="black")
botonCompra.bind("<Leave>",sacar)



######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
######################################################################
listadoVentas=[]
def venta():
    cerrarFrames()
    frameVenta.place(x=0,y=0)
    sonido()
    cerrarFrames()
    sonido()
    fecha = date.today()
    hora = datetime.now()
    fechaActual = fecha.strftime("%d-%m-%Y")
    #horaExacta = f"{hora.hour}{hora.minute}{hora.second}"
    #fechaHora = fecha.strftime("%d/%m/%Y")+" "+time.strftime("%H:%M:%S")
    ventana = Tk()
    ventana.title("Sistema Compra")
    ventana.geometry("600x600")
    ventana.resizable(0,0)
    ventana.config(bg="gray22")
    fuente = {'font':("Calibri",15)}
    colorFrame={'bg':'#7B241C','padx':'20','pady':'10'}
    #fon=PhotoImage(file="Imagenes/imas.png")
    #fona=Label(ventana,image=fon)
    #fona.place(x=0,y=0)
    estiloEntrada={'bg':'#A93226','fg':'snow','padx':'20','pady':'10'}
    extra={'padx':'20','pady':'10'}
    estiloBoton = {'bg':'#F1948A','fg':'white','relief':'flat','bd':'5','font':'("Calibri",15)'}
    frameBotones = Frame(ventana,**colorFrame)
    frameBotones.pack(side=BOTTOM,fill=X)

    
    




    
    
    frameListadoCompra = Frame(ventana,**colorFrame)
    frameListadoCompra.pack(side=LEFT,fill=BOTH,expand=1)

    #ListadoCompra
    labelVenta = Label(frameListadoCompra,**estiloEntrada,**fuente,text="Listado de Venta")
    labelVenta.pack(fill=X)
    tablaVenta = ttk.Treeview(frameListadoCompra)
    tablaVenta.pack(fill=BOTH,padx=20,pady=10)
    tablaVenta["columns"] =("detalle","precio","cantidad","subtotal","iva","total")
    tablaVenta.column("#0",width=50,stretch=0)
    tablaVenta.column("detalle",width=80,)
    tablaVenta.column("precio",width=50)
    tablaVenta.column("cantidad",width=50)
    tablaVenta.column("subtotal",width=50)
    tablaVenta.column("iva",width=50)
    tablaVenta.column("total",width=50)
    
    tablaVenta.heading("#0",text="Código")
    tablaVenta.heading("detalle",text="Detalle")
    tablaVenta.heading("precio",text="Precio")
    tablaVenta.heading("cantidad",text="Cantidad")
    tablaVenta.heading("subtotal",text="Subtotal")
    tablaVenta.heading("iva",text="IVA")
    tablaVenta.heading("total",text="Total")
    #Agregar articulo
    def agregarArticulo():
        global ventanaAgregar
        def cerrarTop():
            global ventanaAgregar
            ventanaAgregar.destroy()
            ventanaAgregar = None
        if ventanaAgregar == None:
            ventanaAgregar = Toplevel()
            ventanaAgregar.geometry("600x700")
            ventanaAgregar.title("Agregar articulo")

            
            frameArticulos = Frame(ventanaAgregar,**colorFrame)
            frameArticulos.pack(side=LEFT,fill=BOTH,expand=1)
            frameBuscador = Frame(frameArticulos,**colorFrame)
            frameBuscador.pack(fill=X)
            frameListado = Frame(frameArticulos,**colorFrame)
            frameListado.pack(fill=BOTH)
            frameNuevoArticulo = Frame(frameArticulos,**colorFrame)
            frameInfoArticulo = Frame(frameArticulos,**colorFrame)
            frameInfoArticulo.pack(fill=BOTH)
            #NuevoLabel
            labelNuevo = Label(frameNuevoArticulo,text="Nuevo Artículo",**fuente,**estiloEntrada)
            labelNuevo.pack()
            frameEntry = Frame(frameNuevoArticulo,**colorFrame)
            frameEntry.pack(fill=BOTH,expand=1)
            frameBotonesNuevoArticulo= Frame(frameNuevoArticulo,**colorFrame)
            frameBotonesNuevoArticulo.pack(side=BOTTOM,fill=X,expand=1)
            
            #Buscador
            labelBuscador = Label(frameBuscador,**estiloEntrada,**fuente,text="Busqueda")
            labelBuscador.pack(side=LEFT,anchor=W)
            entryBuscador = Entry(frameBuscador,**fuente)
            entryBuscador.pack(side=LEFT,fill=X,anchor=W,pady=20,padx=10)
            #Listado
            tablaArticulos = ttk.Treeview(frameListado)
            tablaArticulos.pack(fill=BOTH,padx=20,pady=10)
            tablaArticulos["columns"] =("Marca","Modelo","Precio")
            tablaArticulos.column("#0",width=50,stretch=0)
            tablaArticulos.column("Marca",width=80)
            tablaArticulos.column("Modelo",width=80)
            tablaArticulos.column("Precio",width=80)
            tablaArticulos.heading("#0",text="Código")
            tablaArticulos.heading("Marca",text="Marca")
            tablaArticulos.heading("Modelo",text="Modelo")
            tablaArticulos.heading("Precio",text="Precio")
            #carga tabla desde base
            conexion=sqlite3.connect("base.db")
            tabla=conexion.cursor()
            sql= "SELECT * FROM stock"
            tabla.execute(sql)
            listadoArticulos = tabla.fetchall()
            tabla.close()
            conexion.close()
            for dato in listadoArticulos:
                tablaArticulos.insert("",END,text=dato[0],values=(dato[1],dato[2],dato[6]))
            def infoArticulo(evento):
                index= tablaArticulos.item(tablaArticulos.selection())['text']
                detalles=tablaArticulos.item(tablaArticulos.selection())['values']
                auxDetalles=f"{detalles[0]} {detalles[1]}"
                precioVenta = detalles[2]
                entryCodigo.config(state="normal")
                entryDetalle.config(state="normal")
                entryPrecio.config(state="normal")
                entryCodigo.delete(0,END)
                entryCodigo.insert(END,index)
                entryDetalle.delete(0,END)
                entryDetalle.insert(END,auxDetalles)
                entryPrecio.delete(0,END)
                entryPrecio.insert(END,precioVenta)
                entryCantidad.delete(0,END)
                entryCodigo.config(state="readonly")
                entryDetalle.config(state="readonly")
                entryPrecio.config(state="readonly")
            tablaArticulos.bind("<<TreeviewSelect>>",infoArticulo)
            #EntryArticulo
            labelCodigo = Label(frameInfoArticulo,text="Código",**fuente,**colorFrame)
            entryCodigo = Entry(frameInfoArticulo,**fuente,state="readonly")
            labelDetalle = Label(frameInfoArticulo,text="Detalle",**fuente,**colorFrame)
            entryDetalle = Entry(frameInfoArticulo,**fuente,state="readonly")
            labelCantidad = Label(frameInfoArticulo,text="Cantidad",**fuente,**colorFrame)
            entryCantidad = Entry(frameInfoArticulo,**fuente)
            labelPrecio = Label(frameInfoArticulo,text="Precio",**fuente,**colorFrame)
            entryPrecio = Entry(frameInfoArticulo,**fuente,state="readonly")
            labelIva = Label(frameInfoArticulo,text="IVA",**fuente,**colorFrame)
            entryIva = Entry(frameInfoArticulo,**fuente)
            labelCodigo.grid(row=0,column=0,sticky=W)
            entryCodigo.grid(row=0,column=1,sticky=W)
            labelDetalle.grid(row=1,column=0,sticky=W)
            entryDetalle.grid(row=1,column=1,sticky=W)
            labelPrecio.grid(row=2,column=0,sticky=W)
            entryPrecio.grid(row=2,column=1,sticky=W)
            labelCantidad.grid(row=3,column=0,sticky=W)
            entryCantidad.grid(row=3,column=1,sticky=W)
            #EntrysArticuloNuevo
            labelMarca = Label(frameEntry,text="Marca",**fuente,**estiloEntrada)
            entryMarca = Entry(frameEntry,**fuente)
            labelModelo = Label(frameEntry,text="Modelo",**fuente,**estiloEntrada)
            entryModelo = Entry(frameEntry,**fuente)
            labelCategoria = Label(frameEntry,text="Categoria",**fuente,**estiloEntrada)
            entryCategoria = Entry(frameEntry,**fuente)
            labelMarca.grid(row=0,column=0,sticky=W)
            labelModelo.grid(row=1,column=0,sticky=W)
            labelCategoria.grid(row=2,column=0,sticky=W)
            entryMarca.grid(row=0,column=1)
            entryModelo.grid(row=1,column=1)
            entryCategoria.grid(row=2,column=1)
             #EntrysArticuloNuevo
            def volverBuscador():
                frameBuscador.pack(fill=X)
                frameListado.pack(fill=BOTH)
                frameInfoArticulo.pack(fill=BOTH)
                botonIngresarArticulo.pack(side=BOTTOM,pady=(20),ipadx=30,ipady=10)
                frameNuevoArticulo.pack_forget()            
            botonVolver = Button(frameBotonesNuevoArticulo,command=volverBuscador,text="Volver",**estiloBoton)
            botonVolver.pack(side=LEFT,padx=20,pady=20,ipadx=30)
            def guardarNuevoArticulo():
                pass
            botonGuardar = Button(frameBotonesNuevoArticulo,command=guardarNuevoArticulo,text="Guardar",**estiloBoton)
            botonGuardar.pack(side=RIGHT,padx=20,pady=20,ipadx=30)
            def nuevoArticulo():
                frameBuscador.pack_forget()
                frameListado.pack_forget()
                frameInfoArticulo.pack_forget()
                botonIngresarArticulo.pack_forget()
                frameNuevoArticulo.pack(fill=BOTH,expand=1)
            botonNuevoArticulo = Button(frameBuscador,command=nuevoArticulo,text="Crear articulo",**estiloBoton)
            botonNuevoArticulo.pack(side=RIGHT,ipadx=30,ipady=5,padx=(0,20))
            def ingresarArticulo():
                entryCodigo.config(state="normal")
                entryDetalle.config(state="normal")
                codigoArt = entryCodigo.get()
                detalles= entryDetalle.get()
                cantidad= entryCantidad.get()
                precioVenta=entryPrecio.get()
                subtotal = float(entryPrecio.get()) * float(cantidad)
                iva = subtotal * 0.21
                total = subtotal+iva
                tablaVenta.insert("",END,text=codigoArt,values=(detalles,"$"+precioVenta,cantidad,subtotal,iva,total))
                entryCodigo.config(state="readonly")
                entryDetalle.config(state="readonly")
                datos = [codigoArt,
                         precioVenta,
                         cantidad,
                         subtotal,
                         iva,
                         total]
                listadoVentas.append(datos)
                print(listadoVentas)
                
            botonIngresarArticulo = Button(frameArticulos,command=ingresarArticulo,text="Ingresar Articulo",**estiloBoton)
            botonIngresarArticulo.pack(side=BOTTOM,pady=(20),ipadx=30,ipady=10)

            
            ventanaAgregar.protocol("WM_DELETE_WINDOW",cerrarTop)
        
            
    botonAgregarArticulo = Button(frameListadoCompra,command=agregarArticulo,text="Agregar Articulo",**estiloBoton)
    botonAgregarArticulo.pack(ipadx=30,ipady=10)
    #Botones
    def venderArticulo():
        print("Calcular subtotal,iva,total")
        total = 0
        iva = 0
        subtotal= 0
        for articulo in listadoVentas:
            subtotal = subtotal + articulo[3]
            total = total + articulo[5]
            iva = iva + float(articulo[4])
        print("Guardar la compra BD ")
        fechaVenta = fecha.strftime("%d-%m-%Y")
        datos = (fechaVenta,subtotal,iva,total)
        conexion=sqlite3.connect("base.db")
        tabla = conexion.cursor()
        sqlGuardar= "INSERT INTO ventas(fechaVenta,subtotalVenta,ivaVenta,totalVenta) VALUES(?,?,?,?)"
        tabla.execute(sqlGuardar,datos)
        conexion.commit()
        sqlMax = "SELECT MAX(numeroVenta) FROM Ventas"
        tabla.execute(sqlMax)
        datosBuscados = tabla.fetchall()
        ultimaVenta = datosBuscados[0][0]
        for articulo in listadoVentas:
            print("Actualizar el stock")
            cantidadNueva = int(articulo[2])
            idArticulo = (articulo[0],)
            tabla.execute("SELECT stockArticulo FROM stock WHERE idArticulo=?",idArticulo)
            stockArticulo = tabla.fetchall()
            nuevoStock = float(stockArticulo[0][0]) - float(cantidadNueva)
            actualizarStock = (nuevoStock,articulo[0])
            sql= "UPDATE stock SET stockArticulo=? WHERE idArticulo=?"
            tabla.execute(sql,actualizarStock)
            conexion.commit()
            print("Guardar cada venta articulo BD")
            datosArticulos=(ultimaVenta,articulo[0],articulo[2],articulo[3],articulo[4],articulo[5])
            tabla.execute("INSERT INTO articuloVentas(numeroVenta,codigoArticulo,cantidadArticulo,subtotalArticulo,ivaArticulo,totalArticulo) VALUES(?,?,?,?,?,?)",datosArticulos)
            conexion.commit()
        tabla.close()
        conexion.close()
        print("Ticket")
        

        fechaVenta = date.today()
        horaVenta = datetime.now()
        fechaActual2 = fechaVenta.strftime("%d-%m-%Y")
        horaActual2 = horaVenta.strftime("%H %M %S")
        nombreArchivo = f"Ticket {fechaActual2} {horaActual2}.txt"
        escribir = open(nombreArchivo,"w")
        escribir.write("BIENVENIDOS!\n")
        escribir.write("PET SHOP PATITAS\n")
        escribir.write("FECHA:"+fechaActual2)
        escribir.write("\n")
        escribir.write("HORA Venta:"+horaActual2)

        escribir.write("\n")
        escribir.write("-------------------------------------\n")
        escribir.write("Compra del dia:\n")
        for articulo in listadoVentas:
            
            art=f"ID Articulo:{articulo[0]}   X  {articulo[2]}  ${articulo[3]}\n"
            escribir.write(art)
            
        escribir.write("\n -------------------------")

        
        
        escribir.write("SUB-TOTAL:  $"+ str(subtotal))
        escribir.write("\n")

            
        escribir.write("IVA:   $"+str(iva))

        escribir.write("\n")
            
            
            
        escribir.write("TOTAL:    $"+str(total))
               
                
        escribir.write("\n\n")
        escribir.write("CUIT: 2401112349-93\n")
        escribir.write("Av. Tucuman 342 Lujan de Cuyom Mendoza\n")
            
        escribir.write("****GRACIAS POR SU COMPRA!****\n")
        escribir.write("\n")
        escribir.write("ticket no valido como factura.")
        
                

            
        escribir.close()

        os.startfile(nombreArchivo,"print")
            
        

            
    botonVender = Button(frameBotones,text="Vender",command=venderArticulo,**estiloBoton)
    botonVender.pack(fill=X,ipady=20)
    """
    def compraPrueba():
        conexion= conectar()
        tabla = conexion.cursor()
        buscarIdArticulo= "SELECT MAX(idArticulo) FROM stock"
        tabla.execute(buscarIdArticulo)
        maxNCompra = tabla.fetchall()
        print(maxNCompra)
        tabla.close()
        conexion.close()
    botonPrueba = Button(frameBotones,text="Prueba",command=compraPrueba,**fuente,bg="#3D83A3",fg="snow",relief=FLAT,bd=0)
    botonPrueba.pack(fill=X,ipady=20)
    """
    
botonVenta=Button(frameBotones,text="Ventas",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=venta)
botonVenta.place(x=316,y=35)

def efecto(evento):
    botonVenta.config(bg="#FF9F01",fg="white")
botonVenta.bind("<Enter>",efecto)
def sacar(evento):
    botonVenta.config(bg="white",fg="black")
botonVenta.bind("<Leave>",sacar)


def articulos():
    cerrarFrames()
    frameArticulos.place(x=0,y=0)
    sonido()

    
botonArticulos=Button(frameBotones,text="Articulos",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=articulos)
botonArticulos.place(x=412,y=35)

def efecto(evento):
    botonArticulos.config(bg="#FF9F01",fg="white")
botonArticulos.bind("<Enter>",efecto)
def sacar(evento):
    botonArticulos.config(bg="white",fg="black")
botonArticulos.bind("<Leave>",sacar)


def inicio1():
    cerrarFrames()
    frameIngresandoPaginaPrincipal.place_forget()
    miFrame1.place(x=0,y=0)
    sonido()
botonInicio=Button(frameBotones,text="Inicio",font=("Calibri",15,"bold italic"),width=8,relief="flat",command=inicio1)
botonInicio.place(x=508,y=35)

def efecto(evento):
    botonInicio.config(bg="#FE5100",fg="white")
botonInicio.bind("<Enter>",efecto)
def sacar(evento):
    botonInicio.config(bg="white",fg="black")
botonInicio.bind("<Leave>",sacar)




imagenFondo1=PhotoImage(file="imagenes/perro.png")
imagen1=Label(frameIngresandoPaginaPrincipal,image=imagenFondo1)
imagen1.place(x=-80,y=100)

imagenFondo=PhotoImage(file="imagenes/pet.png")
imagen=Label(miFrame1,image=imagenFondo)
imagen.place(x=0,y=0)
tituloPet=Label(miFrame1,text="Pet Shop 'PATITAS'",font=("Algerian",40,"bold italic"),bg="yellow")
tituloPet.place(x=20,y=20)
titulo=Label(frameIngresandoPaginaPrincipal,text="",font=("calibri",40,"bold italic"),bg="wheat3")
titulo.place(x=200,y=20)


def ingreso():

    
    miFrame1.place_forget()
    
    frameIngresandoPaginaPrincipal.place(x=0,y=0)
    pygame.mixer.pre_init(44100, -16, 1024)
    pygame.init()
    pygame.mixer.get_init()
    pygame.mixer.music.load('sonido/iniciosonido.mp3')
    pygame.mixer.music.play(1)
    pygame.mixer.music.rewind()
    pygame.init()
    frameIngresandoPaginaPrincipal.config(width=800,height=800)
    titulo.after(1000,lambda:titulo.config(text="P"))
    titulo.after(2000,lambda:titulo.config(text="PE"))
    titulo.after(3000,lambda:titulo.config(text="PET"))
    titulo.after(4000,lambda:titulo.config(text="PET S"))
    titulo.after(5000,lambda:titulo.config(text="PET SH"))
    titulo.after(6000,lambda:titulo.config(text="PET SHO"))
    titulo.after(7000,lambda:titulo.config(text="PET SHOP"))
    titulo.after(8000,lambda:titulo.config(text="PET SHOP!"))
       

botonIngreso=Button(miFrame1,text="Ingresar",font=("Calibri",15,"bold italic"),width=10,relief="groove",command=ingreso)
botonIngreso.place(x=480,y=550)

def efecto(evento):
    botonIngreso.config(bg="#FF9F01",fg="white")
    
botonIngreso.bind("<Enter>",efecto)
    
    
def sacar(evento):
    
    botonIngreso.config(bg="white",fg="black")
botonIngreso.bind("<Leave>",sacar)



def cerrarSesion():
    
    sonido()
    resp = messagebox.askquestion('Cerrar', 'Desea Cerrar SESION?')
    if resp == 'yes': 
            
        frameClientes.place_forget()
        frameProveedores.place_forget()
        frameCompra.place_forget()
        frameVenta.place_forget()
        frameArticulos.place_forget()
        raiz.destroy()
        
cerrarSesion=Button(miFrame1,text="Cerrar Sesión",font=("Calibri",15,"bold italic"),width=11,relief="groove",command=cerrarSesion)
cerrarSesion.place(x=12,y=551)


def efecto(evento):
    cerrarSesion.config(bg="#FF9F01",fg="white")
cerrarSesion.bind("<Enter>",efecto)
def sacar(evento):
    cerrarSesion.config(bg="white",fg="black")
cerrarSesion.bind("<Leave>",sacar)

#by=Label(miFrame1,text="by Ahumada Sebastian.",font=("calibri",15,"bold italic"),bg="yellow")
#by.place(x=30,y=540)

#what=Label(miFrame1,text="Wahtsapp: 2615928607",font=("calibri",15,"bold italic"),bg="yellow")
#what.place(x=30,y=570)

labelhora=Label(frameIngresandoPaginaPrincipal,text="",font=("calibri",15,"bold italic"),bg="wheat3",fg="black")
labelhora.place(x=520,y=5)
labelfecha=Label(frameIngresandoPaginaPrincipal,text="",font=("calibri",15,"bold italic"),bg="wheat3",fg="black")
labelfecha.place(x=5,y=5)

def reloj():

    time1=""
    time2=time.strftime("%H:%M:%S")
    if(time1 != time2):
        labelhora.config(text=time2)
        labelhora.after(500,reloj)
reloj()

def fecha():

    time1=""
    time2=time.strftime("%d/%m/%Y")
    if(time1 != time2):
        labelfecha.config(text=time2)
        labelfecha.after(500,reloj)
fecha()




##comienzo a desarrollar el frame clientes

tituloClientesLabel=Label(frameClientes,text="Clientes",font=("calibri",30,"bold italic"),bg="#949992")
tituloClientesLabel.place(x=250,y=5)

idClientesLabel=Label(frameClientes,text="Id Cliente",font=("calibri",15,"bold italic"),bg="#949992")
idClientesLabel.place(x=20,y=80)
razonSocialClientesLabel=Label(frameClientes,text="Razon Social",font=("calibri",15,"bold italic"),bg="#949992")
razonSocialClientesLabel.place(x=20,y=120)
cuitClientesLabel=Label(frameClientes,text="Cuit/Cuil",font=("calibri",15,"bold italic"),bg="#949992")
cuitClientesLabel.place(x=20,y=160)
direccionClientesLabel=Label(frameClientes,text="Direccion",font=("calibri",15,"bold italic"),bg="#949992")
direccionClientesLabel.place(x=20,y=200)
localidadClientesLabel=Label(frameClientes,text="Localidad",font=("calibri",15,"bold italic"),bg="#949992")
localidadClientesLabel.place(x=20,y=240)
provinciaClientesLabel=Label(frameClientes,text="Provincia",font=("calibri",15,"bold italic"),bg="#949992")
provinciaClientesLabel.place(x=20,y=280)
codigoPClientesLabel=Label(frameClientes,text="Codigo Postal",font=("calibri",15,"bold italic"),bg="#949992")
codigoPClientesLabel.place(x=20,y=320)
telefonoClientesLabel=Label(frameClientes,text="Teléfono",font=("calibri",15,"bold italic"),bg="#949992")
telefonoClientesLabel.place(x=20,y=360)
ivaClientesLabel=Label(frameClientes,text="Iva",font=("calibri",15,"bold italic"),bg="#949992")
ivaClientesLabel.place(x=20,y=400)

########################### ENTRY  CLIENTES    ###########################################

def validarLetras(datos):
    for letra in datos:
         if(ord(letra) != 32):
             if(letra.isalpha() == False):
                return False
    return True


def numeros(datos):
    for numero in datos:
        if(ord(numero)!=46):
            if(numero.isdigit()== False):
                 return False
    return True
            
entryClientesid=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesid.place(x=170,y=83)

entryClientesRazon=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesRazon.place(x=170,y=123)
entryClientesCuit=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesCuit.place(x=170,y=163)
entryClientesDireccion=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesDireccion.place(x=170,y=203)
entryClientesLocalidad=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesLocalidad.place(x=170,y=243)
entryClientesProvincia=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesProvincia.place(x=170,y=283)
entryClientesCodigo=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesCodigo.place(x=170,y=323)
entryClientesTelefono=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesTelefono.place(x=170,y=363)
entryClientesIva=Entry(frameClientes,font=("Arial",10,"bold italic"),fg="red")
entryClientesIva.place(x=170,y=403)

####################### FUNCIONES BOTONES CLIENTES ###########################################


#####################3#######  Guardar   """""""""""###################!!!!!!!!!!!!!!!!      
def guardarCliente():
    sonido()
    datos=(entryClientesRazon.get(),entryClientesCuit.get(),entryClientesDireccion.get(),entryClientesLocalidad.get(),entryClientesProvincia.get(),entryClientesCodigo.get(),entryClientesTelefono.get(),entryClientesIva.get())
    if(datos[0]=="" or datos [1]=="" or datos [2]=="" or datos[3]=="" or datos[4]=="" or datos [5]=="" or datos[6]=="" or datos[7]=="" ):
        messagebox.showwarning("Clientes","Complete Todos los Campos para Guardar")
        
    else:
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO cliente (razonSocial,cuil,direccion,localidad,provincia,cpostal,telefono,iva) VALUES(?,?,?,?,?,?,?,?)",datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Cliente","Cliente Nuevo Guardado con Exito!!")
        entryClientesRazon.delete(0,END)
        entryClientesCuit.delete(0,END)
        entryClientesDireccion.delete(0,END)
        entryClientesLocalidad.delete(0,END)
        entryClientesProvincia.delete(0,END)
        entryClientesCodigo.delete(0,END)
        entryClientesTelefono.delete(0,END)
        entryClientesIva.delete(0,END)
           

#####################3#######  Guardar   """""""""""###################!!!!!!!!!!!!!!!!
def borrarEntry():
    
    entryClientesid.delete(0,END)
    entryClientesid.delete(0,END)
    entryClientesRazon.delete(0,END)
    entryClientesCuit.delete(0,END)
    entryClientesDireccion.delete(0,END)
    entryClientesLocalidad.delete(0,END)        
    entryClientesProvincia.delete(0,END)
    entryClientesCodigo.delete(0,END)
    entryClientesTelefono.delete(0,END)
    entryClientesIva.delete(0,END)


################################### buscar  "#######################3

 
def buscarCliente():
    sonido()
    datoid=(entryClientesRazon.get(),)
    if(entryClientesRazon.get() == ""):
        
        messagebox.showwarning("Cliente","Ingrese un nombre para buscar")
        
    else:
        #comboBuscar=ttk.Combobox(frameClientes)
        tabla=conexion.cursor()
        sql="SELECT * FROM cliente WHERE razonSocial = ?"
        tabla.execute(sql,datoid)
        conexion.commit()
        datosCliente=tabla.fetchall()
        #borrarEntryCliente()
        #messagebox.showinfo("Cliente","Resultados de la Búsqueda")
        if(len(datosCliente)>0):
            for dato in datosCliente:
                  
                    #entryClientesid.config(state="normal")
                    entryClientesid.insert(END,dato[0])
                    #entryClientesid.config(state="readonly")
                    #entryClientesRazon.insert(END,dato[1])
                    entryClientesCuit.insert(END,dato[2])
                    entryClientesDireccion.insert(END,dato[3])
                    entryClientesLocalidad.insert(END,dato[4])
                    entryClientesProvincia.insert(END,dato[5])
                    entryClientesCodigo.insert(END,dato[6])
                    entryClientesTelefono.insert(END,dato[7])
                    entryClientesIva.insert(END,dato[8])
        else:
            messagebox.showwarning("Cliente","Cliente Inexistente")
            

            """
            if (len(datosCliente)>1):
                messagebox.showinfo("Sistema","Existen varias coincidencias seleccionar el buscado")
                comboBuscar.place(x=70,y=30)                
                listadoCuit=[]
                for dato in datosCliente:
                    listadoCuit.append(dato[2])
                comboBuscar["values"]= listadoCuit

                def mostrarEntry(evento):
                    cuits=comboBuscar.get()
                    
                    for dato in datosCliente:
                         if(dato[2] == cuits):
                        
                            #entryClientesid.config(state="normal")
                            entryClientesid.insert(END,dato[0])
                            entryClientesid.config(state="readonly")
                            entryClientesRazon.insert(END,dato[1])
                            entryClientesCuit.insert(END,dato[2])
                            entryClientesDireccion.insert(END,dato[3])
                            entryClientesLocalidad.insert(END,dato[4])
                            entryClientesProvincia.insert(END,dato[5])
                            entryClientesCodigo.insert(END,dato[6])
                            entryClientesTelefono.insert(END,dato[7])
                            entryClientesIva.insert(END,dato[8])
                            
                    
            
                       
                          
                            
                               
                comboBuscar.bind("<<ComboboxSelected>>",mostrarEntry)
                    
                      
            else:
                
               
               """ 
                

        
           





#################################       MODIFICAR   ########################

def modificarCliente():
    sonido()
    if(entryClientesRazon.get()=="" or entryClientesCuit.get()=="" or entryClientesDireccion.get()=="" or entryClientesLocalidad.get()=="" or entryClientesProvincia.get()=="" or entryClientesCodigo.get()=="" or entryClientesTelefono.get()=="" or entryClientesIva.get()=="" or entryClientesid.get()==""):
         messagebox.showwarning("Cliente","Debe buscar para poder modificar")
    else:
        datosm=(entryClientesRazon.get(),entryClientesCuit.get(),entryClientesDireccion.get(),entryClientesLocalidad.get(),entryClientesProvincia.get(),entryClientesCodigo.get(),entryClientesTelefono.get(),entryClientesIva.get(),entryClientesid.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE cliente SET razonSocial=?,cuil=?,direccion=?,localidad=?,provincia=?,cpostal=?,telefono=?,iva=? WHERE id=? ",datosm)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Cliente","Modificacion Exitosa")
        
###########################  BOTON DELETE   ###########################################

def borrarCliente():
    sonido()
    conexion=sqlite3.connect("base.db")
    
    
    if(entryClientesRazon.get() == ""):
        messagebox.showwarning("Cliente","Debe buscar para poder Eliminar")
    else:
        conexion.cursor()
        datosb=(entryClientesRazon.get(),)
        tabla=conexion.cursor()
        tabla.execute("DELETE FROM cliente WHERE razonSocial=?",datosb)
        conexion.commit()
        tabla.close()

        messagebox.showinfo("Clientes","Cliente Eliminado")

    
                
        

##################              BOTONES CLIENTES    ##################



botonGuardarCliente=Button(frameClientes,text="Guardar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=guardarCliente)
botonGuardarCliente.place(x=20,y=453)

botonBuscarCliente=Button(frameClientes,text="Buscar \n x nombre",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=buscarCliente)
botonBuscarCliente.place(x=170,y=453)

botonModificarCliente=Button(frameClientes,text="Modificar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=modificarCliente)
botonModificarCliente.place(x=320,y=453)

botonEliminarCliente=Button(frameClientes,text="Eliminar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=borrarCliente)
botonEliminarCliente.place(x=480,y=453)

def borrarCliente():
    
    borrarEntry()

botonLimpiezaFrameCliente=Button(frameClientes,text="Limpiar Pantalla",font=("Calibri",13,"bold italic"),relief="ridge",width=20,height=2,command=borrarCliente,bg="crimson")
botonLimpiezaFrameCliente.place(x=380,y=340)







##############comienzo a desarrollar frame Proveedores#######################################################

tituloProveedoresLabel=Label(frameProveedores,text="Proveedores",font=("calibri",30,"bold italic"),bg="cadetblue4")
tituloProveedoresLabel.place(x=220,y=5)

idProveedoresLabel=Label(frameProveedores,text="Id Proveedor",font=("calibri",15,"bold italic"),bg="cadetblue4")
idProveedoresLabel.place(x=20,y=80)
razonProveedoresLabel=Label(frameProveedores,text="Razon Social",font=("calibri",15,"bold italic"),bg="cadetblue4")
razonProveedoresLabel.place(x=20,y=120)
cuitProveedoresLabel=Label(frameProveedores,text="Cuit/Cuil",font=("calibri",15,"bold italic"),bg="cadetblue4")
cuitProveedoresLabel.place(x=20,y=160)
direccionProveedoresLabel=Label(frameProveedores,text="Direccion",font=("calibri",15,"bold italic"),bg="cadetblue4")
direccionProveedoresLabel.place(x=20,y=200)
localidadProveedoresLabel=Label(frameProveedores,text="Localidad",font=("calibri",15,"bold italic"),bg="cadetblue4")
localidadProveedoresLabel.place(x=20,y=240)
provinciaProveedoresLabel=Label(frameProveedores,text="Provincia",font=("calibri",15,"bold italic"),bg="cadetblue4")
provinciaProveedoresLabel.place(x=20,y=280)
codigoPProveedoresLabel=Label(frameProveedores,text="Codigo Postal",font=("calibri",15,"bold italic"),bg="cadetblue4")
codigoPProveedoresLabel.place(x=20,y=320)
telefonoProveedoresLabel=Label(frameProveedores,text="Teléfono",font=("calibri",15,"bold italic"),bg="cadetblue4")
telefonoProveedoresLabel.place(x=20,y=360)
ivaProveedoresLabel=Label(frameProveedores,text="Iva",font=("calibri",15,"bold italic"),bg="cadetblue4")
ivaProveedoresLabel.place(x=20,y=400)

########################### ENTRY  PROVEEDORES    ###########################################

entryProveedoresid=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresid.place(x=170,y=83)
entryProveedoresRazon=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresRazon.place(x=170,y=123)
entryProveedoresCuit=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresCuit.place(x=170,y=163)
entryProveedoresDireccion=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresDireccion.place(x=170,y=203)
entryProveedoresLocalidad=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresLocalidad.place(x=170,y=243)
entryProveedoresProvincia=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresProvincia.place(x=170,y=283)
entryProveedoresCodigo=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresCodigo.place(x=170,y=323)
entryProveedoresTelefono=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresTelefono.place(x=170,y=363)
entryProveedoresIva=Entry(frameProveedores,font=("Arial",10,"bold italic"),fg="red")
entryProveedoresIva.place(x=170,y=403)
#########################################################funciones boton proveedores ################################3

def guardarProveedor():
    sonido()
    datos=(entryProveedoresRazon.get(),entryProveedoresCuit.get(),entryProveedoresDireccion.get(),entryProveedoresLocalidad.get(),entryProveedoresProvincia.get(),entryProveedoresCodigo.get(),entryProveedoresTelefono.get(),entryProveedoresIva.get())
    if(datos[0]=="" or datos [1]=="" or datos [2]=="" or datos[3]=="" or datos[4]=="" or datos [5]=="" or datos[6]=="" or datos[7]=="" ):
        messagebox.showwarning("Proveedores","Complete Todos los Campos para Guardar")
        
    else:
        tabla=conexion.cursor()
        tabla.execute("INSERT INTO proveedor (razonSocial,cuil,direccion,localidad,provincia,cpostal,telefono,iva) VALUES(?,?,?,?,?,?,?,?)",datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Proveedores","Proveedor Nuevo Guardado con Exito!!")
        entryProveedoresRazon.delete(0,END)
        entryProveedoresCuit.delete(0,END)
        entryProveedoresDireccion.delete(0,END)
        entryProveedoresLocalidad.delete(0,END)
        entryProveedoresProvincia.delete(0,END)
        entryProveedoresCodigo.delete(0,END)
        entryProveedoresTelefono.delete(0,END)
        entryProveedoresIva.delete(0,END)


def buscarProveedor():
    sonido()
    datoid=(entryProveedoresRazon.get(),)
    if(entryProveedoresRazon.get() == ""):
        messagebox.showinfo("Sistema","Ingrese nombre de PROVEEDOR para buscar")
    else:
        tabla=conexion.cursor()
        sql="SELECT * FROM proveedor WHERE razonSocial = ?"
        tabla.execute(sql,datoid)
        conexion.commit()
        datosProveedores=tabla.fetchall()
        tabla.close()
        
        
        for dato in datosProveedores:
            entryProveedoresid.delete(0,END)
            entryProveedoresRazon.delete(0,END)
            entryProveedoresCuit.delete(0,END)
            entryProveedoresDireccion.delete(0,END)
            entryProveedoresLocalidad.delete(0,END)        
            entryProveedoresProvincia.delete(0,END)
            entryProveedoresCodigo.delete(0,END)
            entryProveedoresTelefono.delete(0,END)
            entryProveedoresIva.delete(0,END)

           

                        
        if(len(datosProveedores)>0):
            
            entryProveedoresid.insert(END,dato[0])
            entryProveedoresRazon.insert(END,dato[1])
            entryProveedoresCuit.insert(END,dato[2])
            entryProveedoresDireccion.insert(END,dato[3])
            entryProveedoresLocalidad.insert(END,dato[4])
            entryProveedoresProvincia.insert(END,dato[5])
            entryProveedoresCodigo.insert(END,dato[6])
            entryProveedoresTelefono.insert(END,dato[7])
            entryProveedoresIva.insert(END,dato[8])
                                  
        else:
            messagebox.showwarning("Proveedor","Proveedor Inexistente")


def modificarProveedor():
    sonido()
    if(entryProveedoresRazon.get()=="" or entryProveedoresCuit.get()=="" or entryProveedoresDireccion.get()=="" or entryProveedoresLocalidad.get()=="" or entryProveedoresProvincia.get()=="" or entryProveedoresCodigo.get()=="" or entryProveedoresTelefono.get()=="" or entryProveedoresIva.get()=="" or entryProveedoresid.get()==""):
        messagebox.showwarning("Proveedores","Debe buscar para poder modificar")
    
    else:
        datosmo=(entryProveedoresRazon.get(),entryProveedoresCuit.get(),entryProveedoresDireccion.get(),entryProveedoresLocalidad.get(),entryProveedoresProvincia.get(),entryProveedoresCodigo.get(),entryProveedoresTelefono.get(),entryProveedoresIva.get(),entryProveedoresid.get())
        tabla=conexion.cursor()
        tabla.execute("UPDATE proveedor SET razonSocial=?,cuil=?,direccion=?,localidad=?,provincia=?,cpostal=?,telefono=?,iva=? WHERE id=? ",datosmo)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Proveedor","Modificacion Exitosa")


########################################################

def borrarProveedores():
    datoP=(entryProveedoresid.get(),)
    if(entryProveedoresid.get()== ""):
        messagebox.showwarning("Proveedores","Debe Buscar para poder Eliminar")
    else:
        entryProveedoresid.delete(0,END)
        entryProveedoresRazon.delete(0,END)
        entryProveedoresCuit.delete(0,END)
        entryProveedoresDireccion.delete(0,END)
        entryProveedoresLocalidad.delete(0,END)        
        entryProveedoresProvincia.delete(0,END)
        entryProveedoresCodigo.delete(0,END)
        entryProveedoresTelefono.delete(0,END)
        entryProveedoresIva.delete(0,END)

        tabla=conexion.cursor()
        sql="DELETE FROM proveedor WHERE id=?"
        tabla.execute(sql,datoP)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Proveedor","Proveedor Borrado con exito")


        

################### BOTONES PROVEEDORES##########################3
botonGuardarProveedores=Button(frameProveedores,text="Guardar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=guardarProveedor)
botonGuardarProveedores.place(x=20,y=453)

botonBuscarProveedores=Button(frameProveedores,text="Buscar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=buscarProveedor)
botonBuscarProveedores.place(x=170,y=453)

botonModificarProveedores=Button(frameProveedores,text="Modificar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=modificarProveedor)
botonModificarProveedores.place(x=320,y=453)

botonEliminarProveedores=Button(frameProveedores,text="Eliminar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=borrarProveedores)
botonEliminarProveedores.place(x=480,y=453)

def limpiarP():
        entryProveedoresid.delete(0,END)
        entryProveedoresRazon.delete(0,END)
        entryProveedoresCuit.delete(0,END)
        entryProveedoresDireccion.delete(0,END)
        entryProveedoresLocalidad.delete(0,END)        
        entryProveedoresProvincia.delete(0,END)
        entryProveedoresCodigo.delete(0,END)
        entryProveedoresTelefono.delete(0,END)
        entryProveedoresIva.delete(0,END)
    



botonListarProveedores=Button(frameProveedores,text="Borrar Pantalla",font=("Calibri",13,"bold italic"),fg="snow",relief="ridge",width=20,height=2,bg="crimson",command=limpiarP)
botonListarProveedores.place(x=380,y=340)


        
###################################### ventas   ##################################
#####################################    ARTICULOS        ########################################


tituloArticulos=Label(frameArticulos,text="Artículos",font=("calibri",30,"bold italic"),bg="cadetblue4")
tituloArticulos.place(x=220,y=5)

Articulo1=Label(frameArticulos,text="Código Artículo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo1.place(x=20,y=80)
Articulo2=Label(frameArticulos,text="Marca Artículo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo2.place(x=20,y=120)
Articulo3=Label(frameArticulos,text="Modelo Artículo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo3.place(x=20,y=160)
Articulo4=Label(frameArticulos,text="Categ. Artículo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo4.place(x=20,y=200)
Articulo5=Label(frameArticulos,text="Stock Artículo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo5.place(x=20,y=240)
Articulo6=Label(frameArticulos,text="Precio Costo",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo6.place(x=20,y=280)
Articulo7=Label(frameArticulos,text="Precio Venta",font=("calibri",15,"bold italic"),bg="cadetblue4")
Articulo7.place(x=20,y=320)

########################### ENTRY  ARTICULOS     ###########################################

entryArticulo1=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo1.place(x=170,y=83)
entryArticulo2=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo2.place(x=170,y=123)
entryArticulo3=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo3.place(x=170,y=163)
entryArticulo4=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo4.place(x=170,y=203)
entryArticulo5=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo5.place(x=170,y=243)
entryArticulo6=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo6.place(x=170,y=283)
entryArticulo7=Entry(frameArticulos,font=("Arial",10,"bold italic"),fg="#FF0074")
entryArticulo7.place(x=170,y=323)


#################$$%%&&&$%$%$%&$%&$%/%&/%%$#$%#  ACCION BOTONES VENTANA ARTICULOS   "####"#$"#$"#"#$"$#$%#$%#$"#
entryArticulo1.config(state="normal")
def nuevoArticulo():
    
    datos=(entryArticulo2.get(),entryArticulo3.get(),entryArticulo4.get(),entryArticulo5.get(),entryArticulo6.get(),entryArticulo7.get())
    if(entryArticulo2.get()=="" or entryArticulo3.get()=="" or entryArticulo4.get()=="" or entryArticulo5.get()=="" or entryArticulo6.get()=="" or entryArticulo7.get()==""):
        messagebox.showinfo("Articulos","Complete todos los campos para Guardar un nuevo articulo")
    else:
        
        entryArticulo1.delete(0,END)
        entryArticulo2.delete(0,END)
        entryArticulo3.delete(0,END)
        entryArticulo4.delete(0,END)
        entryArticulo5.delete(0,END)
        entryArticulo6.delete(0,END)
        entryArticulo7.delete(0,END)
        
        tabla=conexion.cursor()
        sql="INSERT INTO articulos (marcaArticulo,modeloArticulo,categoriaArticulo,stockArticulo,precioCosto,precioVenta) VALUES(?,?,?,?,?,?)"
        tabla.execute(sql,datos)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("Articulos","Se ingreso un NUEVO ARTICULO con exito!")

def buscarArticulo():
    dato10=(entryArticulo1.get(),)
    if(entryArticulo1.get()==""):
        messagebox.showwarning("Articulos","Ingrese el codigo para poder buscar")
    else:
        conexion=sqlite3.connect("base.db")
        tabla=conexion.cursor()
        tabla.execute("SELECT * FROM articulos WHERE codigoArticulo=?",dato10)
        conexion.commit()
        informe=tabla.fetchall()
        for dato in informe:
            entryArticulo1.delete(0,END)
            entryArticulo2.delete(0,END)
            entryArticulo3.delete(0,END)
            entryArticulo4.delete(0,END)
            entryArticulo5.delete(0,END)
            entryArticulo6.delete(0,END)
            entryArticulo7.delete(0,END)
                
            
            if(len(dato)>0):
                for dato in informe:
                    
                    entryArticulo1.insert(END,dato[0])
                    entryArticulo2.insert(END,dato[1])
                    entryArticulo3.insert(END,dato[2])
                    entryArticulo4.insert(END,dato[3])
                    entryArticulo5.insert(END,dato[4])
                    entryArticulo6.insert(END,dato[5])
                    entryArticulo7.insert(END,dato[6])
            else:
                
                 messagebox.showwarning("articulos","El articulo buscado no existe")


####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        
####################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def modificarArt():
    if(entryArticulo2.get()=="" or entryArticulo3.get()=="" or entryArticulo4.get()=="" or entryArticulo5.get()=="" or entryArticulo6.get()=="" or entryArticulo7.get()=="" or entryArticulo1.get()==""):
        messagebox.showinfo("art","debe buscar,para poder \n modificar")
    else:
        dato=(entryArticulo2.get(),entryArticulo3.get(),entryArticulo4.get(),entryArticulo5.get(),entryArticulo6.get(),entryArticulo7.get(),entryArticulo1.get(),)
        conexion=sqlite3.connect("base.db")
        tabla=conexion.cursor()
        tabla.execute("UPDATE articulos SET marcaArticulo=?,modeloArticulo=?,categoriaArticulo=?,stockArticulo=?,precioCosto=?,precioVenta=? WHERE codigoArticulo=?",dato)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("articulo","articulo modificado con exito")

def eliminarArt():
    dato=(entryArticulo1.get(),)
    if(entryArticulo2.get()=="" or entryArticulo3.get()=="" or entryArticulo4.get()=="" or entryArticulo5.get()=="" or entryArticulo6.get()=="" or entryArticulo7.get()=="" or entryArticulo1.get()==""):
        messagebox.showinfo("art","debe buscar,para poder \n Eliminar")
    else:
        conexion=sqlite3.connect("base.db")
        tabla=conexion.cursor()
        tabla.execute("DELETE FROM articulos WHERE codigoArticulo=?",dato)
        conexion.commit()
        tabla.close()
        messagebox.showinfo("articulo","articulo Eliminado")
        
        
    
    
            
            
        
        






##########################               BOTONES ARTICULOS      #######################################

botonArticulos1=Button(frameArticulos,text="Guardar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=nuevoArticulo)
botonArticulos1.place(x=20,y=453)

botonArticulos2=Button(frameArticulos,text="Modificar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=modificarArt)
botonArticulos2.place(x=170,y=453)

botonArticulos3=Button(frameArticulos,text="Eliminar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=eliminarArt)
botonArticulos3.place(x=320,y=453)

botonArticulos4=Button(frameArticulos,text="Buscar",font=("Calibri",13,"bold italic"),relief="ridge",width=10,height=2,command=buscarArticulo)
botonArticulos4.place(x=480,y=453)

def borrarE():
    
    entryArticulo1.delete(0,END)
    entryArticulo2.delete(0,END)
    entryArticulo3.delete(0,END)
    entryArticulo4.delete(0,END)
    entryArticulo5.delete(0,END)
    entryArticulo6.delete(0,END)
    entryArticulo7.delete(0,END)
    
botonArticulo=Button(frameArticulos,text="Borrar Pantalla",font=("Calibri",13,"bold italic"),relief="ridge",width=20,height=2,command=borrarE,bg="crimson")
botonArticulo.place(x=380,y=340)














"""
    datosB=(entryArticulo1.get(),)
    if(entryArticulo1.get()==""):
         messagebox.showwarning("Articulos","Ingrese el nombre del articulo que busca en el campo CODIGO del articulo")
    else:
        tabla=conexion.cursor()
        #sql="SELECT * FROM articulos WHERE marcaArticulo=?"
        tabla.execute("SELECT * FROM articulos WHERE codigoArticulo=?",datosB)
        conexion.commit()
        datosfet=tabla.fetchall()
        #tabla.close()

        for daton in datosfet():
            entryArticulo.delete(0,END)
            entryArticulo1.delete(0,END)
            entryArticulo2.delete(0,END)
            entryArticulo3.delete(0,END)
            entryArticulo4.delete(0,END)
            entryArticulo5.delete(0,END)
            entryArticulo6.delete(0,END)
            entryArticulo7.delete(0,END)
            messagebox.showinfo("Articulos","el articulo buscado es:  ",daton)
        for daton in datosfet():
            
            if(len(datosfet)>0):
                entryArticulo.insert(daton[0])
                entryArticulo1.insert(daton[1])
                entryArticulo2.insert(daton[2])
                entryArticulo3.insert(daton[3])
                entryArticulo4.insert(daton[4])
                entryArticulo5.insert(daton[5])
                entryArticulo6.insert(daton[6])
                entryArticulo7.insert(daton[7])
            else:
                messagebox.showinfo("Articulos","No existe el articulo buscado")
        
       """     
        
















raiz.mainloop()
