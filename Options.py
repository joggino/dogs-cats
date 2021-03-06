''' loads data dependent variables from the dataset '''
import Utils.dataset as data
img_width, img_height, nb_train_samples, nb_validation_samples,\
                             train_data_dir, validation_data_dir = data.load_dataset_vars('../data')
''' Parameters to alter '''
MODEL_NAME = "test"
nb_epoch = 50

ckpt_kwargs = {
	"monitor":'val_acc',
	"verbose":1,
	"save_best_only":True,
	"mode":'max',
	"period":5
}

tensorboard_kwargs = {
	"histogram_freq": 10,
	"write_graph": False,
	"write_images": False
}

train_image_kwargs = {
    "rescale": 1./255,
    "shear_range": 0.2,
    "zoom_range": 0.2,
    "horizontal_flip": True
}

test_image_kwargs = {
    "rescale": 1./255
}

train_kwargs = {
	"target_size": (img_width, img_height),
    "batch_size": 32,
    "class_mode":'binary'
}

test_kwargs = {
	"target_size": (img_width, img_height),
    "batch_size": 32,
    "class_mode": 'binary'
}

# One large json file to make it easy to save and reference.
mdl = {
    "logs": {"acc":0},
	"nb_epoch": nb_epoch,
    "train_image_kwargs": train_image_kwargs,
    "test_image_kwargs": test_image_kwargs,
    "train_kwargs": train_kwargs,
    "test_kwargs": test_kwargs,
    "ckpt_kwargs": ckpt_kwargs,
    "ckpt_filepath": "checkpoints/weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5",
    "tensorboard_kwargs": tensorboard_kwargs,
    "tensorboard_logpath": "./logs"
}
