import os
import cv2
from tqdm import tqdm


# sun to coco
sun_label = '/multiview/3d-count/OFFICIAL_SUNRGBD/sunrgbd/sunrgbd_trainval/label_v1'
sun_image = '/multiview/3d-count/OFFICIAL_SUNRGBD/sunrgbd/sunrgbd_trainval/image'

sun_coco_image = '/multiview/3d-count/sun_coco/images'
sun_coco_label = '/multiview/3d-count/sun_coco/labels'


class_dict = {'bed': 0, 'table': 1, 'sofa': 2, 'chair': 3, 'toilet': 4, 'desk': 5, 'dresser': 6, 'night_stand': 7, 'bookshelf': 8, 'bathtub': 9}

for filename in tqdm(os.listdir(sun_label)):
  label_objects = []
  scene_id = filename[0:-4]
  label_file = scene_id + ".txt"
  image_file = scene_id + ".jpg"

  with open(f"{sun_label}/{label_file}") as fn:
    line = fn.readlines()
    
    image = cv2.imread(f"{sun_image}/{image_file}")
    h, w, c = image.shape

  for l in line:
    l = l[0:-1].split(" ")
    class_name = l[0]
    if class_name not in class_dict.keys():
      continue
    class_index = class_dict[class_name]

    left = int(float(l[1]))
    top = int(float(l[2]))
    right = int(float(l[1]) + float(l[3]))
    bottom = int(float(l[2]) + float(l[4]))

    width = (right - left)
    height = (bottom - top)
    x_center = (left + (width / 2))
    y_center = (top + (height/ 2))

    norm_width = width / w
    norm_height = height / h
    norm_x_center = x_center / w
    norm_y_center = y_center / h


    sun_coco_string = (f"{class_index} {norm_x_center} {norm_y_center} {norm_width} {norm_height}\n")
    label_objects.append(sun_coco_string)

# save labels
  with open(f"{sun_coco_label}/{label_file}", "w") as output:
    for i in label_objects:
      output.write(str(i))

# save images
  cv2.imwrite(f"{sun_coco_image}/{image_file}", image)