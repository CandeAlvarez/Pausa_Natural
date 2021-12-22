# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './Visual/ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pausa_Natural(object):
    def setupUi(self, Pausa_Natural):
        Pausa_Natural.setObjectName("Pausa_Natural")
        Pausa_Natural.resize(695, 560)
        self.widget_central = QtWidgets.QWidget(Pausa_Natural)
        self.widget_central.setObjectName("widget_central")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_central)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.tabs = QtWidgets.QTabWidget(self.widget_central)
        self.tabs.setObjectName("tabs")
        self.Nuevo = QtWidgets.QWidget()
        self.Nuevo.setObjectName("Nuevo")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Nuevo)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.Nuevo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_cliente = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cliente.sizePolicy().hasHeightForWidth())
        self.label_cliente.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_cliente.setFont(font)
        self.label_cliente.setObjectName("label_cliente")
        self.horizontalLayout_5.addWidget(self.label_cliente)
        self.texto_cliente = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.texto_cliente.setFont(font)
        self.texto_cliente.setEditable(True)
        self.texto_cliente.setObjectName("texto_cliente")
        self.horizontalLayout_5.addWidget(self.texto_cliente)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.caja_basicos = QtWidgets.QVBoxLayout()
        self.caja_basicos.setObjectName("caja_basicos")
        self.lista_basicos_L = QtWidgets.QGroupBox(self.Nuevo)
        self.lista_basicos_L.setObjectName("lista_basicos_L")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.lista_basicos_L)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lista_basicos = QtWidgets.QVBoxLayout()
        self.lista_basicos.setObjectName("lista_basicos")
        self.verticalLayout_7.addLayout(self.lista_basicos)
        self.caja_basicos.addWidget(self.lista_basicos_L)
        self.horizontalLayout.addLayout(self.caja_basicos)
        self.caja_adicionales = QtWidgets.QVBoxLayout()
        self.caja_adicionales.setObjectName("caja_adicionales")
        self.lista_adicionales_L = QtWidgets.QGroupBox(self.Nuevo)
        self.lista_adicionales_L.setObjectName("lista_adicionales_L")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.lista_adicionales_L)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lista_adicionales = QtWidgets.QVBoxLayout()
        self.lista_adicionales.setObjectName("lista_adicionales")
        self.verticalLayout_10.addLayout(self.lista_adicionales)
        self.caja_adicionales.addWidget(self.lista_adicionales_L)
        self.horizontalLayout.addLayout(self.caja_adicionales)
        self.caja_doble = QtWidgets.QVBoxLayout()
        self.caja_doble.setObjectName("caja_doble")
        self.lista_doble_L = QtWidgets.QGroupBox(self.Nuevo)
        self.lista_doble_L.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lista_doble_L.setFlat(False)
        self.lista_doble_L.setCheckable(False)
        self.lista_doble_L.setObjectName("lista_doble_L")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.lista_doble_L)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.lista_doble = QtWidgets.QVBoxLayout()
        self.lista_doble.setObjectName("lista_doble")
        self.verticalLayout_12.addLayout(self.lista_doble)
        self.caja_doble.addWidget(self.lista_doble_L)
        self.horizontalLayout.addLayout(self.caja_doble)
        self.caja_precio_L = QtWidgets.QGroupBox(self.Nuevo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.caja_precio_L.sizePolicy().hasHeightForWidth())
        self.caja_precio_L.setSizePolicy(sizePolicy)
        self.caja_precio_L.setAutoFillBackground(False)
        self.caja_precio_L.setFlat(False)
        self.caja_precio_L.setObjectName("caja_precio_L")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.caja_precio_L)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.caja_precio = QtWidgets.QVBoxLayout()
        self.caja_precio.setObjectName("caja_precio")
        self.verticalLayout_14.addLayout(self.caja_precio)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_14.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.caja_precio_L)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.boton_agregar_pedido = QtWidgets.QPushButton(self.Nuevo)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.boton_agregar_pedido.setPalette(palette)
        self.boton_agregar_pedido.setObjectName("boton_agregar_pedido")
        self.verticalLayout_4.addWidget(self.boton_agregar_pedido)
        self.tabs.addTab(self.Nuevo, "")
        self.Resumen = QtWidgets.QWidget()
        self.Resumen.setObjectName("Resumen")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Resumen)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.Resumen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 657, 421))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.res_ingredientes = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_ingredientes.sizePolicy().hasHeightForWidth())
        self.res_ingredientes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.res_ingredientes.setFont(font)
        self.res_ingredientes.setFrameShape(QtWidgets.QFrame.Box)
        self.res_ingredientes.setText("")
        self.res_ingredientes.setObjectName("res_ingredientes")
        self.horizontalLayout_8.addWidget(self.res_ingredientes)
        self.res_cubiertos = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.res_cubiertos.sizePolicy().hasHeightForWidth())
        self.res_cubiertos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.res_cubiertos.setFont(font)
        self.res_cubiertos.setFrameShape(QtWidgets.QFrame.Box)
        self.res_cubiertos.setText("")
        self.res_cubiertos.setObjectName("res_cubiertos")
        self.horizontalLayout_8.addWidget(self.res_cubiertos)
        self.ganancia = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ganancia.sizePolicy().hasHeightForWidth())
        self.ganancia.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ganancia.setFont(font)
        self.ganancia.setFrameShape(QtWidgets.QFrame.Box)
        self.ganancia.setText("")
        self.ganancia.setObjectName("ganancia")
        self.horizontalLayout_8.addWidget(self.ganancia)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_9.addWidget(self.scrollArea_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_9.addItem(spacerItem2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.tabs.addTab(self.Resumen, "")
        self.Listado = QtWidgets.QWidget()
        self.Listado.setObjectName("Listado")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Listado)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.grupo_fecha = QtWidgets.QGroupBox(self.Listado)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grupo_fecha.sizePolicy().hasHeightForWidth())
        self.grupo_fecha.setSizePolicy(sizePolicy)
        self.grupo_fecha.setObjectName("grupo_fecha")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.grupo_fecha)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.fecha_consulta = QtWidgets.QDateEdit(self.grupo_fecha)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fecha_consulta.sizePolicy().hasHeightForWidth())
        self.fecha_consulta.setSizePolicy(sizePolicy)
        self.fecha_consulta.setCalendarPopup(True)
        self.fecha_consulta.setDate(QtCore.QDate(2019, 1, 1))
        self.fecha_consulta.setObjectName("fecha_consulta")
        self.horizontalLayout_7.addWidget(self.fecha_consulta)
        self.boton_hoy = QtWidgets.QPushButton(self.grupo_fecha)
        self.boton_hoy.setObjectName("boton_hoy")
        self.horizontalLayout_7.addWidget(self.boton_hoy)
        self.verticalLayout.addWidget(self.grupo_fecha)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Listado)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 657, 371))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.grilla_pedidos = QtWidgets.QGridLayout()
        self.grilla_pedidos.setObjectName("grilla_pedidos")
        self.verticalLayout_6.addLayout(self.grilla_pedidos)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.enviar_captura = QtWidgets.QPushButton(self.Listado)
        self.enviar_captura.setObjectName("enviar_captura")
        self.verticalLayout.addWidget(self.enviar_captura)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.tabs.addTab(self.Listado, "")
        self.Clientes = QtWidgets.QWidget()
        self.Clientes.setObjectName("Clientes")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Clientes)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nombre_cli = QtWidgets.QLineEdit(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nombre_cli.setFont(font)
        self.nombre_cli.setObjectName("nombre_cli")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nombre_cli)
        self.label_4 = QtWidgets.QLabel(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.apellido_cli = QtWidgets.QLineEdit(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.apellido_cli.setFont(font)
        self.apellido_cli.setObjectName("apellido_cli")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.apellido_cli)
        self.label_5 = QtWidgets.QLabel(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.dir_cli = QtWidgets.QLineEdit(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dir_cli.setFont(font)
        self.dir_cli.setObjectName("dir_cli")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dir_cli)
        self.label_11 = QtWidgets.QLabel(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.tel_cli = QtWidgets.QLineEdit(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tel_cli.setFont(font)
        self.tel_cli.setObjectName("tel_cli")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.tel_cli)
        self.boton_agregar_cliente = QtWidgets.QPushButton(self.Clientes)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 236, 99))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.boton_agregar_cliente.setPalette(palette)
        self.boton_agregar_cliente.setObjectName("boton_agregar_cliente")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.boton_agregar_cliente)
        self.label_12 = QtWidgets.QLabel(self.Clientes)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.cubiertos_cli = QtWidgets.QVBoxLayout()
        self.cubiertos_cli.setObjectName("cubiertos_cli")
        self.formLayout_2.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.cubiertos_cli)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.tabs.addTab(self.Clientes, "")
        self.clientes = QtWidgets.QWidget()
        self.clientes.setObjectName("clientes")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.clientes)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boton_editar = QtWidgets.QPushButton(self.clientes)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boton_editar.sizePolicy().hasHeightForWidth())
        self.boton_editar.setSizePolicy(sizePolicy)
        self.boton_editar.setObjectName("boton_editar")
        self.verticalLayout_2.addWidget(self.boton_editar)
        self.scrollArea = QtWidgets.QScrollArea(self.clientes)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 657, 427))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.grilla_clientes = QtWidgets.QGridLayout()
        self.grilla_clientes.setObjectName("grilla_clientes")
        self.verticalLayout_3.addLayout(self.grilla_clientes)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabs.addTab(self.clientes, "")
        self.verticalLayout_11.addWidget(self.tabs)
        self.mensaje = QtWidgets.QLabel(self.widget_central)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mensaje.setFont(font)
        self.mensaje.setText("")
        self.mensaje.setObjectName("mensaje")
        self.verticalLayout_11.addWidget(self.mensaje)
        Pausa_Natural.setCentralWidget(self.widget_central)

        self.retranslateUi(Pausa_Natural)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Pausa_Natural)

    def retranslateUi(self, Pausa_Natural):
        _translate = QtCore.QCoreApplication.translate
        Pausa_Natural.setWindowTitle(_translate("Pausa_Natural", "Pausa Natural"))
        self.label_cliente.setText(_translate("Pausa_Natural", "Cliente"))
        self.lista_basicos_L.setTitle(_translate("Pausa_Natural", "Ingredientes BÁSICOS"))
        self.lista_adicionales_L.setTitle(_translate("Pausa_Natural", "Ingredientes ADICIONALES"))
        self.lista_doble_L.setTitle(_translate("Pausa_Natural", "Doble"))
        self.boton_agregar_pedido.setText(_translate("Pausa_Natural", "Agregar"))
        self.tabs.setTabText(self.tabs.indexOf(self.Nuevo), _translate("Pausa_Natural", "Nuevo Pedido"))
        self.tabs.setTabText(self.tabs.indexOf(self.Resumen), _translate("Pausa_Natural", "Resumen Ingredientes"))
        self.fecha_consulta.setDisplayFormat(_translate("Pausa_Natural", "dd/MM/yyyy"))
        self.boton_hoy.setText(_translate("Pausa_Natural", "HOY"))
        self.enviar_captura.setText(_translate("Pausa_Natural", "Enviar Listado de Pedidos"))
        self.tabs.setTabText(self.tabs.indexOf(self.Listado), _translate("Pausa_Natural", "Listado de Pedidos"))
        self.label_3.setText(_translate("Pausa_Natural", "Nombre"))
        self.label_4.setText(_translate("Pausa_Natural", "Apellido"))
        self.label_5.setText(_translate("Pausa_Natural", "Dirección"))
        self.label_11.setText(_translate("Pausa_Natural", "Teléfono"))
        self.boton_agregar_cliente.setText(_translate("Pausa_Natural", "Agregar"))
        self.label_12.setText(_translate("Pausa_Natural", "Cubiertos"))
        self.tabs.setTabText(self.tabs.indexOf(self.Clientes), _translate("Pausa_Natural", "Agregar Cliente"))
        self.boton_editar.setText(_translate("Pausa_Natural", "Editar Clientes"))
        self.tabs.setTabText(self.tabs.indexOf(self.clientes), _translate("Pausa_Natural", "Listado Clientes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pausa_Natural = QtWidgets.QMainWindow()
    ui = Ui_Pausa_Natural()
    ui.setupUi(Pausa_Natural)
    Pausa_Natural.show()
    sys.exit(app.exec_())
