# Chair:
# python2.7 predict.py \
# --dataset chair \
# --data_id_list ./testing_tuple_lists/id_chair_random_elevation.txt \
# --checkpoint ./chair_checkpoint/model-1 \
# --batch_size 1 \
# --num_input 4 \
# --loss True \
# --write_summary True \
# --summary_file ./output/log_chair.txt \
# --plot_image True \
# --output_dir ./output/img_chair

# Product :
python2.7 predict.py \
--dataset product \
--data_id_list ./testing_tuple_lists/id_product_random_elevation.txt \
--checkpoint ./train_dir/product-default-bs_8_lr_flow_0.0001_pixel_5e-05_d_0.0001-num_input-4-20211030-194111/model-1 \
--batch_size 1 \
--num_input 4 \
--loss True \
--write_summary True \
--summary_file ./output/log_product.txt \
--plot_image True \
--output_dir ./output/img_product