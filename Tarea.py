from tkinter import *
import os
def RegiDatos():
    global ventana2,Entrada11,Entrada12,Entrada13,Entrada14,Entrada21,Entrada22,Entrada23,Entrada24,Entrada31,Entrada32,Entrada33,Entrada34,Entrada41,Entrada42,Entrada43,Entrada44
    CerrarPantalla(ventana1)
    #Inicializamos la pantalla de la 1era opción del menú
    ventana2=Tk()
    ventana2.title("Registrar datos - Grupo 9")
    ventana2.geometry("720x480")
    ventana2.resizable(False, False)

    #Abrimos el fondo

    fondo2=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/megistrardatos.png')
    fondoRE = Label(image = fondo2, text = "registrardatos")
    fondoRE.place(x=0, y=0, relheight=1, relwidth=1)

    #Variable 1.1

    Entrada11=Entry(ventana2,borderwidth=0)
    Entrada11.config(font=('Helvetica',12),bg='chocolate2')
    Entrada11.place(x=145,y=90, width=110, height=27)

    #Variable 1.2

    Entrada12=Entry(ventana2,borderwidth=0)
    Entrada12.config(font=('Helvetica',12),bg='chocolate2')
    Entrada12.place(x=145,y=147, width=110, height=27)

    #Variable 1.3

    Entrada13=Entry(ventana2,borderwidth=0)
    Entrada13.config(font=('Helvetica',12),bg='chocolate2')
    Entrada13.place(x=145,y=207, width=110, height=27)

    #Variable 1.4

    Entrada14=Entry(ventana2,borderwidth=0)
    Entrada14.config(font=('Helvetica',12),bg='chocolate2')
    Entrada14.place(x=145,y=267, width=110, height=27)

    #Variable 2.1 340 540

    Entrada21=Entry(ventana2,borderwidth=0)
    Entrada21.config(font=('Helvetica',12),bg='chocolate2')
    Entrada21.place(x=145,y=325, width=110, height=27)

   #Variable 2.2 

    Entrada22=Entry(ventana2,borderwidth=0)
    Entrada22.config(font=('Helvetica',12),bg='chocolate2')
    Entrada22.place(x=340,y=90, width=110, height=27)

    #Variable 2.3

    Entrada23=Entry(ventana2,borderwidth=0)
    Entrada23.config(font=('Helvetica',12),bg='chocolate2')
    Entrada23.place(x=340,y=147, width=110, height=27)

    #Variable 2.4

    Entrada24=Entry(ventana2,borderwidth=0)
    Entrada24.config(font=('Helvetica',12),bg='chocolate2')
    Entrada24.place(x=340,y=207, width=110, height=27)

    #Variable 3.1

    Entrada31=Entry(ventana2,borderwidth=0)
    Entrada31.config(font=('Helvetica',12),bg='chocolate2')
    Entrada31.place(x=340,y=267, width=110, height=27)

    #Variable 3.2

    Entrada32=Entry(ventana2,borderwidth=0)
    Entrada32.config(font=('Helvetica',12),bg='chocolate2')
    Entrada32.place(x=340,y=322, width=110, height=27)

    #Variable 3.3

    Entrada33=Entry(ventana2,borderwidth=0)
    Entrada33.config(font=('Helvetica',12),bg='chocolate2')
    Entrada33.place(x=340,y=370, width=110, height=27)

    #Variable 3.4

    Entrada34=Entry(ventana2,borderwidth=0)
    Entrada34.config(font=('Helvetica',12),bg='chocolate2')
    Entrada34.place(x=540,y=90, width=110, height=27)

    #Variable 4.1

    Entrada41=Entry(ventana2,borderwidth=0)
    Entrada41.config(font=('Helvetica',12),bg='chocolate2')
    Entrada41.place(x=540,y=147, width=110, height=27)

    #Variable 4.2

    Entrada42=Entry(ventana2,borderwidth=0)
    Entrada42.config(font=('Helvetica',12),bg='chocolate2')
    Entrada42.place(x=540,y=207, width=110, height=27)

    #Variable 4.3

    Entrada43=Entry(ventana2,borderwidth=0)
    Entrada43.config(font=('Helvetica',12),bg='chocolate2')
    Entrada43.place(x=540,y=267, width=110, height=27)

    #Variable 4.4

    Entrada44=Entry(ventana2,borderwidth=0)
    Entrada44.config(font=('Helvetica',12),bg='chocolate2')
    Entrada44.place(x=540,y=325, width=110, height=27)

    #Regreso al menú

    VolverMenu=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/molvermenu.png')
    Boton7=Button(ventana2, text='Volveralmenu2', image=VolverMenu, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana2),borderwidth=0, highlightthickness=0)
    Boton7.place(x=11,y=17)
   
    #Guardar información

    GuardarInfo=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/guardarinfo.png')
    Boton8=Button(ventana2, text='GuardarInformación', image=GuardarInfo, height ="62", width= "220", command=GuardarInformacion,borderwidth=0, highlightthickness=0)
    Boton8.place(x=310,y=412)
    ventana2.mainloop()


