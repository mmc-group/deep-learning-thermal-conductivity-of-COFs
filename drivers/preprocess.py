from moftransformer.examples import example_path
from moftransformer.utils import prepare_data
import os 
import pandas as pd
from config import *


os.makedirs(root_dataset,exist_ok=True)

prop = ['k_avg [W/(mK)]']
results = pd.read_csv(tc_dataset)
files = os.listdir(root_cifs)

f = open("raw_"+downstream+".json", "a")
f.write("{\n")

for idx, file in enumerate(files):
    try:
        kavg = results[results['cof'].str.contains(file[0:-9])][prop[0]].values[0]
        if idx == len(files)-1:
            f.write('"'+file[0:-4]+'": '+str(kavg)+'}')
        else:
            f.write('"'+file[0:-4]+'": '+str(kavg)+',\n')

    except:
        continue

f.close()

prepare_data(root_cifs, root_dataset, downstream=downstream,
             train_fraction=train_fraction, test_fraction=test_fraction)


