
from sklearn.model_selection import train_test_split
from glob import glob
import yaml

path = '/home/openlab/DH_Lee/yolov5/dataset/' # 수정 필요

img_list = glob(path + 'images/*.png')

print(len(img_list))



train_img_list, val_img_list = train_test_split(img_list, test_size = 0.2, random_state=2000)

print(len(train_img_list), len(val_img_list))

with open(path + 'train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')
    
with open(path + 'val.txt','w') as f:
    f.write('\n'.join(val_img_list)+ '\n')



with open(path + 'data.yaml', 'r') as f:
    data = yaml.Loader(f)
    
print(data)

data['train'] = path + 'train.txt'
data['val'] = path + 'val.txt'

with open(path + 'data.yaml', 'w') as f:
    yaml.dump(data,f)

print(data)