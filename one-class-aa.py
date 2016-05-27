import json
from data_cleaner import loadDataSet
from data_cleaner import libSvmFormat
import os

dataMat=[]
labelMat = []
data,label = loadDataSet('one-class/hfz-1.rec',1)
dataMat =dataMat + data
labelMat = labelMat + label
data,label = loadDataSet('one-class/hfz-2.rec',1)
dataMat =dataMat + data
labelMat = labelMat + label
data,label = loadDataSet('one-class/hfz-3.rec',1)
dataMat =dataMat + data
labelMat = labelMat + label
libSvmFormat(dataMat,labelMat,'one-class/hfz.fmat')
'''
dataMat = []
labelMat  = []
for fdata in os.listdir('data_ready_predict'):
	if (fdata[0:3] == 'hfz'):
		data,label = loadDataSet('data_ready_predict/'+fdata,1)
	else:
		data,label = loadDataSet('data_ready_predict/'+fdata,-1)
	dataMat+=data
	labelMat+=label
libSvmFormat(dataMat,labelMat,'data_ready_predict/hfz.fmat')
'''
