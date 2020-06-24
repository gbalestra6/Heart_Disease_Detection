# HEART DISEASE DETECTION

This repository contains data from four different institutions around the world. A summary can be found here: https://archive.ics.uci.edu/ml/datasets/Heart+Disease 

The data came in a non-indexed space delimited form, which I converted to .csv format (see /scripts directory). 

I used AWS SageMaker to train and deploy my model, using the xg-boost algorithm. The resulting Predictor object predicts a binary output corresponding to the presence or absence of heart disease.

To run the notebook for yourself, start up an instance in AWS SageMaker and clone this repository into a new Notebook instance. Note that the hyperparameters in the tuner can be  tweaked.