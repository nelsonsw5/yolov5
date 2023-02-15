


with open('/multiview/3d-count/Kitti/ImageSets/train.txt','r') as f:
    train = f.readlines()

with open('/multiview/3d-count/Kitti/ImageSets/val.txt','r') as f:
    val = f.readlines()

for id in train:
    line = './images/' + id[0:-1] + '.png'
    with open('/multiview/3d-count/kitti_coco/train2017.txt','a') as f:
        f.write(line + '\n')

for id in val:
    line = './images/' + id[0:-1] + '.png'
    with open('/multiview/3d-count/kitti_coco/val2017.txt','a') as f:
        f.write(line + '\n')