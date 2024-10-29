# TSSA-Net
### TSSA-Net: Transposed Sparse Self-Attention-Based Network for Image Super-Resolution
# Installation
-Step 1: Create and activate the Conda environment.
```
conda create -n TSSA-Net python=3.8
conda activate TSSA-Net
```
-Step 2: Install the necessary packages.
```
pip install -r requirements.txt
python setup.py develop
```
# Testing
- Refer to `./options/test` for the configuration file of the model to be tested, and prepare the testing data and pretrained model.    
- Then run the following codes (taking TSSA-Net_SRx4.pth as an example) :
```
python TSSA-Net/test.py -opt options/test/TSSA-Net_SRx4.yml
```
# Training
- Refer to `./options/train` for the configuration file of the model to train.
- Preparation of training data can refer to [this page](https://github.com/XPixelGroup/BasicSR/blob/master/docs/DatasetPreparation.md).
- The training command is like :
```
CUDA_VISIBLE_DEVICES=0,1 python -m torch.distributed.launch --nproc_per_node=2 --master_port=4321 TSSA-Net/train.py -opt options/train/train_TSSA-Net_SRx2_from_scratch.yml --launcher pytorch
```
# Results and Pretrain Model
The Results and pretrain models can be download from [Baidu Netdisk](https://pan.baidu.com/s/1hF5-HjYK9H0xHS41qhO9Fw) 
# Contact
If you have any questions, please feel free to contact me guanhaochen@stu.ynu.edu.cn.
# Acknowledgement
The codes are based on [BasicSR](https://github.com/XPixelGroup/BasicSR/tree/master) and [SwinIR](https://github.com/JingyunLiang/SwinIR). Please also follow their licenses. Thanks for their awesome works.
