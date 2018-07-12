import os

labelmap_file = 'labelmap_openimagev4.prototxt'

originallabel_file = '/media/cql/DATA1/Development/openimagev4/train_label_counts.txt'

flf = open(labelmap_file,'wb')
fof = open(originallabel_file)

flf.write('item {\n')
flf.write('  name: "none_of_the_above"\n')
flf.write('  label: 0\n')
flf.write('  display_name: "background"\n')
flf.write('}\n')

line = fof.readline()
count=1
while line:
    eles1 = line.split(',')
    flf.write('item {\n')
    flf.write('  name: "'+eles1[0]+'"\n')
    flf.write('  label: '+str(count)+'\n')
    flf.write('  display_name: "'+eles1[2][:len(eles1[2])-1]+'"\n')
    flf.write('}\n')
    count=count+1  
    line = fof.readline()

flf.close()