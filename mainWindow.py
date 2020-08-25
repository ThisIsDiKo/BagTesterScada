from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QLabel,
        QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy, QLineEdit, QComboBox, QPushButton,
                             QHBoxLayout, QVBoxLayout, QWidget, QGridLayout)

import numpy
from dxfwrite import DXFEngine as dxf
import configparser

from infoRect import InfoRect

import yaml
import logging

class FarmWidget(QWidget):
    def __init__(self):
        super(FarmWidget, self).__init__()
        # logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
        #                     datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)
        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        #Инициализация файла конфигурации
        #
        self.l = QGridLayout()

        self.listOfRects = []

        for i in range(4):
            s = InfoRect()
            s.set_current_val(0)
            s.set_id(i)
            s.set_start_val(0)
            s.set_name('1_{}'.format(i))
            self.listOfRects.append(s)

        s = InfoRect()
        s.set_current_val(0)
        s.set_id(i)
        s.set_start_val(0)
        s.set_name('1_{}'.format(i))

        self.l.addWidget(self.listOfRects[0], 0, 0)
        self.l.addWidget(self.listOfRects[1], 0, 1)
        self.l.addWidget(self.listOfRects[2], 1, 0)
        self.l.addWidget(self.listOfRects[3], 1, 1)
        logging.info('added widgets')
        #self.l.addWidget(QLabel("HUI"), 0, 0)

        self.setLayout(self.l)



def prepare_yaml():
    import io
    data = {
        'a list': [
            1,
            42,
            3.141,
            1337,
            'help',
            u'€'
        ],
        'a string': 'bla',
        'another dict': {
            'foo': 'bar',
            'key': 'value',
            'the answer': 42
        }
    }

    # Write YAML file
    with io.open('data.yaml', 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

def read_yaml():
    with open("config.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    print(data_loaded)
    if 'farms' in data_loaded.keys():
        print('norm keys')
    for i in range(len(data_loaded['farms'])):
        for key in data_loaded['farms'][i].keys():
            farm = data_loaded['farms'][i][key]
            print(farm['name'])
            print(farm['scan interval'])


if __name__ == '__main__':
    read_yaml()
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ex = FarmWidget()
    ex.show()
    ex.setWindowTitle("Отображение информации о системе")
    sys.exit(app.exec_())

