from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("MainDesign.ui", self)  
        self.show()
        
        self.pushButton_4.clicked.connect(self.open2)
        self.pushButton_5.clicked.connect(self.open3)

    def open2(self):
        self.new_window = AgregarPWindow(self)
        self.new_window.show()
    
    def open3(self):
        self.new_window = HorarioWindow(self)
        self.new_window.show()

class AgregarPWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AgregarPWindow, self).__init__(parent)
        uic.loadUi("AgregarP.ui", self)
        # Agregar un botón de cierre
        
        self.pushButtonBack.clicked.connect(self.close)
        self.BotonGuardar.clicked.connect(self.save_lines)
        self.show()
   
    def save_lines(self):
        print("Profesor guardado: ",self.lineEdit.text())
        print("De",self.tiempo1.text(), "a",self.tiempo2.text())
        print("Materia: ", self.lineEdit2.text())

class HorarioWindow(QMainWindow):
    def __init__(self, parent=None):
        super(HorarioWindow, self).__init__(parent)
        uic.loadUi("HorarioWindow.ui", self)

        # Agregar un botón de cierre
        self.pushButtonBack.clicked.connect(self.close)
        
        self.show()


    


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()





if __name__ == "__main__":
    main()
