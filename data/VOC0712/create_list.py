import os
import cv2

train_names_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/train_id_list.txt'
test_names_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/validation_id_list.txt'

train_images_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/train'
train_annos_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/voc_annotation_t'

test_images_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/validation'
test_annos_dir = '/data0/qilei_chen/OpenImagesChallenge2018/CVDF/voc_annotation_v'

#create trainval.txt
train_names_file = open(train_names_dir)
trainval_file = open('trainval.txt','wb')
line = train_names_file.readline()
while line:
    line_n = train_images_dir+'/'+line[:len(line)-1]+'.jpg'+' '+train_annos_dir+'/'+line[:len(line)-1]+'.xml\n'
    trainval_file.write(line_n);
    line = train_names_file.readline()
trainval_file.close()

#create test.txt and test_name_size
test_names_file = open(test_names_dir)
test_file = open('test.txt','wb')
test_name_size_file = open('test_name_size.txt','wb')
line  = test_names_file.readline()
while line:
    line_n = test_images_dir+'/'+line[:len(line)-1]+'.jpg'+' '+test_annos_dir+'/'+line[:len(line)-1]+'.xml\n'
    test_file.write(line_n)
    image = cv2.imread(test_images_dir+'/'+line[:len(line)-1]+'.jpg')
    size = image.shape
    line_m = line[:len(line)-1]+' '+str(size[0])+' '+str(size[1])+'\n'
    test_name_size_file.write(line_m)
    line = test_names_file.readline()
test_file.close()
test_name_size_file.close()
