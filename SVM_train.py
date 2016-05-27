#-*- coding:utf-8 -*-
import  svmutil 
import os
import re
from  data_cleaner import loadDataSet
from  data_cleaner import libSvmFormatSaveInFile
from  data_cleaner import libSvmFormat
#y,x = svm_read_problem('data/ ')
class svmModel(object):
	
	def __init__(self,name):
		self.dataMat = []
		self.labelMat = []
		self.legalName = name

	def cSvmTrainSet(self):
	  	dataMat = []
	  	labelMat = []
	  	file_pattern = re.compile('^%s-\d.rec' % self.legalName)
	  	for fdata in os.listdir('data'):
	  		if file_pattern.match(fdata):
	  			data,label = loadDataSet('data/'+fdata,1)
	  		else:
	  			data,label = loadDataSet('data/'+fdata,-1)
	  		dataMat+=data
	  		labelMat+=label
		libSvmFormatSaveInFile(dataMat,labelMat,'data_format/%s.mat' % self.legalName) # todo: duoxiancheng
		y,x = svmutil.svm_read_problem('data_format/%s.mat' % self.legalName)
		prob = svmutil.svm_problem(y,x,isKernel = True)
		param = svmutil.svm_parameter('-t 0 ')
		self.model = svmutil.svm_train(prob,param)

		print self.model

	def cSvmPredict(self,filename,isLegal = True):
		label = 1 if isLegal else -1
		dataMat,labelMat = loadDataSet(filename,label)
		x=[]
		y=[]
		for data in dataMat:
			formatData = libSvmFormat(data)
			x.append(formatData)
			y.append(label)
		p_labs, p_acc, p_vals = svmutil.svm_predict(y,x, self.model )
			
		print  p_labs,p_acc,p_vals
		return p_labs

if __name__ == '__main__':
	tmp = svmModel('hfz')
	tmp.cSvmTrainSet()
	tmp.cSvmPredict('data_ready_predict/xxy-1.rec',False)


