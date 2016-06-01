# -*- coding:utf-8 -*-
from Tkinter import *
from SVM_train import *
import tkMessageBox   
import json
import os
try:
	import cPickle as pickle
except ImportError:
	import pickle

#获取一次输入的打字间隔信息，结果以list返回
class TypingInfoGetter(object):
	def _record(self, nNowTime,eventType, strKey):
		if (strKey == 'Return'):
			return
		if self._nFirstKeyPressTime == -1:
			self._nFirstKeyPressTime = nNowTime
		hehe = {'2':'press', '3':'release'}

		self._lstResult.append([
						strKey,
						hehe[eventType],
						nNowTime - self._nFirstKeyPressTime])
		
	def _save(self):
		print(self._lstResult)	
		
	def _event_key_strike(self, event):
		if event.keysym == 'Return' and int(event.type) ==2:
		#	print '!!',self._text.get(),'~~~'
			#        print '!!',self._textTip,'@@@'
			#print type(event.type),int(event.type)
			if self._text.get().strip() == self._textTip.strip() :
			#            print 'it is the same!'
				self._closeWindow()
				return
			else:
				self._try_again()
		if event.keysym == 'BackSpace':
			self._try_again()
		else:
			self._record(event.time,event.type, event.keysym)

	def _try_again(self):
		self._lstResult = []
		self._nFirstKeyPressTime = -1
		self._objEntry.delete(0,END)
		self._text.set('')

	def _closeWindow(self):
		self._objWindow.destroy()

	def _draw_Entry(self):
		self._text = StringVar()
			# 单行文本框
		self._objEntry = Entry(self._objWindow)
		self._objEntry.focus_set() #选定文本框，不必鼠标点击
		self._objEntry.bind('<KeyPress>', self._event_key_strike)
		self._objEntry.bind('<KeyRelease>',self._event_key_strike)
		self._objEntry['textvariable'] = self._text
		self._objEntry.pack()
	
	def __init__(self,test_counter,total_counter):
		self._lstResult = []
		self._nFirstKeyPressTime = -1
		self._objWindow = None
		self._objEntry = None
		self._textTip = "The tip file is not exist!"
		self._text = None

		title = 'counter:%d total:%d' %(test_counter,total_counter)

		self._objWindow = Tk(className=title )
		#文本提示
		with open('test.in','r') as f:
			self._textTip = f.read()
		objContext = Label(self._objWindow,text = self._textTip)
		#objContext.insert(INSERT,"hellohello")
		# objContext.insert(END,"assd")
		objContext.pack()
	
		self._draw_Entry()

		self._objWindow.mainloop()
	
	def getResult(self):
		return self._lstResult
		
		
class GetResult():
	_results = list()
	_usrname = ''
	def __init__(self,times,usrname):
		self._results = []
		self._usrname = usrname
		for i in range(times):
			info = TypingInfoGetter(i+1,times)
			result = info.getResult()
			print result
			self._results.append(result)

	#按list返回
	def List(self):
		return self._results
	def Jason(self):
		return json.dumps(self._results)
	#tmp = json.dumps(type_info)
	def save_as_file(self,filename):
		cnt = 0
		#host = os.getlogin() #获取主机名 
		while True: #第一个顺位未出现数字作为文件名
			cnt = cnt+1
			data_path = '%s/%s-%d.rec' %(filename,self._usrname,cnt)
			if (not os.path.exists(data_path)):
				break
		with open(data_path,'w') as f:
			f.write(self.Jason()) #序列化，并保存进文件
		return data_path            

class UserCreate():
	_objWindow = None
	def _typing_end(self,event):
		if  event.keysym == 'Return': 
			print 'the name=aa%saa' % self._usrN.get().strip()
			if (self._usrN.get().strip() == ''):
				self._try_again()
			else:
				self._closeWindow()

	def _try_again(self):
		self._objEntry.delete(0,END)
		self._usrN.set('')
	def _closeWindow(self):
		self._objWindow.destroy()

	def __init__(self):
		self._objWindow = Tk(className='用户名创建' )
        #objContext = Label(self._objWindow,text = '用户名')
        #objContext.insert(INSERT,"hellohello")
        # objContext.insert(END,"assd")
        #objContext.pack()
		self._usrN = StringVar()
		self._objEntry = Entry(self._objWindow)
		self._objEntry.focus_set() #选定文本框，不必鼠标点击
		self._objEntry.bind('<KeyPress>', self._typing_end)
		self._objEntry['textvariable'] = self._usrN
		self._objEntry.pack()
		self._objWindow.mainloop()    
      #  return self._usrname.get().strip() 
	def get_usr_name(self):
		return self._usrN.get().strip()

class Selection():
	_objWindow = None
	_usrname = None

	def _closeWindow(self):
		self._objWindow.destroy()

	def __init__(self):
		self._objWindow = Tk(className='欢迎来到击键辅助认证系统' )
        #objContext = Label(self._objWindow,text = '用户名')
        #objContext.insert(INSERT,"hellohello")
        # objContext.insert(END,"assd")
        #objContext.pack()
		self._input_button = Button(self._objWindow,text = '用户信息录入',command = self.data_input)
		self._login_button = Button(self._objWindow,text = '用户登陆',command = self.login)
		self._input_button.pack()
		self._login_button.pack()
		self._objWindow.mainloop()    
      #  return self._usrname.get().strip() 
	def data_input(self):
		self._selection = 1
		self._closeWindow()
		#print 'lala'
	#	a = UserCreate()
	#	self.usrname = a.get_usr_name()
	#	GetResult(4,self.usrname).save_as_file()
	def login(self):
		self._selection = 0
		self._closeWindow()
	#	print 'wowo'
	def get_selection(self):
		return self._selection 

def JudgeLegal(result):
	root = Tk()
	root.withdraw()
	if (result == 1):
	   tkMessageBox.showinfo("结果反馈", "登陆成功" )
	else:
	   tkMessageBox.showinfo("结果反馈", "登陆失败" )
if __name__ == '__main__':
	#print tmp	
       # print GetResult(2).List()
       # print GetResult(2).Dict()
		slt =  Selection().get_selection()
		print slt
		if (slt):
			usrname = UserCreate().get_usr_name()
			GetResult(4,usrname).save_as_file('data')
		else:
			usrname = UserCreate().get_usr_name()
			info = GetResult(1,usrname)
			data_path = info.save_as_file('data_ready_predict')
			train  = svmModel(usrname)
			train.cSvmTrainSet()
			results = train.cSvmPredict(data_path,1)
			JudgeLegal(results[0])
#			if (results[0] == 1):  #把登陆成功信息输入数据库
#				info.save_as_file('data')	
		#	if results[0] == 1:
		#		print 'yes'
		#	else:
		#		print 'no'

