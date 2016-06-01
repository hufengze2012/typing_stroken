#-*- coding:utf-8 -*-
from  data_cleaner import libSvmFormatSaveInFile
from  data_cleaner import libSvmFormat
import json
import os
import numpy
import re
class DistanceModel(object):
	
	def _init__(self,name):
		pass
	def loadDataSet(self, filename):
		with open('test.in','r') as f:
			text = f.read()
		with open(filename,'r') as f:
			str = f.read()
		fr = json.loads(str)
		total_words_time = []
		for line in fr :
			words_time = [] #存每个单词的字母时间间隔
			word = []
			wordLeftTime = -1
			for i,action_P in enumerate(line):
		#		print action_P
				if (action_P[1] =='press'):
					if action_P[0] == 'space' or action_P[0] =='Return':
						wordLeftTime = -1
						if (word !=[]):
							words_time.append(word) 
							word = []
					elif  wordLeftTime == -1:
						wordLeftTime = action_P[2]
					elif wordLeftTime != -1: 
						word.append(action_P[2]-wordLeftTime)	
						wordLeftTime = action_P[2]
			if (word !=[]):
				words_time.append(word)
			yield words_time
#			total_words_time.append(words_time)
#		print total_words_time
#		return total_words_time
		
	def merge_list(self,lista, listb):
		for index_i in range(len(lista)):
			for index_j in range(len(lista[index_i])):
				lista[index_i][index_j] += listb[index_i][index_j]
		return lista

	def divideUp(self,res, length):
		for index_i in range(len(res)):
			for index_j in range(len(res[index_i])):
					res[index_i][index_j] = res[index_i][index_j] / length
		return res
	
	def averageCalculate(self,filename,usrname):
	  	file_pattern = re.compile('^%s-\d.rec' % usrname)
		cnt = 0
		total_data = []
		length = 0
		for fdata in os.listdir(filename):
			if file_pattern.match(fdata):
				for each_item in self.loadDataSet('%s/%s' % (filename,fdata)) :
					if (each_item != []):
						total_data.append(each_item)
						print each_item
						length = length+1
		res_sum = reduce(self.merge_list,total_data)
		average_res = self.divideUp(res_sum,length)
		print 'the averge results = ',average_res

	def format_model_duration_time(self,filename,usrname):
		file_pattern = re.compile('^%s-\d.rec' % usrname)
		total_data = []
		length = 0
		for fdata in os.listdir(filename):
			if file_pattern.match(fdata):
				for each_item in self.loadDataSet('%s/%s' % (filename,fdata)) :
					if (each_item != []):
						total_data.append(each_item)
		return total_data
	def format_predict_duration_itme(self,filename):
		total_data = []
		for each_item in self.loadDataSet(filename):
			if (each_item != []):
				total_data.append(each_item)
		return total_data

	def average_time_calculate(self,time):
		length = len(time)	
		res_sum = reduce(self.merge_list,time)
		average_res = self.divideUp(res_sum,length)
		return average_res
	
	def distanceTrainSet(self,usrname,filename): #usrname 等待预测用户名filename 等待预测文件
		legal_usr = self.average_time_calculate(self.format_model_duration_time('data',usrname))
		judge_usr = self.average_time_calculate(self.format_predict_duration_itme(filename))
		print 'legal_usr_data = ',legal_usr
		print 'predict_usr_data = ',judge_usr
		maxn = max([len(word) for word in legal_usr])
		result = 0
		sum_n_graph = sum(range(2,maxn+2))	
		for n in range(2,maxn+2):
			#  x = legal_n_graph_model 
			x = self.n_graph_model(n,legal_usr)
			# y = judge_n_graph_model 
			y = self.n_graph_model(n,judge_usr)
			print 'x=',x
			print 'y=',y
			similar = 0
			for index in range(len(x)): 
				#print '~',x[index],y[index]
				part = max(x[index],y[index])/(min(x[index],y[index])+0.0)
				similar += 1 if part<1.25 else 0
			an1d25 = 1-similar/(len(x)+0.0)
			result += an1d25*n/sum_n_graph
			print an1d25
		print 'result=',result

	def n_graph_model(self,n,time_list):
		graph_time = []
		n -= 1
		for word in time_list:
			#print word
			for i in range(len(word)-n+1):
			#	print '~~~',word[i:i+n]
				graph_time.append(sum(word[i:i+n]))
		return graph_time
if __name__ == '__main__':
	DistanceModel().distanceTrainSet('liyue','data_ready_predict/hfz-1.rec')
#	DistanceModel().averageCalculate('data','hfz')
#	tmp = DistanceModel().loadDataSet('data_ready_predict/hfz-1.rec')
#	tmp = DistanceModel().loadDataSet('data_ready_predict/hfz-2.rec')
#	tmp = DistanceModel().loadDataSet('data_ready_predict/hfz-3.rec')
