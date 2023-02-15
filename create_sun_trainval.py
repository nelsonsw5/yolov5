


with open('/multiview/3d-count/OFFICIAL_SUNRGBD/sunrgbd/sunrgbd_trainval/train_data_idx.txt','r') as f:
    train = f.readlines()

with open('/multiview/3d-count/OFFICIAL_SUNRGBD/sunrgbd/sunrgbd_trainval/val_data_idx.txt','r') as f:
    val = f.readlines()

for id in train:
    line = './images/' + str(id[0:-1]).zfill(6) + '.jpg'
    with open('/multiview/3d-count/sun_coco/train2017.txt','a') as f:
        f.write(line + '\n')

for id in val:
    line = './images/' + str(id[0:-1]).zfill(6) + '.jpg'
    with open('/multiview/3d-count/sun_coco/val2017.txt','a') as f:
        f.write(line + '\n')

