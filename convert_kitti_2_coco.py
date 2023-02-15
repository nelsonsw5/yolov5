import os
import cv2
from tqdm import tqdm

# convert kitti to coco

# class x_center y_center width height
# jpg 

kitti_label = '/multiview/3d-count/Kitti/training/label_2'
kitti_image = '/multiview/3d-count/Kitti/training/image_2'

kitti_coco_image = '/multiview/3d-count/kitti_coco/images'
kitti_coco_label = '/multiview/3d-count/kitti_coco/labels'

counter = 0
num = 5

for filename in tqdm(os.listdir(kitti_label)):
  label_objects = []
  scene_id = filename[0:-4]
  label_file = scene_id + ".txt"
  image_file = scene_id + ".png"

  with open(f"{kitti_label}/{label_file}") as fn:
    line = fn.readlines()
    
    image = cv2.imread(f"{kitti_image}/{image_file}")
    h, w, c = image.shape

  for l in line:
    l = l[0:-1].split(" ")

    left = int(float(l[4]))
    top = int(float(l[5]))
    right = int(float(l[6]))
    bottom = int(float(l[7]))
    
    class_name = l[0]
    if class_name == "Car":
      class_index = 0

    elif class_name == "Pedestrian":
      class_index = 1

    elif class_name == "Cyclist":
      class_index = 2
    
    else:
      continue

    width = (right - left)
    height = (bottom - top)
    x_center = (left + (width / 2))
    y_center = (top + (height/ 2))

    norm_width = width / w
    norm_height = height / h
    norm_x_center = x_center / w
    norm_y_center = y_center / h


    kitti_coco_string = (f"{class_index} {norm_x_center} {norm_y_center} {norm_width} {norm_height}\n")
    label_objects.append(kitti_coco_string)

# save labels
  with open(f"{kitti_coco_label}/{label_file}", "w") as output:
    for i in label_objects:
      output.write(str(i))

# save images
  cv2.imwrite(f"{kitti_coco_image}/{image_file}", image)