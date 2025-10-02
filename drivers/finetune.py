import moftransformer
from moftransformer.examples import example_path
from config import *

moftransformer.run(root_dataset, downstream, log_dir=log_dir,
                   max_epochs=max_epochs, batch_size=batch_size,
                   mean=mean, std=std)