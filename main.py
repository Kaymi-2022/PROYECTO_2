import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QTableWidgetItem
from PyQt6.QtGui import * 
from PyQt6 import uic,QtWidgets
import funciones as op

class Ejemplo01(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("formulario.ui",self)
        self.initUi()
    
    def initUi(self):

        nombreColumnas=("CATEGORIA","NOMBRES Y APELLIDOS","OCUPACION","SUELDO","DESCUENTO 1","DESCUENTO 2", "BONIFICACION 1","BONIFICACION 2")
        self.twgdata.setColumnWidth(0,120)
        self.twgdata.setColumnWidth(1,350)
        self.twgdata.setColumnWidth(2,100)
        self.twgdata.setColumnWidth(3,100)
        self.twgdata.setColumnWidth(4,200)
        self.twgdata.setColumnWidth(5,200)
        self.twgdata.setColumnWidth(6,200)
        self.twgdata.setColumnWidth(7,200)
        self.twgdata.setHorizontalHeaderLabels(nombreColumnas)
        self.b_nuevo.clicked.connect(self.reset)
        self.b_registrar.clicked.connect(self.registrar)
        self.b_actualizar.clicked.connect(self.actualizar)
        self.b_salir.clicked.connect(self.salir)
        categoria=["A","B","C","D","E"]
        for i in categoria:
            self.cb_categoria.addItem(i)
    
    def reset(self):
        self.txt_codigo.setText("")
        self.txt_apellidos.setText("")
        self.txt_nombres.setText("")
        self.lb_datos.setText("")
        self.lb_codigo.setText("")
        self.lb_ocupacion.setText("")
        self.lb_sueldo.setText("")
        self.lb_descuento1.setText("")
        self.lb_descuento2.setText("")
        self.lb_bonificacion1.setText("")
        self.lb_bonificacion2.setText("")
        self.cb_categoria.setCurrentIndex(0)

    def registrar(self):
        categoria=self.cb_categoria.itemText(self.cb_categoria.currentIndex())
        dato="Estudiante: "
        dato+=self.txt_nombres.text()+ " "
        dato+=self.txt_apellidos.text()
        self.lb_datos.setText(dato.upper())
        codigo="Codigo: "
        codigo+=self.txt_codigo.text()
        self.lb_codigo.setText(codigo)
        self.lb_ocupacion.setText(op.vocupacion(categoria))
        self.lb_sueldo.setText(str(round(op.vsueldo(categoria),2)))
        self.lb_descuento1.setText(op.vdescuento1(categoria))
        self.lb_descuento2.setText(op.vdescuento2(categoria))
        self.lb_bonificacion1.setText(op.vbonificacion1(categoria))
        self.lb_bonificacion2.setText(op.vbonificacion2(categoria))
        
    def actualizar(self):
        categoria=self.cb_categoria.itemText(self.cb_categoria.currentIndex())
        datos=self.txt_nombres.text()+ " "
        datos+=self.txt_apellidos.text()
        ocupacion=self.lb_ocupacion.text()
        sueldo=self.lb_sueldo.text()
        desc1=self.lb_descuento1.text()
        desc2=self.lb_descuento2.text()
        bono1=self.lb_bonificacion1.text()
        bono2=self.lb_bonificacion2.text()


        
        op.IngresoDatos(categoria,datos.upper(),ocupacion,sueldo,desc1,desc2,bono1,bono2)
        data=[{"CATEGORIA":op.listado[0],"NOMBRES Y APELLIDOS":op.listado[1],
            "OCUPACION":op.listado[2],"SUELDO":op.listado[3],
            "DESCUENTO 1":op.listado[4],"DESCUENTO 2":op.listado[5],
            "BONIFICACION 1":op.listado[6],"BONIFICACION 2":op.listado[7]}]
        indicefila=self.twgdata.rowCount()
        self.twgdata.insertRow(indicefila)
        
        for dato in data:
            self.twgdata.setItem(indicefila,0,QtWidgets.QTableWidgetItem(dato["CATEGORIA"]))
            self.twgdata.setItem(indicefila,1,QtWidgets.QTableWidgetItem(str(dato["NOMBRES Y APELLIDOS"])))
            self.twgdata.setItem(indicefila,2,QtWidgets.QTableWidgetItem(str(dato["OCUPACION"])))
            self.twgdata.setItem(indicefila,3,QtWidgets.QTableWidgetItem(str(dato["SUELDO"])))
            self.twgdata.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(dato["DESCUENTO 1"])))
            self.twgdata.setItem(indicefila,5,QtWidgets.QTableWidgetItem(str(dato["DESCUENTO 2"])))
            self.twgdata.setItem(indicefila,6,QtWidgets.QTableWidgetItem(str(dato["BONIFICACION 1"])))
            self.twgdata.setItem(indicefila,7,QtWidgets.QTableWidgetItem(str(dato["BONIFICACION 2"])))
            indicefila+=1
        op.listado.clear()
    
    def salir(self):
        self.close()
            
    


if __name__=='__main__':
    app = QApplication(sys.argv)
    ventana1=Ejemplo01()
    ventana1.show()
    sys.exit(app.exec())
