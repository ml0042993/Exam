import sys,os,re,xlrd
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QAbstractItemView
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import QCheckBox,QRadioButton


from ui_MainWindow import Ui_MainWindow



class QmyMainWindow(QMainWindow):
	def __init__(self,parent=None):
		super().__init__(parent)#调用父类构造函数,创建窗体
		self.ui = Ui_MainWindow()#创建Ui对象
		self.ui.setupUi(self)#构造UI
		self.ui.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.BASE_PATH = os.getcwd()
		self.itemModel = QStandardItemModel(self)
		self.item_Model = QStandardItemModel(self)

		self.__CheckedFlags = Qt.Checked

	def __Excle_init(self):

		self.excle_book = xlrd.open_workbook(self.Open_File_path)
		self.excle_sheetnames = self.excle_book.sheet_names()#获取excle的sheet名称
		self.__InitModelRaido()
		self.__groupbox4_init()
		self.__Excle_api(self.excle_sheetnames[0])
	def __Excle_api(self,sheetname):
		self.item_list=[]
		excle_sheet = self.excle_book.sheet_by_name(sheetname)
		self.rows = excle_sheet.nrows

		for i in range(self.rows):
			original_table = excle_sheet.row_values(i)
			original_table[0] = "第" + str(original_table[0]) + "题"
			original_table = [str(j) for j in original_table]
			self.item_list.append(original_table)
		print(self.item_list)
		self.__InitModelExcle()
	def __InitModelRaido(self):
		Count_Row = len(self.excle_sheetnames)
		for i in range(Count_Row):
			item = QStandardItem(self.excle_sheetnames[i])
			self.itemModel.setItem(0, i, item)

	def __InitModelExcle(self):
		Count_Row = len(self.item_list)
		for i in range(Count_Row):
			Count_Col = len(self.item_list[i])#Count_Col是二维列表内的列表的长度
			for j in range(Count_Col):
				item_model = QStandardItem(self.item_list[i][j])
				self.item_Model.setItem(i,j,item_model)
		self.ui.listView.setModel(self.item_Model)
	def on_listView_clicked(self,index):
		# print(index)
		try:
			self.ui.lineEdit.clear()

			self.__Signal = index.row()
			for i in self.ui.groupBox_2.children():
				if type(i) == QCheckBox:
					i.deleteLater()#删除checkBox组件
			item = self.item_Model.item(self.__Signal,2)#获取题目的单元格的QStandardItem对象
			self.__Title = item.text()#
			self.__TYPE = self.item_Model.item(self.__Signal,2).text()#题目类型的文本
			self.ui.lineEdit.setText(self.__Title)#给文本框设置文字

			Column = self.item_Model.columnCount()#获取二维列表的长度
			for i in range(3,7):
				item = self.item_Model.item(self.__Signal,i)#遍历二级列表内的元素
				try:
					anchor = item.text()
					print(anchor)
					checkName = "chk_{}_{}".format(self.__Signal,i)
					self.__CreateChecked(checkName,anchor)#按照选项个数动态生成生成复选框
				except AttributeError:
					break
		except AttributeError:
			return
	def __CreateChecked(self,checkName,checkText):
		'''
		创建复选框
		:param checkName: 复选框的objectName
		:param checkText: 复选框的文本内容
		:return:
		'''
		self.chk = QCheckBox(self.ui.groupBox_2)#在groupBox_2内实例化复选框
		self.chk.setObjectName(checkName)#设置名称
		self.ui.verticalLayout_2.addWidget(self.chk)#添加复选框到布局管理器内，必要的，否则无法正常显示
		self.chk.setText(checkText)#设置文本内容

	def __CreateRadio(self,radioName,radioText):
		'''
		创建单选框
		:param checkName: 复选框的objectName
		:param checkText: 复选框的文本内容
		:return:
		'''
		self.rab = QRadioButton(self.ui.groupBox_4)#在groupBox_2内实例化复选框
		self.rab.setObjectName(radioName)#设置名称
		self.ui.horizontalLayout.addWidget(self.rab)#添加复选框到布局管理器内，必要的，否则无法正常显示
		self.rab.setText(radioText)#设置文本内容

	@pyqtSlot()
	def on_actOpen_File_triggered(self):
		'''
		打开文件按钮
		:return:
		'''
		self.__FileName,self.flt = QFileDialog.getOpenFileName(self,"打开一个文件",self.BASE_PATH,"*(*.xlsx)")
		if self.__FileName == "":
			return

		# self.ui.btnInit.setEnabled(True)#打开初始化按钮
		self.Open_File_path=self.__FileName#获取文件路径
		# print(self.Open_File_path)
		self.__Excle_init()
	##=========自定义槽函数============
	def __groupbox4_init(self):
		for i in self.ui.groupBox_4.children():
			if type(i) == QRadioButton:
				i.deleteLater()  # 删除checkBox组件
		Column = self.itemModel.columnCount()  # 获取二维列表的长度

		for i in range(Column):
			item = self.itemModel.item(0, i)  # 遍历二级列表内的元素

			try:
				radioText = item.text()
				radioName = "rad_{}_{}".format(0, i)
				self.__CreateRadio(radioName,radioText)  # 按照选项个数动态生成生成复选框
			except AttributeError:
				break


	##===========窗体测试程序==========
if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = QmyMainWindow()
	form.show()

	sys.exit(app.exec_())