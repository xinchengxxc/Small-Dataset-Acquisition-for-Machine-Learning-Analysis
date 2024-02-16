# Small-Dataset-Acquisition-for-Machine-Learning-Analysis
Repository for the paper "Small Dataset Acquisition for Machine Learning Analysis of Industrial Processes with Possible Uncertainties"

This GitHub repository contains the data and code used for the paper "Small Dataset Acquisition for Machine Learning Analysis with Possible Uncertainties".

# example_data:

here you can find some training data, generated with different DOE strategies. Using Minitab to get the D-optimal of a specific dataset

All the training datasets here are without uncertainty. Run the uncertainty_generation.ipynb to build datasets with uncertainties. For Emukit use emu_integratednoise.ipynb.

A test dataset with 2500 data points is given as an example. With testdata_generation.py you can generate other test datasets.


# code:

relevant Python scripts / Jupyter notebooks for data generation, model training, and others.

Python freecad API scripts for running simulations are stored in code/freecad. The simulation results are exported and the corresponding training dataset and test set are constructed.

Workflow:
  1. generate training datasets (different sampling strategies) with traindata_generation.ipynb
  2. generate test dataset for evaluation with testdata_generation.py
  3. with model_generation.ipynb the models can be trained with Auto-sklearn. A test dataset and the training datasets have to be specified.

Tips:
normal.py: data normalization 

Freecad_fem.txt for building the FEM simulation in freecad with Python console.



# results:

Experiment results related to the paper can be found here.

requirement:

for freecad:

Python                   3.8.10

sklearn                  0.0.post5

joblib                   1.2.0

pandas                   2.0.2

numpy                    1.24.3

pyDOE                    0.3.8

pyDOE2                   1.3.0

GPy                      1.12.0

for auto-sklearn:

with WSL for linux: 

ubuntu                   22.04.1

Python                   3.10.6

auto-sklearn             0.15.0
