from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *

import sys, os

#-----------------------------------------------------------------------------------------

class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		loadUi('UIFormNotepad.ui', self)

		self.SONDART_NAME = 'untitled.py'

		self.logicUi()
		self.show()

	def logicUi(self):
#		self.atn_new.triggered.connect(lambda:)
		self.atn_open.triggered.connect(lambda: self.func_open())
		self.atn_save_as.triggered.connect(lambda: self.func_save_as())
#		self.atn_to_close.triggered.connect(lambda:)

	def func_open(self):
		filepath = QFileDialog.getSaveFileName(self, 'Сохранение файла', self.SONDART_NAME)[0]

		with open(filepath, 'r') as file:
			file.write(self.plainTextEdit_1.toPlainText())

	def func_save_as(self):
		filepath = QFileDialog.getSaveFileName(self, 'Сохранение файла', self.SONDART_NAME)[0]
		filename = filepath.split('/')[-1]
		if filename.split('.')[0] != '':
			if not ('py' in filename.split('.')):
				filename = '{filename.split(".")[0]}.py'
		else:
			filename = self.SONDART_NAME

		with open(str(filepath.split('/')[:-1] + '/' + filename), 'w') as file:
			file.write(self.plainTextEdit_1.toPlainText())
		print(filepath.split('/')[:-1] + filename)

#-----------------------------------------------------------------------------------------

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec_())
