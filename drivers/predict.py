from pathlib import Path
import moftransformer
from moftransformer.examples import example_path
from config import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd



load_path = Path(log_dir) / f'pretrained_mof_seed{seed}_from_pmtransformer/version_{version}/checkpoints/{checkpoint}.ckpt'

if not load_path.exists():
    raise ValueError(f'load_path does not exists. check path for .ckpt file : {load_path}')


# This predicts on all the data splits of the training data
moftransformer.predict(
    root_dataset, load_path=load_path, downstream=downstream, split='all', mean=mean, std=std
)

# Results will be stored in 'pretrained_mof_seed{seed}_from_pmtransformer/version_{version}/'