
# Config
# --prefix: a nickname for the training
# --dataset: choose among car, chair, kitti, and synthia. You can also add your own datasets.
# Checkpoints: specify the path to a pre-trained checkpoint
# --checkpoint: load all the parameters including the flow and pixel modules and the discriminator.
# Logging
# --log_step: the frequency of outputing log info ([train step 681] Loss: 0.51319 (1.896 sec/batch, 16.878 instances/sec))
# --ckpt_save_step: the frequency of saving a checkpoint
# --test_sample_step: the frequency of performing testing inference during training (default 100)
# --write_summary_step: the frequency of writing TensorBoard summaries (default 100)
# Hyperparameters
# --num_input: the number of source images
# --batch_size: the mini-batch size (default 8)
# --max_steps: the max training iterations
# GAN
# --gan_type: the type of GAN losses such as LS-GAN, WGAN, etc

python2.7 trainer.py \
--batch_size 8 \
--dataset product \
--num_input 4