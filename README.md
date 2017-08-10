# Instructions to use InfoGAN for Shapes

## Preparation
You need:
* to clone our github repository

$ `git clone https://github.com/felixblind/labrotation-ai.git`

* python2.7 (not in a virtual environment!)
* pip
* an old version of prettytensor, this will install a new version of tensorflow, so be sure to do this before you install the the old version of tensorflow). You can run:

$ `export PT_BINARY_URL=https://pypi.python.org/packages/73/3a/e0f1b3fa2623bf3df7fd106dd82d06502e4926c0c2389d41350cd967e31c/prettytensor-0.6.2-py2-none-any.whl#md5=369d16653bf378e62d933552f5b9dcb8`                   
$ `sudo pip install --upgrade $PT_BINARY_URL`

* progressbar:

$ `pip install progressbar`

* dateutil:

$ `pip install python-dateutil`

* pygame (To create shapes yourself):

$ `pip install pygame`

* scipy (To create shapes yourself):

$ `pip install scipy`

* Pillow (To create shapes yourself):

$ `pip install Pillow`

* Tensorflow 0.9.0, (first install prettytensor!) to get this specific version if you are on Linux you can run:
		
$ `export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-linux_x86_64.whl`                  $ `sudo pip install --upgrade $TF_BINARY_URL`

## Run our version
The file image.pkl that is used for InfoGAN and currently in the github repository contains not rotated shapes, only right triangles and only shapes that are somewhere in the middle of the images. To simply run this version with 100 Epochs and two uniform variables, go into your InfoGAN directory and run:

$ `PYTHONPATH='.' python launchers/run_shape_exp.py`

To call tensorboard type:

$ `tensorboard --logdir logs/shape/`

## Change Shapes
If you want to change the shapes that are used for InfoGAN you have to run CreateShapes.py (in the labrotation-ai directory) with your changes. This will create a new images.pkl file. After running 

$ `python CreateShapes.py`

you can switch to the InfoGAN directory and run the aforementioned commands.

Currently supported shape options are:
1. Rotation of rectangles and ellipses in specified angles
2. Only using shapes that originate somewhere in the middle of the image or all shapes
3. Using right triangles or use all triangles

1. To change rotation of rectangles and ellipses open labrotation-ai/CreateShapes.py and go to the main method (at the end of the script). The variable “rotationAngles” needs a list of all angles in which the shapes should be rotated. Be sure to only use angles up to 90°, as the shapes already exist in 90°, 180° and 270° rotation and those will also be rotated. Example: To rotate the shapes in 15°-Steps the “rotationAngles” should be [15,30,45,60,75].

2. To change that the shapes shouldn’t originate in the middle of the image, open labrotation-ai/Shapes.py and change every call of “checkMatrixAndMiddle” to “checkMatrix”.

3. To use all triangles instead of only right triangles open labrotation-ai/CreateShapes.py and go to the main method (at the end of the script). Decomment “createTriangles(...)” and comment “createRightTriangles(...)”.

## Change InfoGAN
### Generation variables
The current version of InfoGAN can cope with Uniform variables, Gaussian and MeanBernoulli with value 1, and categorical variables with 10 categories. To change what variables will be used for the generation open labrotation-ai/InfoGAN/launchers/run_shape_exp.py and type change them in latent_spec.

### Categorical variables
If you want more or less categories for the categorical variable additionally to run_shape_exp.py you also have to change in labrotation-ai/InfoGAN/infogan/algos/infogan_trainer.py the function visualize_all_factors(...). Change all 10s to your new number of categories and all 100s to your (number of categories)². Right now it is not possible to have different visualization for categorical and uniform variables.

### Network
If you want to change the Network itself it should be possible to change it in labrotation-ai/InfoGAN/infogan/models/regularized_gan.py in the init function. But no guaranty that this works, we haven’t tested it.
