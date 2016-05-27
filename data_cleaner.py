# -*- coding:utf-8 -*-
import json
import os
def loadDataSet(filename,label):
	with open(filename,'r') as f:
		str= f.read()
	fr = json.loads(str)
	#处理duration时间
	duration_times = list()
	interval_times = list()
	dataMat = []
	labelMat = []
#	print fr[0]
	for line in fr:
		duration_time = list()
		interval_time =list()
		for i,action_P in enumerate(line):
			if (action_P[1] == 'press' and action_P[0] != 'Return'):
				for action_R in line[i+1:]:
					if (action_R[0] == action_P[0] and \
						action_R[1] == 'release'):
						duration_time.append([action_P[0],action_R[2]-action_P[2]])		
						break
				for action_next in line[i+1:]:
					if (action_next[1] == 'press' and action_next[0] != 'Return'):
						interval_time.append([action_P[0],action_next[0],action_next[2]-action_P[2]])	
						break
		duration_times.append(duration_time)	
		interval_times.append(interval_time)
		print 'duration_time\n',duration_time
		print 'interval_time\n',interval_time
		dataMat.append([float(x[1]) for x in duration_time]+[float(y[2]) for y in interval_time])
	#	data_length.append(interval_time[:][2])
		#duration_times = [ ['a',123'],... ]
#	print duration_times[0]
#	print interval_times[0]
#	print dataMat[0]
	for data in dataMat:
		labelMat.append(float(label))
	print labelMat
	return dataMat,labelMat

def libSvmFormatSaveInFile(dataMat,labelMat,filename):
	dataLen = len(dataMat)
	with open(filename,'w') as f:
		for i in range(dataLen):	
			array = str(labelMat[i])
			for _id,data in enumerate(dataMat[i]):
				array = array+' %d:%0.1f'%(_id+1,data)
			f.write(array)
			f.write('\n')
def libSvmFormat(data):
	formatData = {}
	for _id,data in enumerate(data):
		formatData[_id] = data
	return formatData

if __name__ == '__main__':
#	dataMat,labelMat = loadDataSet('data/hfz-1.rec',1)
#	libSvmFormat(dataMat,labelMat,'data_format/hfz-1.fmat')
	dataMat = []
	labelMat  = []
	for fdata in os.listdir('data'):
		if (fdata[0:3] == 'hfz'):
			data,label = loadDataSet('data/'+fdata,1)
		else:
			data,label = loadDataSet('data/'+fdata,-1)
		dataMat+=data
		labelMat+=label
	libSvmFormatSaveInFile(dataMat,labelMat,'data_format/hfz.fmat')

	

#	print 'dataMat1\n',dataMat[0]
#	print 'dataMat2\n',dataMat[1]
#	print 'dataMat3\n',dataMat[2]
#	print 'dataMat4\n',dataMat[3]
#	print 'labelMat\n',labelMat
#	loadDataSet('data/sunxin-1.rec',1)
