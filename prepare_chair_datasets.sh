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
gdown --id 1-IbmdJqi37JozGuDJ42IzOFG_ZNAksni
# "car" 150GB
# gdown --id 1vrZURHH5irKrxPFuw6e9mZ3wh2RqzFC9
mv data_$OBJ_CLS.hdf5 "./datasets/shapenet/data_$OBJ_CLS.hdf5"

# -------------------------------------------------
# Download checkpoint model
# "chair"
gdown --id 1uTDxvpuHH4GiEfkvIg_esIvd5mgBjuY8
mv "nvs-chair/*" "./${OBJ_CLS}_checkpoint/*"