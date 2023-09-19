This github repository contains the data and code used for paper "Small Dataset Acquisition for Machine Learning Analysis with Possible Uncertainties".

example_data:

here you can find some training data, generated with different DOE strategies. Using Minitab to get the D-optimal of a specific dataset
All the training datasets here are without uncertainty. Run the uncertainty_generation.ipynb to build datasets with uncertainties. For Emukit use emu_integratednoise.ipynb.
A test dataset with 2500 data points are give as an example. With testdata_generation.py you can generate other test datasets.


code:

relevant python scripts / jupyter notebooks for data generation, model training and others.
Python freecad API scripts for data import&export are stored in the freecad folder.
Tips:
normal.py: data normalization 
Freecad_fem.txt for building the FEM simulation in freecad with python console.
auto-sklearn.ipynb: build models with auto-sklearn

results:

Experiment results related to the paper can be found here.