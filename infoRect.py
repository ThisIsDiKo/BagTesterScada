from PyQt5. QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.Qt import QTimer


class InfoSquad(QWidget):
    def __init__(self):
        super(InfoSquad, self).__init__()

        self.id = 0
        self.stringName = 0
        self.currentValue = 0
        self.startValue = 0

        self.lblCurrentVal = QLabel('<--->')
        self.lblStartVal = QLabel('-----')
        self.lblName = QLabel('No name')

        self.container = QWidget(self)
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.lblStartVal, alignment=Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.lblCurrentVal, alignment=Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.lblName, alignment=Qt.AlignCenter)

        self.container.setLayout(self.vBoxLayout)
        self.container.setStyleSheet("background-color:red;border-radius: 10px;")
        self.container.setMaximumSize(200, 200)
        self.containerLayout = QVBoxLayout()
        self.containerLayout.addWidget(self.container)
        self.setLayout(self.containerLayout)

    def set_name(self, name):
        self.stringName = str(name)
        self.lblName.setText(self.stringName)

    def set_start_val(self, val):
        self.startValue = str(val)
        self.lblStartVal.setText(self.startValue)

    def set_current_val(self, val):
        self.currentValue = str(val)
        self.lblCurrentVal.setText(self.currentValue)

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ex = InfoSquad()
    ex.show()
    sys.exit(app.exec_())
