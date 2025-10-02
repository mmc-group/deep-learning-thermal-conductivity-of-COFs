from moftransformer.visualize import PatchVisualizer
from moftransformer.examples import visualize_example_path
from config import *
from pathlib import Path

model_path = Path(log_dir) / f'pretrained_mof_seed{seed}_from_pmtransformer/version_{version}/checkpoints/{checkpoint}.ckpt'
cifname = '' # specify name of CIF file to be visualized

vis = PatchVisualizer.from_cifname(cifname, model_path, root_dataset)
vis.draw_graph()