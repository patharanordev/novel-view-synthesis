import os
import h5py
import ipyplot
import numpy as np
from PIL import Image

data = None
base_path = "specific/images/"
filename = "specific/data_chair.hdf5"

# clear the old hdf5
if os.path.exists(filename):
  os.remove(filename)

h5 = h5py.File(filename, "a")

for i in os.listdir(base_path):
  img_path = os.path.join(base_path, i)
  img_name = i.split('.')[0]
  img_pose = img_name.split('_')[1:]
  img_pose = [int(img_pose[0]), int(img_pose[1])]
  # print('image:', img_name)
  # print('pose:', img_pose)

  # create group by image name
  img_group = h5.create_group(img_name)

  # add image
  img_group.create_dataset('image', data=np.asarray(Image.open(img_path)))

  # add pose
  img_group.create_dataset('pose', data=img_pose)

h5.close()