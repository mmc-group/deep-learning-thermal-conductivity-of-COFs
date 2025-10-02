root_cifs = '../data/mercado-UC-cif' 
root_dataset = '../data/mercado-UC-processed/' 
downstream =  'kavg'
tc_dataset = '../data/TC-data.csv'

train_fraction = 0.8
test_fraction = 0.1


# Settings for finetuning and prediction:
log_dir = './logs/'    
seed = 0               
version = 0            # version for model. It increases with the number of trains
checkpoint = 'best'    # Checkpoint name
mean = None
std = None
max_epochs = 100
batch_size = 32