def RegiColumnas():
    global ventana3
    CerrarPantalla(ventana1)

    #Inicializamos la pantalla de la 1era opción del menú

    ventana3=Tk()
    ventana3.title("Filas y Columnas - Grupo 9")
    ventana3.geometry("720x480")
    ventana3.resizable(False, False)

    #Abrimos el fondo

    fondo3=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/milasycolumnas.png')
    fondoRC = Label(image = fondo3, text = "filasycolumnas1")
    fondoRC.place(x=0, y=0, relheight=1, relwidth=1)

    #Variable ba

    Entradaba=Entry(ventana3,borderwidth=0)
    Entradaba.config(font=('Helvetica',12),bg='chocolate2')
    Entradaba.place(x=170,y=120, width=140, height=27)

    #Variable bb

    Entradabb=Entry(ventana3,borderwidth=0)
    Entradabb.config(font=('Helvetica',12),bg='chocolate2')
    Entradabb.place(x=170,y=175, width=140, height=27)

    #Variable bc

    Entradabc=Entry(ventana3,borderwidth=0)
    Entradabc.config(font=('Helvetica',12),bg='chocolate2')
    Entradabc.place(x=170,y=230, width=140, height=27)

    #Variable bd

    Entradabd=Entry(ventana3,borderwidth=0)
    Entradabd.config(font=('Helvetica',12),bg='chocolate2')
    Entradabd.place(x=170,y=290, width=140, height=27)

    #Variable yy 340 540

    Entradayy=Entry(ventana3,borderwidth=0)
    Entradayy.config(font=('Helvetica',12),bg='chocolate2')
    Entradayy.place(x=290,y=350, width=50, height=27)

   #Variable ca 

    Entradaca=Entry(ventana3,borderwidth=0)
    Entradaca.config(font=('Helvetica',12),bg='chocolate2')
    Entradaca.place(x=475,y=120, width=140, height=27)

   #Variable cc

    Entradacb=Entry(ventana3,borderwidth=0)
    Entradacb.config(font=('Helvetica',12),bg='chocolate2')
    Entradacb.place(x=475,y=175, width=140, height=27)

    #Variable cc

    Entradacc=Entry(ventana3,borderwidth=0)
    Entradacc.config(font=('Helvetica',12),bg='chocolate2')
    Entradacc.place(x=475,y=230, width=140, height=27)

    #Variable  cd

    Entradacd=Entry(ventana3,borderwidth=0)
    Entradacd.config(font=('Helvetica',12),bg='chocolate2')
    Entradacd.place(x=475,y=290, width=140, height=27)

    #Variable  xx

    Entradaxx=Entry(ventana3,borderwidth=0)
    Entradaxx.config(font=('Helvetica',12),bg='chocolate2')
    Entradaxx.place(x=600,y=353, width=50, height=27)

    #Regreso al menú

    VolverMenu2=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/molvermenu.png')
    Boton9=Button(ventana3, text='Volveralmenu2', image=VolverMenu2, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana3),borderwidth=0, highlightthickness=0)
    Boton9.place(x=11,y=17)

    #Guardar información

    GuardarInfo2=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/guardarinfo.png')
    Boton10=Button(ventana3, text='GuardarInformación', image=GuardarInfo2, height ="62", width= "220", command=GuardarInformacion,borderwidth=0, highlightthickness=0)
    Boton10.place(x=310,y=412)
    ventana3.mainloop()


