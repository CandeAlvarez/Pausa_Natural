from PyQt5.QtWidgets import QCheckBox, QTextEdit, QLineEdit, QGroupBox, QRadioButton, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QColor, QFont
from Database.crear_bd import *
from datetime import date
from Visual.widget_pedido import *
from PyQt5.QtCore import QObject, pyqtSignal

hash_clicks = {}


class widget_pedido(QtWidgets.QWidget,Ui_widget_pedido):
    
    borrado = pyqtSignal()
    
    #Init: agrega todos los widgets visuales necesarios
    def __init__(self,pedido, *args, **kwargs):
        self.pedido_global = pedido
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
    def set_pedido(self):
       
        cliente = self.pedido_global.cliente.nombre + " " + self.pedido_global.cliente.apellido
        precio = "Precio: $" + str(self.pedido_global.precio)
        cubierto =  self.pedido_global.cliente.cubierto.nombre
        
        #Color naranja
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        
        ##Fuente negrita
        negrita = QtGui.QFont()
        negrita.setBold(True)
        
        self.label_cliente.setFont(negrita)
        #self.label_cubierto.setFont(negrita)
        
        self.label_cliente.setText(cliente)
        self.label_precio.setText(precio)
        self.label_cubierto.setText(cubierto)
        self.lista_ing.itemDoubleClicked.connect(self.cambiar_estilo)
        self.lista_ing.itemClicked.connect(self.limpiar)
        self.boton_eliminar.clicked.connect(self.eliminar_pedido)
        
                  
        lst_cantidades = self.pedido_global.asociaciones
        for a in lst_cantidades:
            item = QListWidgetItem()  
            ing = Ingrediente.find(a.ingrediente)
            if ing.cocido:
                item.setForeground(brush)
            texto = ing.nombre
            if a.cantidad == 2:
                texto += "    (x2)"
            item.setText(texto)
            hash_clicks.update( {ing.nombre : False} )
            
            self.lista_ing.addItem(item)  

    
    def limpiar(self):
        self.lista_ing.clearSelection()
    
    def eliminar_pedido(self):
        resp = QMessageBox.question(
            self,
            "ATENCIÓN",
            "ELIMINAR pedido?"
        )
        
        if resp == QMessageBox.No:
            return
        
        print(self.pedido_global)
        self.pedido_global.delete()
        self.hide()
        self.borrado.emit()
    
    def cambiar_estilo(self, item):
        texto = item.text().split()
        click = hash_clicks[texto[0]]
        
        if not click:
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)
            hash_clicks[texto[0]] = True
        else:
            hash_clicks[texto[0]] = False
            brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)

        self.lista_ing.clearSelection()
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = widget_p()
    window.show()
    app.exec_()
        
       
