python2.7 evaler.py \
--dataset chair \
--data_id_list ./testing_tuple_lists/id_chair_random_elevation.txt \
--checkpoint ./chair_checkpoint/model-1 \
--num_input 4 \
--loss True \
--write_summary True \
--summary_file ./output/log_chair.txt \
--plot_image True \
--output_dir ./output/img_chair