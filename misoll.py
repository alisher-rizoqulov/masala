from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
class chiqar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250,250)

        self.ism=QLabel("Ism:",self)
        self.ism.move(20,20)

        self.ism_e = QLineEdit(self)
        self.ism_e.move(60,20)
       

        self.fam=QLabel("Fam:",self)
        self.fam.move(20,50)

        self.fam_e=QLineEdit(self)
        self.fam_e.move(60,50)
        

        self.yosh=QLabel("Yosh:",self)
        self.yosh.move(20,80)

        self.yosh_e=QLineEdit(self)
        self.yosh_e.move(60,80)
       



app = QApplication([])
win = chiqar()
win.show()
app.exec_()