# Image generation with GANs

The aim of this raport is to present the results of a project conducted as part of the Deep Learning course at Warsaw University of Technology. The project included image generation with Generative Adversarial Networks using the LSUN bedroom dataset.
The folders contain:
- data - a place to store the LSUN dataset downloaded from https://www.kaggle.com/datasets/jhoward/lsun_bedroom?resource=download
- models - implementation of different versions of the the DCGAN model
- utils - functions for downloading dataset and other miscellaneous
- weights - DCGAN models trained during the experiments (one using dropout trained for 10 epochs, and the original architecture trained for 5 epochs and 10 epochs)

The notebooks contain the experiments and the visualisations of images created in them:
- DCGAN - regular DCGAN 64x64 trained for 5 epochs
- DCGAN64_dropout - DCGAN 64x64 with dropout, soft labels and using SGD trained for 10 epochs
- DCGAN64_fid_interpolation - regular DCGAN 64x64 trained for 10 epochs (final model) with the FID calculation and visualisation of images cteated from a interpolation of two latent vectors
- DCGAN128_dropot - DCGAN 128x128 with dropout, soft labels and using SGD, training stopped due to time of computation
- DCGAN128_fail - regular DCGAN 128x128, training stopped due to model collapse