def VeriDatos():
    global ventana4
    CerrarPantalla(ventana1)
    ventana4 = Tk()
    ventana4.title("Ver Datos - Grupo 9")
    ventana4.geometry("720x480")
    ventana4.resizable(False, False)

    # Fondo

    fondo4 = PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/verTabla.png')
    fondoVT = Label(ventana4, image=fondo4)
    fondoVT.place(x=0, y=0, relheight=1, relwidth=1)

    # Leer datos desde una sola línea

    datos = []
    try:
        with open('C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Data/Data.txt', 'r') as f:
            linea = f.readline().strip()
            valores = linea.split(',')
            for i in range(0, 16, 4):
                fila = valores[i:i+4]
                datos.append(fila)
    except FileNotFoundError:
        print("El archivo de datos no existe. Asegúrate de registrar datos primero.")
    # Coordenadas
    coordenadas = [
        (160, 187), (300, 187), (440, 187), (580, 187),
        (160, 245), (300, 245), (440, 245), (580, 245),
        (160, 300), (300, 300), (440, 300), (580, 300),
        (160, 355), (300, 355), (440, 355), (580, 355)
    ]
    for idx in range(16):
        fila = idx // 4
        col = idx % 4
        valor = datos[fila][col] if fila < len(datos) and col < len(datos[fila]) else ""
        x, y = coordenadas[idx]
        celda = Label(ventana4, text=valor, font=('Helvetica', 12), bg='white', width=10, height=2)
        celda.place(x=x, y=y)
    # Botón de volver al menú (con imagen)
    VolverMenuImg = PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/molvermenu.png')
    BotonVolver = Button(ventana4, image=VolverMenuImg,
                         command=lambda: VolverMenuPrincipal(ventana4),
                         borderwidth=0, highlightthickness=0)
    BotonVolver.image = VolverMenuImg  # <- Importante para que la imagen no se pierda
    BotonVolver.place(x=11, y=17)
    ventana4.mainloop()


def ModelariDatos():
    print("hola4")

def EliminariRegistros():
    # Ruta del archivo donde se almacenan los datos
    archivo_datos = './Data/    Data.txt'

    # Verificar si el archivo existe
    if os.path.exists(archivo_datos):
        # Vaciar el archivo
        with open(archivo_datos, 'w') as f:
            pass  # Sobrescribir el archivo con un contenido vacío
        print("Todos los registros han sido eliminados correctamente.")
    else:
        print("No hay registros para eliminar. El archivo no existe.")

def Saliri():

    ventana1.destroy()

def CerrarPantalla(ventana):

    ventana.destroy()

