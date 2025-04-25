from tkinter import *

import os

def RegiEmpresa():
    global ventana2,EntradaNombre,EntradaPais,EntradaDireccion,EntradaDepartamento
    CerrarPantalla(ventana1)

    #Inicializamos la pantalla de la 1era opción del menú

    ventana2=Tk()
    ventana2.title("Registrar datos de una empresa-Grupo 7")
    ventana2.geometry("720x480")
    ventana2.resizable(False, False)

    #Abrimos el fondo
    
    fondo2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registroempresa.png')
    fondoRE = Label(image = fondo2, text = "registrarempresa")
    fondoRE.place(x=0, y=0, relheight=1, relwidth=1)

    #Apertura para la entrada de datos

    #Nombre de la empresa

    EntradaNombre=Entry(ventana2,borderwidth=0)
    EntradaNombre.config(font=('Helvetica',12))
    EntradaNombre.place(x=270,y=135)

    #Ubicación de la empresa(País)
    
    EntradaPais=Entry(ventana2,borderwidth=0)
    EntradaPais.config(font=('Helvetica',12))
    EntradaPais.place(x=270,y=200)

    #Ubicación de la empresa(Departamento)
    
    EntradaDepartamento=Entry(ventana2,borderwidth=0)
    EntradaDepartamento.config(font=('Helvetica',12))
    EntradaDepartamento.place(x=270,y=265)

    #ubicación de la empresa(Dirección)

    EntradaDireccion=Entry(ventana2,borderwidth=0)
    EntradaDireccion.config(font=('Helvetica',12))
    EntradaDireccion.place(x=270,y=335)

    #Botones

    #Guardar información

    GuardarInfo=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/guardarinformación.png')
    Boton7=Button(ventana2, text='GuardarInformación1', image=GuardarInfo, height ="62", width= "220", command=GuardarInformación,borderwidth=0, highlightthickness=0)
    Boton7.place(x=250,y=400)

    #Regreso al menú

    VolverMenu=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/volveralmenu.png')
    Boton8=Button(ventana2, text='Volveralmenu', image=VolverMenu, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana2),borderwidth=0, highlightthickness=0)
    Boton8.place(x=20,y=20)
    ventana2.mainloop()

def RegiProducto():

    global EntradaNombreP, EntradaCodigoP,EntradaPrecioU,EntradaCantidadP,EntradaFechaP,ventana3
    CerrarPantalla(ventana1)

    #Inicializamos la pantalla de la 2da opción del menú

    ventana3=Tk()
    ventana3.title("Registrar productos-Grupo 7")
    ventana3.geometry("720x480")
    ventana3.resizable(False, False)

    #Abrimos el fondo
    
    fondo3=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registroproducto.png')
    fondoRP = Label(image = fondo3, text = "registrarproducto")
    fondoRP.place(x=0, y=0, relheight=1, relwidth=1)

    #Apertura para la entrada de datos

    #Nombre del producto

    EntradaNombreP=Entry(ventana3,borderwidth=0)
    EntradaNombreP.config(font=('Helvetica',8))
    EntradaNombreP.place(x=350,y=112) 

    #Código del Producto
    
    EntradaCodigoP=Entry(ventana3,borderwidth=0)
    EntradaCodigoP.config(font=('Helvetica',8))
    EntradaCodigoP.place(x=350,y=163)

    #Precio Unitario del Producto
    
    EntradaPrecioU=Entry(ventana3,borderwidth=0)
    EntradaPrecioU.config(font=('Helvetica',8))
    EntradaPrecioU.place(x=350,y=220)

    #Cantidad Inicial del Producto

    EntradaCantidadP=Entry(ventana3,borderwidth=0)
    EntradaCantidadP.config(font=('Helvetica',8))
    EntradaCantidadP.place(x=350,y=290)

    #Fecha del producto

    EntradaFechaP=Entry(ventana3,borderwidth=0)
    EntradaFechaP.config(font=('Helvetica',8))
    EntradaFechaP.place(x=350,y=343)

    #Regreso al menú

    VolverMenu2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/volveralmenu.png')
    Boton9=Button(ventana3, text='Volveralmenu2', image=VolverMenu2, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana3),borderwidth=0, highlightthickness=0)
    Boton9.place(x=20,y=20)

    #Guardar información

    GuardarInfo2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/guardarinformación.png')
    Boton10=Button(ventana3, text='GuardarInformación2', image=GuardarInfo2, height ="62", width= "220", command=GuardarInformación2,borderwidth=0, highlightthickness=0)
    Boton10.place(x=250,y=400)
    ventana3.mainloop()

