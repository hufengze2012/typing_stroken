# -*- coding:utf-8 -*-
from Tkinter import *
import json

#获取一次输入的打字间隔信息，结果以list返回
class TypingInfoGetter(object):
	_lstResult = []
	_nFirstKeyPressTime = -1
	_objWindow = None
	_objEntry = None
	_textTip = "The tip file is not exist!"
	_text = None
	def _record(self, nNowTime,eventType, strKey):
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
		if event.keysym == 'Return':
			#print '~~~',self._text.get(),'~~~',self._textTip,'~~~',event.type
			#print type(event.type),int(event.type)
			if self._text.get() == self._textTip :
				if int(event.type) == 2:
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
		
		
class GetResult(object):
    _results = list()
    def __init__(self,times):
	for i in range(times):
		result = TypingInfoGetter(i+1,times).getResult()
		self._results.append(result)

    #按list返回
    def List(self):
        return self._results
    def Dict(self):
        return json.dumps(self._results)
	#tmp = json.dumps(type_info)
if __name__ == '__main__':
	#print tmp	
        print GetResult(2).List()
        print GetResult(2).Dict()
