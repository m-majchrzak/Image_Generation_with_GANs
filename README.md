# Image generation with GANs

This repository contains code needed to reproduce the results for `Project III` of the Deep Learning course.

Check the other projects:

- [Project I](https://github.com/Wladeko/deep-learning-cnn) - Image Classification with CNNs
- [Project II](https://github.com/Wladeko/deep-learning-rnn) - Speech Commands Recognition with RNNs

---
## Description
The aim of this raport is to present the results of a project conducted as part of the Deep Learning course at Warsaw University of Technology. The project included image generation with Generative Adversarial Networks using the LSUN bedroom dataset.

The folders contain:

- data - a place to store the LSUN [dataset](https://www.kaggle.com/datasets/jhoward/lsun_bedroom?resource=download)
- models - implementation of different versions of the the DCGAN model
- utils - functions for downloading dataset and other miscellaneous
- weights - DCGAN models trained during the experiments (one using dropout trained for 10 epochs, and the original architecture trained for 5 epochs and 10 epochs)
- images - a place to temporarily store images for FID calculations

The notebooks contain the experiments and the visualisations of images created in them:

- DCGAN64 - regular DCGAN 64x64 trained for 5 epochs
- DCGAN64_dropout - DCGAN 64x64 with dropout, soft labels and using SGD trained for 10 epochs
- DCGAN64\_fid_interpolation - regular DCGAN 64x64 trained for 10 epochs (final model) with the FID calculation and visualisation of images cteated from a interpolation of two latent vectors
- DCGAN128_dropout - DCGAN 128x128 with dropout, soft labels and using SGD, training stopped due to time of computation
- DCGAN128 - regular DCGAN 128x128, training stopped due to model collapse

---
## Results
We presented obtained results in short [report](https://github.com/Wladeko/deep-learning-gan/blob/main/report.pdf).

---
## Co-author
Be sure to check co-author of this project, [Martyna](https://github.com/m-majchrzak).