def RegiMovimiento():

    global ventana1, fondo5, fondo6, fondo7,aceptar,aceptar2,aceptar3,ventana4,fondo8,EntradaCodigo,EntradaTipoMovimiento,EntradaCantidad,EntradaFecha
    if not os.listdir(OutFolderPathDataEmpresa) and not os.listdir(OutFolderPathDataProducto):
        ventana8 = Toplevel(ventana1)
        ventana8.title("Advertencia!")
        ventana8.geometry("200x200")
        ventana8.resizable(False, False)
        fondo7 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertencia.png')
        fondoadvertencia3 = Label(ventana8, image=fondo7, text="advertencia")
        fondoadvertencia3.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar3=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar3=Button(ventana8, text='advertenciaaceptar', image=aceptar3, height ="40", width= "60", command=lambda:CerrarPantalla(ventana8),borderwidth=0, highlightthickness=0)
        botonaceptar3.place(x=75,y=130)

    elif not os.listdir(OutFolderPathDataEmpresa):
        ventana6 = Toplevel(ventana1)
        ventana6.title("Advertencia!")
        ventana6.geometry("200x200")
        ventana6.resizable(False, False)
        fondo5 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertenciaempresa.png')
        fondoadvertencia = Label(ventana6, image=fondo5, text="advertenciaempresa")
        fondoadvertencia.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar=Button(ventana6, text='advertenciaaceptar', image=aceptar, height ="40", width= "60", command=lambda:CerrarPantalla(ventana6),borderwidth=0, highlightthickness=0)
        botonaceptar.place(x=75,y=130)

    elif not os.listdir(OutFolderPathDataProducto):
        ventana7 = Toplevel(ventana1)
        ventana7.title("Advertencia!")
        ventana7.geometry("200x200")
        ventana7.resizable(False, False)
        fondo6 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertenciaproducto.png')
        fondoadvertencia2 = Label(ventana7, image=fondo6, text="advertenciaproducto")
        fondoadvertencia2.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar2=Button(ventana7, text='advertenciaaceptar', image=aceptar2, height ="40", width= "60", command=lambda:CerrarPantalla(ventana7),borderwidth=0, highlightthickness=0)
        botonaceptar2.place(x=75,y=130)

    else:
        CerrarPantalla(ventana1)
        ventana4 = Tk()
        ventana4.title("Registrar el movimiento de un producto-Grupo7")
        ventana4.geometry("720x480")
        ventana4.resizable(False, False)
        fondo4 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registromovimiento.png')
        fondoRP = Label(ventana4, image=fondo4, text="registrarmovimiento")
        fondoRP.place(x=0, y=0, relheight=1, relwidth=1)

        # Apertura para la entrada de datos

        # Código del Producto

        EntradaCodigo = Entry(ventana4, borderwidth=0)
        EntradaCodigo.config(font=('Helvetica', 8))
        EntradaCodigo.place(x=330, y=114)

        # Tipo de movimiento del producto (Compra o Venta)

        EntradaTipoMovimiento = Entry(ventana4, borderwidth=0)
        EntradaTipoMovimiento.config(font=('Helvetica', 8))
        EntradaTipoMovimiento.place(x=330, y=177)

        # Cantidad del producto asdasdasasd 

        EntradaCantidad = Entry(ventana4, borderwidth=0)
        EntradaCantidad.config(font=('Helvetica', 8))
        EntradaCantidad.place(x=330, y=250)

        # Fecha de la operación

        EntradaFecha = Entry(ventana4, borderwidth=0)
        EntradaFecha.config(font=('Helvetica', 8))
        EntradaFecha.place(x=330, y=328)

        # Botones
        VolverMenu2 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/volveralmenu.png')
        Boton11 = Button(ventana4, text='Volveralmenu2', image=VolverMenu2, height="40", width="100", command=lambda: VolverMenuPrincipal(ventana4), borderwidth=0, highlightthickness=0)
        Boton11.place(x=20, y=20)
        GuardarInfo3 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/guardarinformación.png')
        Boton12 = Button(ventana4, text='GuardarInformación3', image=GuardarInfo3, height="62", width="220", command=GuardarInformación3, borderwidth=0, highlightthickness=0)
        Boton12.place(x=250, y=400)

        # Mostrar lista de productos

        lista_productos = []
        for archivo in os.listdir(OutFolderPathDataProducto):
            if archivo.endswith(".txt"):
                with open(os.path.join(OutFolderPathDataProducto, archivo), "r") as file:
                    lineas = file.readlines()
                    if lineas:

                        # Obtener nombre y código del producto desde el archivo

                        info_producto = lineas[0].strip().split(',')
                        if len(info_producto) >= 2:
                            nombre = info_producto[0]
                            codigo = info_producto[1]
                            lista_productos.append(f"{nombre} - {codigo}")


        # Mostrar la lista de productos en la ventana 9

        ventana9 = Toplevel(ventana4)
        ventana9.title("Lista de Productos")
        ventana9.geometry("200x400")
        ventana9.resizable(False, False)
        fondo8 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/lista.png')
        listaproductos = Label(ventana9, image=fondo8, text="listaproductos")
        listaproductos.place(x=0, y=0, relheight=1, relwidth=1)

        # Crear etiqueta para mostrar la lista de productos

        etiqueta_productos = Label(ventana9, text="\n".join(lista_productos), anchor="w", justify="left", font=('Poppins', 12,'bold'),bg="SteelBlue1")
        etiqueta_productos.place(x=10, y=80)
        ventana4.mainloop()


