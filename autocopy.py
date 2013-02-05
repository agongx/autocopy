#coding=utf-8
import os,shutil,filecmp

srcFile='F:/a/1.txt'

dstDir='F:/c/'

idpath=dstDir+'id.txt'

max=10     #max backup versions





def getid():

	''' get current version id,if it doesn't exists,create one.



	    todo:获取harsh值



	'''

	# create the file if id.txt doesn't exist and make id=0

	if os.path.isfile(idpath):

		with open(idpath,mode='r') as idfile:

			id=idfile.read()

			if id is not None:

				id=int(id)

			else:	

				id=0

	# get the id,if id.txt exists

	else:

		

		with open(idpath,mode='w') as idfile:

			idfile.write('0')

			id=0

	return id



def setid(id):

	''' store the new id to the id.txt

	    @param int  id  [targetpath]

	    todo:读取harsh值,并存储



	'''

	with open(idpath,mode='w') as idfile:

		idfile.write(str(id))

		

def copy(srcFile,dstDir,id):

	''' copy srcFile to targetdir

	    @param int  id  [vesion id]

	    todo:复制文件

	'''
	shutil.copy2(srcFile,dstDir+str(id)+".txt")
	# os.system("copy %s %s"%(srcFile,dstDir+str(id)+".txt"))

def check(srcFile,dstDir,id):

	''' copy srcFile to target

	    @param int  id  [vesion id]

	'''

	if filecmp.cmp(srcFile,dstDir+str(id)+".txt"):#判断没有变化

		return False

	else:		

		id+=1

		if id>max:

			id=1

	return id 



if not os.path.exists(srcFile):
	print "srcFile not exist!"
if not os.path.exists(dstDir):
	print "dstDir not exist!"
	#if dstDir not exsists ,create it
	os.mkdir(dstDir)



id=getid()

id=check(srcFile,dstDir,id)

if not id :#没变化
	quit()
else:
	copy(srcFile,dstDir,id)

	setid(id)



print "copy %s %s"%(srcFile,dstDir+str(id)+".txt")

with open(idpath,mode='r') as idfile:

	print idfile.read()