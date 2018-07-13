import os

f1 = open('test.txt')
f2 = open('test1.txt','wb')

line = f1.readline()
while line:
    f2.write(line.replace('/data0/qilei_chen/OpenImagesChallenge2018/CVDF/',''))
    line = f1.readline()
f2.close()