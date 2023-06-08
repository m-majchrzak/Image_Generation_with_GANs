# Image generation with GANs

The aim of this raport is to present the results of a project conducted as part of the Deep Learning course at Warsaw University of Technology. The project included image generation with Generative Adversarial Networks using the LSUN bedroom dataset: https://www.kaggle.com/datasets/jhoward/lsun_bedroom?resource=download

ToDo:

Modele:
- jeden model uczony od zera (DCGAN?) (Martyna)
- 2 z listy (StyleGAN2 + StyleGAN3) (gotowy + dotrenowanie) (Martyna)
- Stable diffusion (Władek)

Experymenty:
- calculate the Fr´echet Inception Distance (FID) for your generated images and
compare it to results from literature - https://paperswithcode.com/sota/image-generation-on-lsun-bedroom-256-x-256
- assess your results qualitatively
- investigate the influence of hyperparameters on obtained results
 - discuss sets of hyperparameters which help in overcoming training collapse and
mode collapse
- select two of your generated images together with their latent vectors; interpolate
linearly between the two latent vectors to generate 8 additional latent vectors; use
these 8 vectors to generate images from your model; present the 10 generated
images (8 newly generated and 2 generated previously) and discuss the importance
of the results
- discuss any additional findings
