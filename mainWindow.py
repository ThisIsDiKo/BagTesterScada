from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QImage, QPainter, QPalette, QPixmap
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QLabel,
        QMainWindow, QMenu, QMessageBox, QScrollArea, QSizePolicy, QLineEdit, QComboBox, QPushButton,
                             QHBoxLayout, QVBoxLayout, QWidget)

import numpy
from dxfwrite import DXFEngine as dxf
import configparser

import yaml


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Инициализация файла конфигурации
        #


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


if __name__ == '__main__':
    prepare_yaml()