def VerKardexUnitario():

    global fondo6,aceptar2,fondo10,BuscarCodigo,ventana5
    if not os.listdir(OutFolderPathDataProducto):
        ventana7 = Toplevel(ventana1)
        ventana7.title("Advertencia!")
        ventana7.geometry("200x200")
        ventana7.resizable(False, False)
        fondo6 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertenciaproducto.png')
        fondoadvertencia2 = Label(ventana7, image=fondo6, text="advertenciaproducto")
        fondoadvertencia2.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar2=Button(ventana7, text='advertenciaaceptar', image=aceptar2, height ="40", width= "60", command=lambda:CerrarPantalla(ventana7),borderwidth=0, highlightthickness=0)
        botonaceptar2.place(x=75,y=130)

    else:
        CerrarPantalla(ventana1)
        ventana5=Tk()
        ventana5.title("Ver Kárdex Unitario-Grupo 7")
        ventana5.geometry("1000x707")
        ventana5.resizable(False, False)

        #Abrimos el fondo
        
        fondo10=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/VerKardex.png')
        fondoK = Label(image = fondo10, text = "kardexunitario")
        fondoK.place(x=0, y=0, relheight=1, relwidth=1)

        # Apertura para la entrada de datos

        # Código del Producto

        BuscarCodigo = Entry(ventana5, borderwidth=0,bg='lightblue')
        BuscarCodigo.config(font=('Helvetica', 8))
        BuscarCodigo.place(x=50, y=135)
        
        #Botón para buscar el código

        BotonBuscar=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/buscarproducto.png')
        Botonbuscar=Button(ventana5, text='Volveralmenu2', image=BotonBuscar, height ="40", width= "100", command=buscar_codigo,borderwidth=0, highlightthickness=0)
        Botonbuscar.place(x=180,y=125)

        #Botón para regresar al menú

        VolverMenu=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/volver.png')
        BotonVolver=Button(ventana5, text='Volveralmenu2', image=VolverMenu, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana5),borderwidth=0, highlightthickness=0)
        BotonVolver.place(x=20,y=20)
        ventana5.mainloop()

