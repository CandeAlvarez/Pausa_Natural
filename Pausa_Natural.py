from Visual.ventana import *
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QCheckBox, QTextEdit, QLineEdit, QGroupBox, QRadioButton, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox, QGridLayout, QLabel,QFrame
from PyQt5.QtGui import QColor, QFont,QPixmap, QRegion
from PyQt5.QtCore import QDate, Qt, QPoint
# from PyQt5.QtCore.Qt import MatchStartsWith
from Database import *
from datetime import date
from Logica_Widgets.w_pedido import *
from Logica_Widgets.w_cliente import *

import sys

lst_adicionales = []
lst_basicos = []
lst_cubiertos = []
lst_checkboxes_basicos = []
lst_checkboxes_dobles = []
lst_checkboxes_adicionales = []
lst_checkboxes_cubiertos = []
lst_pedidos_dia = []
precios = [160,180,200]
lst_checkboxes_precios = []
precio_manual = []
clientes = []
lst_widgets = []
editando = []

cant_cols_pedidos = 7

class MainWindow(QtWidgets.QMainWindow,Ui_Pausa_Natural):
    
    #Init: agrega todos los widgets visuales necesarios
    
    def __init__(self, *args, **kwargs):
                
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        self.setupUi(self)
        lst_pedidos_dia = []
        
        #Vincula el boton con el listenerfrom datetime import date
        self.boton_agregar_pedido.clicked.connect(self.agregar_pedido)
        self.boton_agregar_cliente.clicked.connect(self.agregar_cliente)        
        self.tabs.currentChanged.connect(self.cambiar_tab)
        self.fecha_consulta.dateChanged.connect(self.mostrar_pedidos)
        self.boton_hoy.clicked.connect(self.setear_hoy)
        self.boton_editar.clicked.connect(self.tab_clientes)
        self.enviar_captura.clicked.connect(self.capturar_pantalla)
        
        self.texto_cliente.setDuplicatesEnabled(False)
        self.texto_cliente.setCurrentText("")
        
        self.agregar_nombres()         
        self.setear_hoy()
        
        self.obtener_nombres()
        
        self.agregar_botones_visuales()
        
        editando.append(False)
        
        self.limpiar_nombre()
        
    def tab_clientes(self):

        if editando[0]:
            self.mostrar_clientes()
        else:
            self.editar_clientes()
            
        editando[0] = not editando[0]

            
    
    def agregar_botones_visuales(self):
        #Agrega los botones visuales
        for ing in lst_basicos:
            checkbox = QCheckBox(ing)
            checkbox.clicked.connect(self.estimar_precio)
            self.lista_basicos.addWidget(checkbox)
            lst_checkboxes_basicos.append(checkbox)

        for ing in lst_adicionales:
            checkbox = QCheckBox(ing)
            checkbox.clicked.connect(self.estimar_precio)
            self.lista_adicionales.addWidget(checkbox)
            lst_checkboxes_adicionales.append(checkbox)
            check2 = QCheckBox(" ")
            check2.clicked.connect(self.estimar_precio)
            self.lista_doble.addWidget(check2)
            lst_checkboxes_dobles.append(check2)
        
        #Al ayout creado en QT designer se le agrega como widget el grupo de botones
        #El grupo de botones tiene, a su vez, otro layout para contener a los botones en sí
        
        lay_cubiertos = QVBoxLayout()
        grupo_cubiertos = QGroupBox("")
        for c in lst_cubiertos:
            b = QRadioButton(c)
            lay_cubiertos.addWidget(b)
            lst_checkboxes_cubiertos.append(b)
            
        grupo_cubiertos.setLayout(lay_cubiertos)
        self.cubiertos_cli.addWidget(grupo_cubiertos)
         
        
        lay_botones = QVBoxLayout()
        grupo_botones = QGroupBox("Precio")
        for p in precios:
            checkbox = QRadioButton(str(p))
            lay_botones.addWidget(checkbox)
            lst_checkboxes_precios.append(checkbox)
        
        otro = QRadioButton('Otro')
        lst_checkboxes_precios.append(otro)
        lay_botones.addWidget(otro)
        
        otro_precio = QLineEdit()
        lay_botones.addWidget(otro_precio)
        precio_manual.append(otro_precio)
        
        grupo_botones.setLayout(lay_botones)
        self.caja_precio.addWidget(grupo_botones)
        
    
    def obtener_nombres(self):
        #Obtiene los nombres de todos los ingredientes
        lst_ingredientes = Ingrediente.all()
        for i in lst_ingredientes:
            nombre = i.nombre
            if i.basico:
                lst_basicos.append(nombre)
            else:
                lst_adicionales.append(nombre)
                
        #Obtiene los nombres de los cubiertos
        lst_aux = Cubierto.all()
        for c in lst_aux:
            lst_cubiertos.append(c.nombre)
    
    
    ###### Funciones principales ######
    #       agregar_pedido 
    #       mostrar resumen 
    #       mostrar_pedidos 
    #       agregar_cliente 
    ################################### 
    
    
    def mostrar_resumen(self):
        
        fecha = date.today().strftime("%d/%m/%Y")
        pedidos = Pedido.query.filter(Pedido.fecha== fecha).all()
        
        precio_total = 0
        
        hash_ing = {}
        hash_cubiertos = {}
        
        for i in lst_basicos:
            hash_ing.update( {i : 0} )
            
        for i in lst_adicionales:
            hash_ing.update( {i : 0} )
            
        for c in lst_cubiertos:
            hash_cubiertos.update({c : 0})
                    
        for p in pedidos:
            lst_cantidades = p.asociaciones
            for a in p.asociaciones:
                hash_ing[a.ingrediente]+= a.cantidad
            tipo_cubierto = p.cliente.cubierto.nombre
            hash_cubiertos[tipo_cubierto]+=1
            precio_total += p.precio
            
        for a in hash_ing:
            if hash_ing[a]>0:
                print(a+"->"+str(hash_ing[a]))
        
        texto = "<body><div><br><b> RESUMEN DE INGREDIENTES </b> <p>"
        
        for ing in hash_ing:
            if hash_ing[ing] > 0:
                i = Ingrediente.query.filter(Ingrediente.nombre==ing).first()
                if i.cocido:
                    texto += "<span style=\"color: #FF4500;\">" + ing + " -----> " + str(hash_ing[ing]) + "</span><br>"
                else:
                    texto += ing + " -----> " + str(hash_ing[ing]) + "<br>"
    
        texto = texto[:-4]
        texto += "<br></div></body>"
        self.res_ingredientes.setText(texto)
        
        texto = "<body><div><b> <br> RESUMEN DE CUBIERTOS </b> <p>"
        
        for c in hash_cubiertos:
            if hash_cubiertos[c] > 0:
                texto += c + " -----> " + str(hash_cubiertos[c]) + "<br>"
        
        texto = texto[:-4]
        texto += "<br></div></body>"
        self.res_cubiertos.setText(texto)
        
        texto = "<body><div><b> <br> GANANCIA </b> $ " + str(precio_total) + "<br></div></body>"

        self.ganancia.setText(texto)
    
        
    def mostrar_pedidos(self):
        
        f = self.fecha_consulta.date()
        
        if f.day() < 9:
            dia = '0'+str(f.day())
        else:
            dia = str(f.day())
            
        if f.month() < 9:
           mes = '0'+str(f.month())    
        else:
            mes = str(f.month()) 

        fecha2 = dia + "/"+ mes + "/" +str( f.year() )
        
        for i in range(self.grilla_pedidos.count()): self.grilla_pedidos.itemAt(i).widget().close()

        pedidos = Pedido.query.filter(Pedido.fecha== fecha2).all()

        lst_widgets_pedido = []
        
        for p in pedidos:
            prueba = widget_pedido(p)
            prueba.borrado.connect(self.mostrar_pedidos)
            prueba.set_pedido()
            lst_widgets_pedido.append(prueba)
         
        cant = len(lst_widgets_pedido)

        for i in range(cant):
            fila = i//cant_cols_pedidos
            col = i % cant_cols_pedidos
            self.grilla_pedidos.addWidget(lst_widgets_pedido[i],fila,col)
    
    def editar_clientes(self):

        cant = self.grilla_clientes.count()
        
        for i in range(self.grilla_clientes.count()): self.grilla_clientes.itemAt(i).widget().close()
        
        clientes = Cliente.all()
        lst_widgets = []
        
        #####
        lst_widgets_cliente = []
        for c in clientes:
            aux = widget_cliente(c)
            aux.set_cliente()
            lst_widgets_cliente.append(aux)
        
        cant = len(lst_widgets_cliente)

        for i in range(cant):
            fila = i//5
            col = i % 5
            self.grilla_clientes.addWidget(lst_widgets_cliente[i],fila,col)
        
        #####
    
    
    def mostrar_clientes(self):
        
        for i in range(self.grilla_clientes.count()): self.grilla_clientes.itemAt(i).widget().close()

        clientes = Cliente.all()
        lst_widgets = []

        for c in clientes:
                
            nomb = c.nombre
            ape = c.apellido
            dire = c.direccion
            tel = c.telefono
            cub = c.cubierto.nombre
            
            texto = "<html><body><div><b>" + nomb + " " + ape  +"</b>" + "<p>"
            texto += "<b>Dirección: </b>"+ dire + "<br> <b>Teléfono: </b>" + tel + "<br> <b>Cubiertos: </b>" + cub + "</p></div></body></html>"
                            
            aux = QLabel()
            aux.setFrameShape(QFrame.Box)
            #aux.setReadOnly(True)
            
            aux.setText(texto)
            lst_widgets.append(aux)
        
        cant_clientes = len(clientes)
        
        for i in range(cant_clientes):
            fila = i//5
            col = i % 5
            self.grilla_clientes.addWidget(lst_widgets[i],fila,col)
    
    
    def agregar_cliente(self):
        nombre = self.nombre_cli.text()
        apellido = self.apellido_cli.text()
        direccion = self.dir_cli.text()
        telefono = self.tel_cli.text()
        
        cubiertos = ""
        for c in lst_checkboxes_cubiertos:
            if c.isChecked():
                cubiertos = c.text()
        
        if nombre == "" or apellido == "":
            self.mostrar_mensaje("Falta ingresar nombre y apellido del cliente")
            return
        
        if cubiertos == "":
            self.mostrar_mensaje("Falta seleccionar una preferencia de cubiertos")
            return
        
        #Crea un objeto de tipo Cliente
        obj_cubierto = Cubierto.find(cubiertos)
        
        aux = nombre+apellido
        
        res = [z for z in aux if z!=" " ]         
        
        alias = ""
        
        for z in res:
            alias += z
                        
        existe = Cliente.query.filter(Cliente.alias == alias).first()
        
        if existe is None:
            Cliente.create(alias=alias,nombre=nombre,apellido=apellido,direccion=direccion,telefono=telefono,cubierto=obj_cubierto)
            self.mostrar_mensaje("Cliente "+nombre+" "+apellido+" agregado exitosamente")
        else:
            self.mostrar_mensaje("El cliente ya existe")
        
        self.limpiar_cliente()
        self.limpiar_cubiertos()
   
    def agregar_pedido(self):
        
        fecha = date.today().strftime("%d/%m/%Y")
        precio = self.obtener_precio()
        lst_ing = self.obtener_ingredientes()
        cliente = self.obtener_cliente()
        
        if cliente is None or precio == 0 or lst_ing is None:
            print("Ocurrio algun error")
            return      
        
        
        p = Pedido.query.filter(Pedido.fecha==fecha, Pedido.cliente==cliente).first()
        
        if p is not None:
        
            resp = QMessageBox.question(
                self,
                "ATENCIÓN",
                "Ya existe un pedido en el día de la fecha para este cliente. ¿Desea agregar el pedido igualmente?"
            )
            
            if resp == QMessageBox.No:
                self.limpiar()
                return
        
        p=Pedido.create(fecha=fecha,cliente=cliente,precio=precio)
        for index, ing in enumerate(lst_ing):
                a = Ingrediente.find(ing)
                p.ingredientes.append(a)
                if not a.basico: #Los adicionales pueden tener doble cantidad
                    indice = lst_adicionales.index(ing)
                    if lst_checkboxes_dobles[indice].isChecked():
                        #print("entro con 2 - ingrediente"+ing)
                        p.asociaciones[index].cantidad = 2
                    else:
                        #print("entro con 1 - adicional . ingrediente" +ing)
                        p.asociaciones[index].cantidad = 1
                else:
                    #print("es basico")
                    p.asociaciones[index].cantidad = 1
                    
        p.save()
        
        print("Fecha guardado "+fecha)
       
        self.mostrar_mensaje("Pedido del cliente "+ cliente.nombre + " " + cliente.apellido + " agregado exitosamente")
        
        self.limpiar()
          
    ###### Funciones auxiliares ######
    #       cambiar_tab 
    #       obtener_cliente 
    #       obtener_precio 
    #       estimar_precio
    #       agregar_nombres
    #       mostrar_mensaje
    #       borrar_mensaje
    ################################### 
                
    def mostrar_mensaje(self,texto):
        self.mensaje.setText(texto)
    
    def borrar_mensaje(self):
        self.mensaje.setText("")
    
    def cambiar_tab(self,index):
        self.mostrar_mensaje("")
        
        if index == 0: #Tab agregar pedido
            self.agregar_nombres()
            self.limpiar_nombre()
        if index == 1: #Tab mostrar resumen
            self.mostrar_resumen() 
        if index == 2: #Tab mostrar pedidos
            self.mostrar_pedidos()
        if index == 4: #Tab mostrar clientes
            self.mostrar_clientes()
           
    def obtener_cliente(self):
        cliente = self.texto_cliente.currentText()
        c = None
        if cliente == "":
            print("falta cliente")
            self.mostrar_mensaje("Falta ingresar el cliente")
            return None
        else:                    
            lst_cliente = cliente.split()
            alias = cliente.replace(" ","")
            
            if len(lst_cliente) == 1 :
                self.mostrar_mensaje("Debe ingresar nombre y apellido del cliente")
                return None
        
            c = Cliente.find(alias)

            if c is None:
                    self.mostrar_mensaje("El cliente ingresado no existe")
                    return None
            else:
                return c
    
    def obtener_precio(self):
        marcado = 0
        res = ""
        
        for p in lst_checkboxes_precios:
            if p.isChecked():
                if p.text() == 'Otro':
                    res = precio_manual[0].text()
                else:
                    res = p.text()
                marcado += 1
                
        if marcado == 0:
            self.mostrar_mensaje("Falta seleccionar o indicar un precio")
            return 0
        
        if marcado == 1:
            if res.isdigit():
                self.borrar_mensaje()
                return int(res)
            else:
                self.mostrar_mensaje("El precio ingresado no es un valor numérico")
                return 0
    
    def obtener_ingredientes(self):
        lst_ing = []
                    
        for boton in lst_checkboxes_basicos:
            ing = boton.text()
            if boton.isChecked():
                lst_ing.append(ing)

        for boton in lst_checkboxes_adicionales:
            ing = boton.text()
            if boton.isChecked():
                lst_ing.append(ing)

        if len(lst_ing) == 0:
            self.mostrar_mensaje("Debe seleccionar los ingredientes")
            return None
        
        if len(lst_ing) > 6:
            self.mostrar_mensaje("Ha seleccionado más de 6 ingredientes")
            return None
    
        return lst_ing
    
    def estimar_precio(self):
        cant_b = 0
        cant_a = 0
        cant_d = 0
        
        for boton in lst_checkboxes_basicos:
            if boton.isChecked():
                cant_b += 1
                
        for boton in lst_checkboxes_adicionales:
            if boton.isChecked():
                cant_a += 1
        
        for boton in lst_checkboxes_dobles:
            if boton.isChecked():
                cant_d += 1
        
        if cant_a == 2:
            lst_checkboxes_precios[0].setChecked(True)

        if cant_a == 3:
            lst_checkboxes_precios[1].setChecked(True) 
            
        if cant_d == 2:
            lst_checkboxes_precios[2].setChecked(True) 
    
    def agregar_nombres(self):
        clientes = Cliente.all()
               
        self.texto_cliente.clear()       
        for c in clientes:
            texto = c.nombre + " " + c.apellido
            self.texto_cliente.insertItem(0,texto)
    
    def limpiar_ingredientes(self):
        for boton in lst_checkboxes_basicos:
            boton.setCheckState(0)
        for boton in lst_checkboxes_adicionales:
            boton.setCheckState(0)
        for boton in lst_checkboxes_dobles:
            boton.setCheckState(0)            
            
    def limpiar_nombre(self):        
        self.texto_cliente.setCurrentText("")
    
    def limpiar_cubiertos(self):
        for boton in lst_checkboxes_cubiertos:
           boton.setDown(0)
    
    def limpiar_cliente(self):
        self.nombre_cli.setText("")
        self.apellido_cli.setText("")
        self.dir_cli.setText("")
        self.tel_cli.setText("")
        
    def limpiar(self):
        self.limpiar_ingredientes()
        self.limpiar_nombre()
        
    def setear_hoy(self):
        f = date.today()
        fecha = QDate(f.year,f.month,f.day)
        self.fecha_consulta.setDate(fecha)
        self.mostrar_pedidos()        
         
    def capturar_pantalla(self):
        fecha = date.today().strftime("%d-%m-%Y")
        nombre = 'Imagenes_Pedidos/' + str(fecha) + '.jpg'
        print(nombre)
        aux = QPixmap(window.size()) 
        window.render(aux, QPoint(), QRegion())
        aux.save(nombre)
        
        sandbox = Enviar_Imagen(nombre)
    
#########################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #aux = QPixmap(window.size()) 
    #window.render(aux, QPoint(), QRegion())
    #aux.save("Hello.jpg")
    app.exec_()