def GuardarInformacion():
    global Reg11,Reg12,Reg13,Reg14,Reg21,Reg22,Reg23,Reg24,Reg31,Reg32,Reg33,Reg34,Reg41,Reg42,Reg43,Reg44,Data

    Reg11 = Entrada11.get()
    Reg12 = Entrada12.get()
    Reg13 = Entrada13.get()
    Reg14 = Entrada14.get()
    Reg21 = Entrada21.get()
    Reg22 = Entrada22.get()
    Reg23 = Entrada23.get()
    Reg24 = Entrada24.get()
    Reg31 = Entrada31.get()
    Reg32 = Entrada32.get()
    Reg33 = Entrada33.get()
    Reg34 = Entrada34.get()
    Reg41 = Entrada41.get()
    Reg42 = Entrada42.get()
    Reg43 = Entrada43.get()
    Reg44 = Entrada44.get()

    Data = "DatosEmpresa"

    # Consistencia
    if (
        len(Reg11) == 0 or len(Reg12) == 0 or len(Reg13) == 0 or len(Reg14) == 0 or
        len(Reg21) == 0 or len(Reg22) == 0 or len(Reg23) == 0 or len(Reg24) == 0 or
        len(Reg31) == 0 or len(Reg32) == 0 or len(Reg33) == 0 or len(Reg34) == 0 or
        len(Reg41) == 0 or len(Reg42) == 0 or len(Reg43) == 0 or len(Reg44) == 0
    ):
        print("Error, el asno de said no hizo los diseños :p")

    else:
        Lista1 = os.listdir(OutFolderPathDataEmpresa)
        ListaData = []

        for lis in Lista1:
            Empresa = lis.split('.')
            ListaData.append(Empresa[0])

        info = [
            Reg11, Reg12, Reg13, Reg14,
            Reg21, Reg22, Reg23, Reg24,
            Reg31, Reg32, Reg33, Reg34,
            Reg41, Reg42, Reg43, Reg44
        ]

        # Exportar información
        with open(f"{OutFolderPathDataEmpresa}/Data.txt", "a") as f:
            f.write(','.join(info) + '\n')

        # Limpiar
        for entrada in [
            Entrada11, Entrada12, Entrada13, Entrada14,
            Entrada21, Entrada22, Entrada23, Entrada24,
            Entrada31, Entrada32, Entrada33, Entrada34,
            Entrada41, Entrada42, Entrada43, Entrada44
        ]:
            entrada.delete(0, END)


def VolverMenuPrincipal(ventana):
    ventana.destroy()
    FuncionPrincipal()



def FuncionPrincipal():

    global ventana1,OutFolderPathDataEmpresa

    #Definimos las rutas de acceso del kardex

    OutFolderPathDataEmpresa='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Data'

    #Creamos la ventana del menú

    ventana1=Tk()
    ventana1.title("Menú de opciones-Grupo 9")
    ventana1.geometry("853x480")
    ventana1.resizable(False, False)

    #Fondo de la ventana principal

    fondo1=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/menu.png')
    fondo = Label(image = fondo1, text = "menu")
    fondo.place(x=0, y=0, relheight=1, relwidth=1)\
    
    #Botones de la ventana principal
    #1era opción

    RegDatos=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/megistrardatos.png')
    Boton1=Button(ventana1, text='regedatos', image=RegDatos, height ="50", width= "172", command=RegiDatos,borderwidth=0, highlightthickness=0)
    Boton1.place(x=40,y=82)

    #2da opción

    RegColumnas=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/megistrarcolumnas.png')
    Boton2=Button(ventana1, text='regecolumnas', image=RegColumnas, height ="50", width= "172", command=RegiColumnas,borderwidth=0, highlightthickness=0)
    Boton2.place(x=40,y=142)

    #3era opción

    VerDatos=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/mertabla.png')
    Boton3=Button(ventana1, text='VereDatos', image=VerDatos, height ="50", width= "172", command=VeriDatos,borderwidth=0, highlightthickness=0)
    Boton3.place(x=40,y=202)

    #4ta opción

    ModelarDatos=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/modelardatos.png')
    Boton4=Button(ventana1, text='ModeDatos', image=ModelarDatos, height ="50", width= "172", command=ModelariDatos,borderwidth=0, highlightthickness=0)
    Boton4.place(x=40,y=265)

    #5ta opción

    EliminarRegistros=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/eliminarregistros.png')
    Boton5=Button(ventana1, text='ElimiReg', image=EliminarRegistros, height ="50", width= "172", command=EliminariRegistros,borderwidth=0, highlightthickness=0)
    Boton5.place(x=40,y=328)

    #6ta opción

    Salir=PhotoImage(file='C:/Users/USER/OneDrive/Escritorio/UNMSM/ProjectPY/InveOp/Images/salir.png')
    Boton6=Button(ventana1, text='SalirProg', image=Salir, height ="50", width= "172", command=Saliri,borderwidth=0, highlightthickness=0)
    Boton6.place(x=40,y=392)
    ventana1.mainloop()

FuncionPrincipal()