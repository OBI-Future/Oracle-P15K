import pytorch_lightning as pl
from torch.utils.data import DataLoader

from dataset import MyDataset
from obidiff.logger import ImageLogger
from obidiff.model import create_model, load_state_dict

# Configs
resume_path = 'models/control_sd15_ini.ckpt'
batch_size = 1
logger_freq = 1200
learning_rate = 1e-5
sd_locked = False
only_mid_control = False


# First use cpu to load models. Pytorch Lightning will automatically move it to GPUs.
model = create_model('./models/obidiff.yaml').cpu()
model.load_state_dict(load_state_dict(resume_path, location='cpu'))
model.learning_rate = learning_rate
model.sd_locked = sd_locked
model.only_mid_control = only_mid_control


# Misc
prompt_file_train = './training/Oracle-P15K/train.json'
prompt_file_val = './training/Oracle-P15K/val.json'
train_data_root = '/path/to/training/set/'
val_data_root = '/path/to/validation/set/'
train_dataset = MyDataset(
    prompt_file=prompt_file_train, data_root=train_data_root)
val_dataset = MyDataset(prompt_file=prompt_file_val, data_root=val_data_root)
train_dataloader = DataLoader(train_dataset, num_workers=32,
                              batch_size=batch_size, shuffle=True)
val_dataloader = DataLoader(val_dataset, num_workers=32,
                            batch_size=batch_size, shuffle=False)
logger = ImageLogger(batch_frequency=logger_freq)
trainer = pl.Trainer(gpus=1, precision=32, callbacks=[logger], max_epochs=300)


# # Train!
trainer.fit(model, train_dataloaders=train_dataloader,
            val_dataloaders=val_dataloader)