def VerKardexTotal():

    global fondo11, ventana1, fondo7, aceptar3, fondo5, aceptar, fondo6, aceptar2, fondo9
    if not os.listdir(OutFolderPathDataEmpresa) and not os.listdir(OutFolderPathDataProducto):
        ventana8 = Toplevel(ventana1)
        ventana8.title("Advertencia!")
        ventana8.geometry("200x200")
        ventana8.resizable(False, False)
        fondo7 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertencia.png')
        fondoadvertencia3 = Label(ventana8, image=fondo7, text="advertencia")
        fondoadvertencia3.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar3=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar3=Button(ventana8, text='advertenciaaceptar', image=aceptar3, height ="40", width= "60", command=lambda:CerrarPantalla(ventana8),borderwidth=0, highlightthickness=0)
        botonaceptar3.place(x=75,y=130)

    elif not os.listdir(OutFolderPathDataEmpresa):
        ventana6 = Toplevel(ventana1)
        ventana6.title("Advertencia!")
        ventana6.geometry("200x200")
        ventana6.resizable(False, False)
        fondo5 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertenciaempresa.png')
        fondoadvertencia = Label(ventana6, image=fondo5, text="advertenciaempresa")
        fondoadvertencia.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar=Button(ventana6, text='advertenciaaceptar', image=aceptar, height ="40", width= "60", command=lambda:CerrarPantalla(ventana6),borderwidth=0, highlightthickness=0)
        botonaceptar.place(x=75,y=130)

    elif not os.listdir(OutFolderPathDataProducto):
        ventana7 = Toplevel(ventana1)
        ventana7.title("Advertencia!")
        ventana7.geometry("200x200")
        ventana7.resizable(False, False)
        fondo6 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertenciaproducto.png')
        fondoadvertencia2 = Label(ventana7, image=fondo6, text="advertenciaproducto")
        fondoadvertencia2.place(x=0, y=0, relheight=1, relwidth=1)
        aceptar2=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')
        botonaceptar2=Button(ventana7, text='advertenciaaceptar', image=aceptar2, height ="40", width= "60", command=lambda:CerrarPantalla(ventana7),borderwidth=0, highlightthickness=0)
        botonaceptar2.place(x=75,y=130)

    else:    
        CerrarPantalla(ventana1)
        ventana12=Tk()
        ventana12.title("Ver Kárdex Total-Grupo 7")
        ventana12.geometry("1000x707")
        ventana12.resizable(False, False)

        #Abrimos el fondo
        
        fondo9=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/VerKardexTotal.png')
        fondoK = Label(image = fondo9, text = "kardextotal")
        fondoK.place(x=0, y=0, relheight=1, relwidth=1)

        #Iniciamos la recopilación de los datos de la empresa

        lista_empresa = []
        for archivo2 in os.listdir(OutFolderPathDataEmpresa):
            if archivo2.endswith(".txt"):
                with open(os.path.join(OutFolderPathDataEmpresa, archivo2), "r") as file:
                    contenido = file.readlines()
                    if contenido:
                        info_empresa = contenido[0].strip().split(',')
                        if len(info_empresa) >= 4:
                            nombre = info_empresa[0]
                            codigo = info_empresa[1]
                            valor_unitario = info_empresa[2]
                            cantidad_inicial = info_empresa[3]
                            lista_empresa.append(nombre)
                            lista_empresa.append(codigo)
                            lista_empresa.append(valor_unitario)
                            lista_empresa.append(cantidad_inicial)

        # Ventana secundaria para observar los datos de la empresa

        ventana10 = Toplevel(ventana12)
        ventana10.title("EMPRESA")
        ventana10.geometry("200x200")
        ventana10.resizable(False, False)
        fondo11 = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/Ventana Flotante Kardex.png')
        reporteempresa = Label(ventana10, image=fondo11, text='empresakardex')
        reporteempresa.place(x=0, y=0, relheight=1, relwidth=1)

        # Crear etiqueta para mostrar la empresa

        etiqueta_empresa1 = Label(ventana10, text=lista_empresa[0], anchor="w", justify="left", font=('Poppins', 8, 'bold'), bg="white")
        etiqueta_empresa1.place(x=20, y=34)

        # Crear etiqueta para mostrar la empresa

        etiqueta_empresa2 = Label(ventana10, text=lista_empresa[1], anchor="w", justify="left", font=('Poppins', 8, 'bold'), bg="white")
        etiqueta_empresa2.place(x=20, y=78)

        # Crear etiqueta para mostrar la empresa

        etiqueta_empresa3 = Label(ventana10, text=lista_empresa[2], anchor="w", justify="left", font=('Poppins', 8, 'bold'), bg="white")
        etiqueta_empresa3.place(x=20, y=122)

        # Crear etiqueta para mostrar la empresa

        etiqueta_empresa4 = Label(ventana10, text=lista_empresa[3], anchor="w", justify="left", font=('Poppins', 8, 'bold'), bg="white")
        etiqueta_empresa4.place(x=20, y=166)

                # Recopilar la información de los productos
        lista_productos = []
        for archivo in os.listdir(OutFolderPathDataProducto):
            if archivo.endswith(".txt"):
                with open(os.path.join(OutFolderPathDataProducto, archivo), "r") as file:
                    lineas = file.readlines()
                    if lineas:
                        info_producto = lineas[0].strip().split(',')
                        if len(info_producto) >= 4:  # Asegurar que haya al menos 4 elementos (nombre, código, precio, cantidad)
                            nombre_producto = info_producto[0]
                            codigo_producto = info_producto[1]
                            valor_unitario_producto = float(info_producto[2])
                            cantidad_inicial_producto = int(info_producto[3])
                            # Obtén la información del movimiento del producto
                            movimientos = []
                            archivo_movimiento = os.path.join(OutFolderPathDataMovimiento, f"{codigo_producto}.txt")
                            if os.path.exists(archivo_movimiento):
                                with open(archivo_movimiento, "r") as file_movimiento:
                                    for linea in file_movimiento:
                                        movimientos.append(linea.strip().split(","))
                            # Calcula el total (saldo)
                            saldo = cantidad_inicial_producto
                            for movimiento in movimientos:
                                if movimiento[1].lower() == 'compra':
                                    saldo += int(movimiento[2])
                                elif movimiento[1].lower() == 'venta':
                                    saldo -= int(movimiento[2])
                            # Agrega el producto a la lista
                            lista_productos.append({
                                'nombre': nombre_producto,
                                'codigo': codigo_producto,
                                'valor_unitario': valor_unitario_producto,
                                'cantidad_final': saldo,
                                'saldo_total': saldo * valor_unitario_producto  # Calcula el saldo total
                            })


        # Crear etiqueta para mostrar la información de los productos
        y_position = 230 # Posición inicial en Y
        for producto in lista_productos:

            # Nombre del producto
            etiqueta_nombre = Label(ventana12, text=f"{producto['nombre']} - {producto['codigo']}", anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
            etiqueta_nombre.place(x=60, y=y_position)

            # Valor unitario del producto

            etiqueta_valor_unitario = Label(ventana12, text=f"{producto['valor_unitario']}", anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
            etiqueta_valor_unitario.place(x=490, y=y_position)

            # Cantidad final del producto

            etiqueta_cantidad_final = Label(ventana12, text=f"{producto['cantidad_final']}", anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
            etiqueta_cantidad_final.place(x=670, y=y_position)

            # Saldo total del producto

            etiqueta_saldo_total = Label(ventana12, text=f"{producto['saldo_total']:.2f}", anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
            etiqueta_saldo_total.place(x=830, y=y_position)

            y_position += 45

        #Botón para regresar al menú

        VolverMenu=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/volver.png')
        BotonVolver=Button(ventana12, text='Volveralmenu2', image=VolverMenu, height ="40", width= "100", command=lambda:VolverMenuPrincipal(ventana12),borderwidth=0, highlightthickness=0)
        BotonVolver.place(x=20,y=20)
        ventana12.mainloop()

def EliminaRegistros():

    # Eliminar archivos en la carpeta Registro Empresa

    dataempresa = OutFolderPathDataEmpresa

    for listaempresa in os.listdir(dataempresa):
        
        archivo = os.path.join(dataempresa, listaempresa)

        if os.path.isfile(archivo):

            os.remove(archivo)
    
    # Eliminar archivos en la carpeta Registro Producto

    dataproducto = OutFolderPathDataProducto

    for listaproducto in os.listdir(dataproducto):

        archivo2 = os.path.join(dataproducto, listaproducto)

        if os.path.isfile(archivo2):
            
            os.remove(archivo2)
    
    # Eliminar archivos en la carpeta Registro Movimiento

    datamovimiento = OutFolderPathDataMovimiento

    for listamovimiento in os.listdir(datamovimiento):

        archivo3 = os.path.join(datamovimiento, listamovimiento)

        if os.path.isfile(archivo3):

            os.remove(archivo3)

    print("Se han eliminado todos los registros.")

def GuardarInformación():

    global RegEntradaNombre,RegEntradaPais,RegEntradaDireccion,RegEntradaDepartamento,EmpresaLista,PantallaEmpresa,fondoempresa,aceptarempresa

    RegEntradaNombre,RegEntradaPais,RegEntradaDireccion,RegEntradaDepartamento=EntradaNombre.get(),EntradaPais.get(),EntradaDireccion.get(),EntradaDepartamento.get()
    
    #Consistencia
  
    if len(RegEntradaNombre) == 0 or len(RegEntradaPais) == 0 or len(RegEntradaDireccion) == 0 or len(RegEntradaDepartamento) == 0:

        print("ERROR AL COMPLETAR EL FORMULARIO")
  
    else:

        EmpresaLista = os.listdir(OutFolderPathDataEmpresa)
  
        EmpresaInfo = []

        for lis in EmpresaLista:

            #Extracción de Usuario
  
            Empresa = lis.split('.')
  
            #AlmacenarUsuario
  
            EmpresaInfo.append(Empresa[0])

        if os.listdir(OutFolderPathDataEmpresa):
  
            #registrado

            PantallaEmpresa = Toplevel(ventana2)

            PantallaEmpresa.title("Advertencia!")

            PantallaEmpresa.geometry("200x200")

            PantallaEmpresa.resizable(False, False)
            
            fondoempresa = PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/advertencia2.png')

            fondoadvertencia3 = Label(PantallaEmpresa, image=fondoempresa, text="advertencia")

            fondoadvertencia3.place(x=0, y=0, relheight=1, relwidth=1)

            aceptarempresa=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/aceptar.png')

            botonaceptar3=Button(PantallaEmpresa, text='advertenciaaceptar2', image=aceptarempresa, height ="40", width= "60", command=lambda:CerrarPantalla(PantallaEmpresa),borderwidth=0, highlightthickness=0)

            botonaceptar3.place(x=75,y=130)
  
            print("EMPRESA YA REGISTRADA")

            EntradaNombre.delete(0, END)
  
            EntradaPais.delete(0, END)
  
            EntradaDepartamento.delete(0, END)
  
            EntradaDireccion.delete(0, END) 
  
        else:
  
            #No Registrado
  
            info = []
  
            info.append(RegEntradaNombre)
  
            info.append(RegEntradaPais)
  
            info.append(RegEntradaDepartamento)
  
            info.append(RegEntradaDireccion)
  
            #Exportar la información
  
            f = open(f"{OutFolderPathDataEmpresa}/{RegEntradaNombre}.txt", "a")
  
            f.write(RegEntradaNombre + ',')
  
            f.write(RegEntradaPais + ',')
  
            f.write(RegEntradaDepartamento + ',')
  
            f.write(RegEntradaDireccion)
  
            f.close()
  
            #Limpiar
  
            EntradaNombre.delete(0, END)
  
            EntradaPais.delete(0, END)
  
            EntradaDepartamento.delete(0, END)
  
            EntradaDireccion.delete(0, END) 


def GuardarInformación2():

    global RegNombreP,RegCodigoP,RegPrecioU,RegPrecioI,RegFechaP,EmpresaLista2,i

    RegNombreP,RegCodigoP,RegPrecioU,RegPrecioI,RegFechaP=EntradaNombreP.get(),EntradaCodigoP.get(),EntradaPrecioU.get(),EntradaCantidadP.get(),EntradaFechaP.get()
    
    #Consistencia

    if len(RegNombreP) == 0 or len(RegCodigoP) == 0 or len(RegPrecioU) == 0 or len(RegPrecioI) == 0 or len(RegFechaP) == 0 :
         
        print("ERROR AL COMPLETAR EL FORMULARIO")

    # Verificar si el precio y la cantidad son números

    try:

        float(RegPrecioU) #verificar si la cantidad es un flotante

        int(RegPrecioI)  # Verificar si la cantidad es un entero

    except ValueError:

        #Limpiar
  
        EntradaNombreP.delete(0, END)
  
        EntradaCodigoP.delete(0, END)
  
        EntradaPrecioU.delete(0, END)
  
        EntradaCantidadP.delete(0, END)

        EntradaFechaP.delete(0, END) 

        print("ERROR AL COMPLETAR EL FORMULARIO")

        return  # Salir de la función si hay errores de entrada
    
    else:

        EmpresaLista2 = os.listdir(OutFolderPathDataProducto)

        ProductoInfo = []

        i=1

        for lis2 in EmpresaLista2:

            i=i+1

            #Extracción de Usuario

            Producto=lis2.split('.')

            #Almacenar Usuario

            ProductoInfo.append(Producto[0])

        if RegNombreP in ProductoInfo:

            #Registrado 

            print("PRODUCTO REGISTRADO ANTERIORMENTE")
        
        else:

            #No Registrado

            info2 = []

            info2.append(RegNombreP)

            info2.append(RegCodigoP)

            info2.append(RegPrecioU)

            info2.append(RegPrecioI)

            info2.append(RegFechaP)

            #Exportar la información

            f = open(f"{OutFolderPathDataProducto}/{i}.txt","a")

            f.write(RegNombreP + ',')

            f.write(RegCodigoP + ',')  

            f.write(RegPrecioU + ',')  

            f.write(RegPrecioI + ',')

            f.write(RegFechaP)

            f.close()   

            #Limpiar
  
            EntradaNombreP.delete(0, END)
  
            EntradaCodigoP.delete(0, END)
  
            EntradaPrecioU.delete(0, END)
  
            EntradaCantidadP.delete(0, END)

            EntradaFechaP.delete(0, END)         

def CerrarPantalla(ventana):
    ventana.destroy()

def GuardarInformación3():
    global RegCodigoProducto, RegTipoMovimiento, RegCantidadP, RegFechaProducto,Cantidad_Final,Cantidad_Inicial,Cantidad_Adicional
    RegCodigoProducto, RegTipoMovimiento, RegCantidadP, RegFechaProducto = EntradaCodigo.get(), EntradaTipoMovimiento.get(), EntradaCantidad.get(), EntradaFecha.get()
    # Consistencia

    if len(RegCodigoProducto) == 0 or len(RegTipoMovimiento) == 0 or len(RegCantidadP) == 0 or len(RegFechaProducto) == 0:
        print("ERROR AL COMPLETAR EL FORMULARIO")
        return  # Salir de la función si hay errores de entrada
    
    try:
        int(RegCantidadP) #verificar si la cantidad es un entero

    except ValueError:

        #Limpiar
  
        EntradaCodigo.delete(0, END)
        EntradaTipoMovimiento.delete(0, END)
        EntradaCantidad.delete(0, END)
        EntradaFecha.delete(0, END) 
        print("ERROR AL DIGITAR LA CANTIDAD DEL PRODUCTO")
        return  # Salir de la función si hay errores de entrada

    # Verificar si el producto existe en la carpeta de productos

    producto_encontrado = False

    for archivo_producto in os.listdir(OutFolderPathDataProducto):
        if archivo_producto.endswith(".txt"):
            with open(os.path.join(OutFolderPathDataProducto, archivo_producto), "r") as file:
                lineas = file.readlines()
                if lineas:
                    info_producto = lineas[0].strip().split(',')
                    if len(info_producto) >= 2 and info_producto[1] == RegCodigoProducto:
                        producto_encontrado = True
                        break  # Se encontró el producto, salir del bucle

    if not producto_encontrado:
        print("El producto no se encuentra en la base de datos.")
        EntradaCodigo.delete(0, END)
        EntradaTipoMovimiento.delete(0, END)
        EntradaCantidad.delete(0, END)
        EntradaFecha.delete(0, END) 
        return  # Salir de la función si el producto no existe

    # Leer la cantidad inicial del producto desde el archivo

    try:
        with open(os.path.join(OutFolderPathDataProducto, archivo_producto), "r") as file:
            lineas = file.readlines()
            if lineas:
                info_producto = lineas[0].strip().split(',')
                if len(info_producto) >= 4:  # Asegurar que haya al menos 4 elementos (nombre, código, precio, cantidad)
                    Cantidad_Inicial = int(info_producto[3]) 

    except FileNotFoundError:
        print("ERROR: El archivo del producto no se encontró.")
        return
    
    try:

        if RegTipoMovimiento.lower() == 'compra':
            Cantidad_Adicional = int(RegCantidadP)
            Cantidad_Final = Cantidad_Inicial + Cantidad_Adicional

        elif RegTipoMovimiento.lower() == 'venta':
            Cantidad_Adicional = int(RegCantidadP)
            Cantidad_Final = Cantidad_Inicial - Cantidad_Adicional

            # Verificar si hay suficiente inventario para la venta

            if Cantidad_Final < 0:
                EntradaCodigo.delete(0, END)
                EntradaTipoMovimiento.delete(0, END)
                EntradaCantidad.delete(0, END)
                EntradaFecha.delete(0, END) 
                print("ERROR: No hay suficiente inventario para la venta.")
                return  # Salir de la función si no hay suficiente inventario
            
        else:
            print("ERROR AL INGRESAR EL TIPO DE MOVIMIENTO")
            EntradaCodigo.delete(0, END)
            EntradaTipoMovimiento.delete(0, END)
            EntradaCantidad.delete(0, END)
            EntradaFecha.delete(0, END)
            return  # Salir de la función si el tipo de movimiento es inválido
        
    except ValueError:
        print("ERROR: La cantidad debe ser un número entero.")
        return

    # Guardar el movimiento en el archivo

    informacion = []
    informacion.append(RegCodigoProducto)
    informacion.append(RegTipoMovimiento)
    informacion.append(RegCantidadP)
    informacion.append(RegFechaProducto)

    with open(f"{OutFolderPathDataMovimiento}/{RegCodigoProducto}.txt", "a") as f:
        f.write(",".join(informacion) + "\n")

    # Actualizar la cantidad inicial del producto en el archivo

    with open(archivo_producto, "w") as file:
        file.write(f"{info_producto[0]},{info_producto[1]},{info_producto[2]},{Cantidad_Final}\n")

    # Limpiar los campos de entrada

    EntradaCodigo.delete(0, END)
    EntradaTipoMovimiento.delete(0, END)
    EntradaCantidad.delete(0, END)
    EntradaFecha.delete(0, END) 
    print("REGISTRADO CORRECTAMENTE")

def buscar_codigo():
    global EncontrarCodigo2, ventana5, cantidad_label, saldo_label, movimientos_labels
    EncontrarCodigo2 = BuscarCodigo.get()
    if len(EncontrarCodigo2) == 0:
        print("ERROR AL COMPLETAR EL FORMULARIO")
    else:
        ListaBuscar = os.listdir(OutFolderPathDataProducto)

        for archivo_producto in ListaBuscar:
            if archivo_producto.endswith(".txt"):
                with open(os.path.join(OutFolderPathDataProducto, archivo_producto), "r") as file:
                    lineas = file.readlines()
                    if lineas:
                        info_producto = lineas[0].strip().split(',')
                        if len(info_producto) >= 2:
                            codigo_producto = info_producto[1]
                            if codigo_producto == EncontrarCodigo2:
                                print("¡Código encontrado en el archivo:", archivo_producto)
                                BuscarCodigo.delete(0, END)

                                # Obtén la información del producto
                                producto_info = info_producto

                                # Obtén la información del movimiento del producto
                                movimientos = []
                                archivo_movimiento = os.path.join(OutFolderPathDataMovimiento, f"{codigo_producto}.txt")
                                if os.path.exists(archivo_movimiento):
                                    with open(archivo_movimiento, "r") as file_movimiento:
                                        for linea in file_movimiento:
                                            movimientos.append(linea.strip().split(","))

                                # Calcula el total (saldo)
                                cantidad_inicial = int(info_producto[3])
                                saldo = cantidad_inicial
                                valor_unitario = float(info_producto[2])
                                saldo_total = saldo * valor_unitario  # Calcula el saldo total

                                y_position = 240  # Posición inicial en el eje Y
                                movimientos_labels = []  # Inicializa la lista de etiquetas para los movimientos

                                # Bucle para mostrar los movimientos
                                for i, movimiento in enumerate(movimientos):

                                     # Crea nuevas etiquetas en cada iteración
                                    cantidad_label = Label(ventana5, text=f"Cantidad Final: {saldo}",
                                                        anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    cantidad_label.place(x=790, y=y_position)
                                    saldo_label = Label(ventana5, text=saldo_total,  # Muestra el saldo total
                                                        anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    saldo_label.place(x=880, y=y_position)
                                    # Fecha
                                    etiqueta_kardex = Label(ventana5, text=movimiento[3],
                                                           anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    etiqueta_kardex.place(x=40, y=y_position)

                                    # Detalle
                                    etiqueta_kardex = Label(ventana5, text=movimiento[1],
                                                           anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    if movimiento[1].lower() == 'compra':
                                        etiqueta_kardex.place(x=150, y=y_position)  # Posición original
                                    elif movimiento[1].lower() == 'venta':
                                        etiqueta_kardex.place(x=180, y=y_position)  # Posición desplazada

                                    # Valor Unitario
                                    etiqueta_kardex = Label(ventana5, text=producto_info[2],
                                                           anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    etiqueta_kardex.place(x=290, y=y_position)

                                    # Cantidad
                                    cantidad_movimiento = int(movimiento[2])
                                    etiqueta_cantidad = Label(ventana5, text=f"{cantidad_movimiento}",
                                                            anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    if movimiento[1].lower() == 'compra':
                                        etiqueta_cantidad.place(x=430, y=y_position)  # Posición original
                                    elif movimiento[1].lower() == 'venta':
                                        etiqueta_cantidad.place(x=620, y=y_position)  # Posición desplazada

                                    # Total
                                    total_movimiento = cantidad_movimiento * valor_unitario
                                    etiqueta_total = Label(ventana5, text=f"{total_movimiento:.2f}",
                                                            anchor="w", justify="left", font=('Poppins', 12, 'bold'), bg="light goldenrod yellow")
                                    if movimiento[1].lower() == 'compra':
                                        etiqueta_total.place(x=500, y=y_position)  # Posición original
                                    elif movimiento[1].lower() == 'venta':
                                        etiqueta_total.place(x=700, y=y_position)  # Posición desplazada

                                    # Agrega las etiquetas de cada movimiento a la lista
                                    movimientos_labels.append((etiqueta_kardex, etiqueta_kardex, etiqueta_kardex, etiqueta_cantidad, etiqueta_total))

                                    # Actualiza el saldo
                                    if movimiento[1].lower() == 'compra':
                                        saldo += cantidad_movimiento
                                        saldo_total += total_movimiento
                                    elif movimiento[1].lower() == 'venta':
                                        saldo -= cantidad_movimiento
                                        saldo_total -= total_movimiento

                                    # Actualiza las etiquetas existentes
                                    cantidad_label.config(text=saldo)
                                    saldo_label.config(text=saldo_total)

                                    y_position += 45  # Incrementa la posición en Y para el siguiente movimiento
                                return  # Detener la búsqueda si se encuentra

        print("ERROR AL COMPLETAR EL FORMULARIO CONCHATUMARE")
        BuscarCodigo.delete(0, END)

def VolverMenuPrincipal(ventana):
    ventana.destroy()
    FuncionPrincipal()

def FuncionPrincipal():
    global ventana1,OutFolderPathDataEmpresa,OutFolderPathDataMovimiento,OutFolderPathDataProducto

    #Definimos las rutas de acceso del kardex

    OutFolderPathDataEmpresa='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Data/Registro Empresa'
    OutFolderPathDataMovimiento='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Data/Registro Movimiento'
    OutFolderPathDataProducto='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Data/Registro Producto'


    #Creamos la ventana del menú

    ventana1=Tk()
    ventana1.title("Menú de opciones-Grupo 7")
    ventana1.geometry("720x480")
    ventana1.resizable(False, False)

    #Fondo de la ventana principal

    fondo1=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/menu.png')
    fondo = Label(image = fondo1, text = "menu")
    fondo.place(x=0, y=0, relheight=1, relwidth=1)

    #Botones de la ventana principal

    #1era opción

    RegEmpresa=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registrarempresa.png')
    Boton1=Button(ventana1, text='regempresa', image=RegEmpresa, height ="62", width= "220", command=RegiEmpresa,borderwidth=0, highlightthickness=0)
    Boton1.place(x=125,y=10)

    #2da opción

    RegProducto=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registrarproducto.png')
    Boton2=Button(ventana1, text='regproducto', image=RegProducto, height ="62", width= "220", command=RegiProducto,borderwidth=0, highlightthickness=0)
    Boton2.place(x=125,y=82)

    #3era opción

    RegMovimiento=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/registrarmovimiento.png')
    Boton3=Button(ventana1, text='regmovimiento', image=RegMovimiento, height ="62", width= "220", command=RegiMovimiento,borderwidth=0, highlightthickness=0)
    Boton3.place(x=125,y=152)

    #4ta opción

    KardexUnitario=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/kardexunitario.png')
    Boton4=Button(ventana1, text='kardexunitario', image=KardexUnitario, height ="62", width= "220", command=VerKardexUnitario,borderwidth=0, highlightthickness=0)
    Boton4.place(x=125,y=221)

    #5ta opción

    KardexTotal=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/kardextotal.png')
    Boton5=Button(ventana1, text='kardextotal', image=KardexTotal, height ="62", width= "220", command=VerKardexTotal,borderwidth=0, highlightthickness=0)
    Boton5.place(x=125,y=292)

    #6ta opción

    EliminarRegistros=PhotoImage(file='C:/Users/Jeicoll/Desktop/Python/Proyectos Python/Kárdex/Logos/eliminarregistros.png')
    Boton6=Button(ventana1, text='regempresa', image=EliminarRegistros, height ="62", width= "220", command=EliminaRegistros,borderwidth=0, highlightthickness=0)
    Boton6.place(x=125,y=363)
    ventana1.mainloop()

FuncionPrincipal()