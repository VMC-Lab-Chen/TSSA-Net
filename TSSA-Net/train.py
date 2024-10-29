# flake8: noqa
import os.path as osp

import TSSA_Net.archs
import TSSA_Net.data
import TSSA_Net.models
from basicsr.train import train_pipeline

if __name__ == '__main__':
    root_path = osp.abspath(osp.join(__file__, osp.pardir, osp.pardir))
    train_pipeline(root_path)
