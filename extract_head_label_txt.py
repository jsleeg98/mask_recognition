import os
import shutil
from glob import glob

path = 'D://User/Desktop/AI 메이커톤/kaggle_helmet/head/'

img_list = glob(path + '*.png')


# 현재 위치에 있는 이미지 파일에 이름에 해당하는 txt 파일만을 추출하여 원하는 위치에 복사하는 코드
for name in img_list:
    temp = name.split('\\')[-1].split('.')[0]
    print(temp)
    txt_path = 'D://User/Desktop/AI 메이커톤/kaggle_helmet/labels/' + temp + '.txt'
    # print(txt_path)
    shutil.copy(txt_path,  'D://User/Desktop/AI 메이커톤/kaggle_helmet/head/' + temp + '.txt')



