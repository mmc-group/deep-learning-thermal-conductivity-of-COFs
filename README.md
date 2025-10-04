# Deep Learning Reveals Key Predictor of Thermal Conductivity in Covalent Organic Frameworks

This repository contains all the code necessary to reproduce the results presented in:

Thakolkaran et al., **Deep learning reveals key predictors of thermal conductivity in covalent organic frameworks**, Digital Discovery (2025).


---

## Acknowledgements

All the code shown here is adapted from the MOFTransformer/PMTransformer repository:
- Park, H., Kang, Y., & Kim, J. (2023). Enhancing Structure–Property Relationships in Porous Materials through Transfer Learning and Cross-Material Few-Shot Learning. ACS Applied Materials & Interfaces, 15(48), 56375–56385. [https://doi.org/10.1021/acsami.3c10323](https://doi.org/10.1021/acsami.3c10323)
- Repository: [MOFTransformer](https://github.com/hspark1212/MOFTransformer/tree/master).  

We use publicly available hypothetical COF datasets from:
- Mercado, R., Fu, R., Yakutovich, A. V., Talirz, L., Haranczyk, M., & Smit, B. (2018). In Silico design of 2D and 3D covalent organic frameworks for methane storage applications. Chemistry of Materials, 30(15), 5069–5086. [https://doi.org/10.1021/acs.chemmater.8b01425](https://doi.org/10.1021/acs.chemmater.8b01425)
    - [Dataset link](https://archive.materialscloud.org/records/1mb1g-5gm52)
    - We provide the subset of 2,471 2D COF cif files (1x1x1 unit cells) used from this dataset in this repository.
- Lan, Y., Han, X., Tong, M., Huang, H., Yang, Q., Liu, D., Zhao, X., & Zhong, C. (2018). Materials genomics methods for high-throughput construction of COFs and targeted synthesis. Nature Communications, 9(1). [https://doi.org/10.1038/s41467-018-07720-x](https://doi.org/10.1038/s41467-018-07720-x)
    - [Dataset link](https://figshare.com/s/c7e3b7610a71b9d64210)

---

## Usage

The following file tree lists all files included in this repository.

```bash
main-folder/
│
├── data/
│   ├── charge/              # Dataset of TC of COFs with electrostatic interactions
│   ├── mercado-UC-cif/      # CIF files for the Mercado dataset
│   ├── multilayer-TC/       # Dataset of TC of selected multilayer COFs
│   ├── pSED/                # pSED data of selected COFs
│   ├── size-convergence/    # Dataset of TC of selected COFs used for size convergence study
│   ├── vacf/                # Dataset of VACF of selected COFs
│   ├── vdos/                # Dataset of VDOS of selected COFs
│   └── TC-data.csv          # COF dataset with thermal conductivity and dangling mass ratio values
│
├── drivers/
│   ├── preprocess.py        # Prepares the the files for PMTransformer 
│   ├── finetune.py          # Fine-tunes the pre-trained PMTransformer to predict the thermal conductivity
│   ├── predict.py           # Predict thermal conductivity using the fine-tuned PMTransformer
│   ├── visualize.py         # Visualize attention maps for specific COF files
│   ├── config.py            # Contains all configurations and hyperparameters.
│   └── environment.yml      # Conda environment file
│
├── visualize_results.ipynb  # Jupyter notebook to visualize data
```



To use this repository, follow these steps:

1. Install the dependencies using the provided environment file:
   ```bash
   conda env create -f environment.yml
   conda activate your_environment_name
   ```
2. Download the pre-trained PMTransformer model:
   ```bash
   moftransformer download pretrain_model
   ```
3. Preprocess the COF cif files and corresponding property labels:
   ```bash
   python preprocess.py
   ```
4. Fine-tune the pre-trained model using thermal conductivity (TC) data:
   ```bash
   python finetune.py
   ```
5. Predict and save the TC values for train/test/validation sets:
   ```bash
   python predict.py
   ```
6. Visualize attention maps for individual COFs:
   ```bash
   python visualize.py
   ```

