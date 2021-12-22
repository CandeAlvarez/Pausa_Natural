from PyQt5.QtWidgets import QCheckBox, QTextEdit, QLineEdit, QGroupBox, QRadioButton, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QColor, QFont
from Database.crear_bd import *
from datetime import date
from Visual.widget_cliente import *
from PyQt5.QtCore import QObject, pyqtSignal

lst_cubiertos = []



class widget_cliente(QtWidgets.QWidget,Ui_widget_cliente):
    
    
    #Init: agrega todos los widgets visuales necesarios
    def __init__(self,cliente, *args, **kwargs):
        self.cliente_global = cliente
        self.lst_checkboxes_cubiertos = []
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar_cambios)
        self.boton_eliminar.clicked.connect(self.eliminar_cliente)
        
        lst_cubiertos = Cubierto.all()
        
        #Al layout creado en QT designer se le agrega como widget el grupo de botones
        #El grupo de botones tiene, a su vez, otro layout para contener a los botones en sí
        
        lay_cubiertos = QVBoxLayout()
        grupo_cubiertos = QGroupBox("")
        for c in lst_cubiertos:
            b = QRadioButton(c.nombre)
            lay_cubiertos.addWidget(b)
            self.lst_checkboxes_cubiertos.append(b)
            
        grupo_cubiertos.setLayout(lay_cubiertos)
        self.cubiertos.addWidget(grupo_cubiertos)
        

    def set_cliente(self):
        
        ##Fuente negrita
        negrita = QtGui.QFont()
        negrita.setBold(True)
        
        self.label_1.setFont(negrita)
        self.label_2.setFont(negrita)
        self.label_3.setFont(negrita)
        self.label_4.setFont(negrita)
        
        self.apellido.setText(self.cliente_global.apellido)
        self.nombre.setText(self.cliente_global.nombre)
        self.dire.setText(self.cliente_global.direccion)
        self.tel.setText(self.cliente_global.telefono)
        
        nomb_cubierto = self.cliente_global.cubierto.nombre
        
        #print("El cliente "+self.cliente_global.nombre+" tiene cubiertos: "+nomb_cubierto)
        
        for w in self.lst_checkboxes_cubiertos:
            if w.text() == nomb_cubierto:
                w.setChecked(True)
        

    def guardar_cambios(self):
        n = self.nombre.text()
        a = self.apellido.text()
        d = self.dire.text()
        t = self.tel.text()
        
        cubiertos = ""
        for c in self.lst_checkboxes_cubiertos:
            if c.isChecked():
                cubiertos = c.text()
                
        obj_cubierto = Cubierto.find(cubiertos)

        self.cliente_global.update(nombre=n,apellido=a,direccion=d,telefono=t,cubierto=obj_cubierto)
        print("Guardando")

        
    def eliminar_cliente(self):
        resp = QMessageBox.question(
            self,
            "ATENCIÓN",
            "Segura que desea eliminar el cliente?"
        )
        
        if resp == QMessageBox.No:
            return
        
        self.cliente_global.delete()
        self.hide()                
            

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = widget_p()
    window.show()
    app.exec_()
        
       
