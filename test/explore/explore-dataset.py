import h5py
from PIL import Image

data = None
obj_brand =  "product" # "shapenet"
object_category_name = "product"
filename = "../../datasets/{}/data_{}.hdf5".format(obj_brand, object_category_name)
f = h5py.File(filename, "r")

# List all groups
keys = list(f.keys())
print("Example keys (sampling first 10-keys): %s\n" % keys[:10])

interested_list = keys
# interested_list = ['11c9c57efad0b5ec297936c81e7f6629_0_0',
# '11c9c57efad0b5ec297936c81e7f6629_0_10',
# '11c9c57efad0b5ec297936c81e7f6629_0_20',
# '11c9c57efad0b5ec297936c81e7f6629_2_0',
# '11c9c57efad0b5ec297936c81e7f6629_2_10',
# '11c9c57efad0b5ec297936c81e7f6629_2_20',
# '11c9c57efad0b5ec297936c81e7f6629_4_0',
# '11c9c57efad0b5ec297936c81e7f6629_4_10',
# '11c9c57efad0b5ec297936c81e7f6629_4_20',
# '11c9c57efad0b5ec297936c81e7f6629_6_0',
# '11c9c57efad0b5ec297936c81e7f6629_6_10',
# '11c9c57efad0b5ec297936c81e7f6629_6_20',
# '11c9c57efad0b5ec297936c81e7f6629_8_0',
# '11c9c57efad0b5ec297936c81e7f6629_8_10',
# '11c9c57efad0b5ec297936c81e7f6629_8_20',
# '11c9c57efad0b5ec297936c81e7f6629_10_0',
# '11c9c57efad0b5ec297936c81e7f6629_10_10',
# '11c9c57efad0b5ec297936c81e7f6629_10_20',
# '11c9c57efad0b5ec297936c81e7f6629_12_0',
# '11c9c57efad0b5ec297936c81e7f6629_12_10',
# '11c9c57efad0b5ec297936c81e7f6629_12_20',
# '11c9c57efad0b5ec297936c81e7f6629_14_0',
# '11c9c57efad0b5ec297936c81e7f6629_14_10',
# '11c9c57efad0b5ec297936c81e7f6629_14_20',
# '11c9c57efad0b5ec297936c81e7f6629_16_0',
# '11c9c57efad0b5ec297936c81e7f6629_16_10',
# '11c9c57efad0b5ec297936c81e7f6629_16_20',
# '11c9c57efad0b5ec297936c81e7f6629_18_0',
# '11c9c57efad0b5ec297936c81e7f6629_18_10',
# '11c9c57efad0b5ec297936c81e7f6629_18_20',
# '11c9c57efad0b5ec297936c81e7f6629_20_0',
# '11c9c57efad0b5ec297936c81e7f6629_20_10',
# '11c9c57efad0b5ec297936c81e7f6629_20_20',
# '11c9c57efad0b5ec297936c81e7f6629_22_0',
# '11c9c57efad0b5ec297936c81e7f6629_22_10',
# '11c9c57efad0b5ec297936c81e7f6629_22_20',
# '11c9c57efad0b5ec297936c81e7f6629_24_0',
# '11c9c57efad0b5ec297936c81e7f6629_24_10',
# '11c9c57efad0b5ec297936c81e7f6629_24_20',
# '11c9c57efad0b5ec297936c81e7f6629_26_0',
# '11c9c57efad0b5ec297936c81e7f6629_26_10',
# '11c9c57efad0b5ec297936c81e7f6629_26_20',
# '11c9c57efad0b5ec297936c81e7f6629_28_0',
# '11c9c57efad0b5ec297936c81e7f6629_28_10',
# '11c9c57efad0b5ec297936c81e7f6629_28_20',
# '11c9c57efad0b5ec297936c81e7f6629_30_0',
# '11c9c57efad0b5ec297936c81e7f6629_30_10',
# '11c9c57efad0b5ec297936c81e7f6629_30_20',
# '11c9c57efad0b5ec297936c81e7f6629_32_0',
# '11c9c57efad0b5ec297936c81e7f6629_32_10',
# '11c9c57efad0b5ec297936c81e7f6629_32_20',
# '11c9c57efad0b5ec297936c81e7f6629_34_0',
# '11c9c57efad0b5ec297936c81e7f6629_34_10',
# '11c9c57efad0b5ec297936c81e7f6629_34_20']

max_img = len(interested_list)

for key in interested_list:
    each_group = f[key]
    data = each_group['image'][()]
    Image.fromarray(data).save(f'./output/{key}.png')