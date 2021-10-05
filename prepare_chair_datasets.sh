#!/bin/sh

# Note:
#  - $1 is object class name, example "chair"

REPO_NAME=novel-view-synthesis
OBJ_CLS=chair

# -------------------------------------------------
# Prepare directory
mkdir -p "./output/img_$OBJ_CLS"
mkdir -p "./${OBJ_CLS}_checkpoint"

# -------------------------------------------------
# Download datasets:
# "chair" 15GB
gdown --id 1Ab_r96nwtIRZ5fhjzeL9ahCaKo-VWAVR
unzip data_$OBJ_CLS.hdf5
mv data_$OBJ_CLS.hdf5 "./datasets/shapenet/data_$OBJ_CLS.hdf5"

# For "car" around 150GB

# -------------------------------------------------
# Download checkpoint model
# "chair"
gdown --id 1uTDxvpuHH4GiEfkvIg_esIvd5mgBjuY8
mv "nvs-chair.zip" "./${OBJ_CLS}_checkpoint/nvs-chair.zip"
cd "./${OBJ_CLS}_checkpoint" && unzip nvs-chair.zip