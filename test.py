import pytorch_lightning as pl
from torch.utils.data import DataLoader

from dataset import MyDataset
from obidiff.logger import ImageLogger
from obidiff.model import create_model, load_state_dict

# Configs
resume_path = '/path/to/checkpoint.ckpt'
batch_size = 1
logger_freq = 1200
learning_rate = 1e-5
sd_locked = True
only_mid_control = False


# First use cpu to load models. Pytorch Lightning will automatically move it to GPUs.
model = create_model('./models/obidiff.yaml').cpu()
model.load_state_dict(load_state_dict(resume_path, location='cpu'))
model.learning_rate = learning_rate
model.sd_locked = sd_locked
model.only_mid_control = only_mid_control


# Misc
prompt_file_test = 'training/Oracle-P15K/test.json'
test_data_root = '/path/to/testing/set/'
test_dataset = MyDataset(prompt_file=prompt_file_test,
                         data_root=test_data_root)
test_dataloader = DataLoader(test_dataset, num_workers=32,
                             batch_size=batch_size, shuffle=True)
logger = ImageLogger(batch_frequency=logger_freq)
trainer = pl.Trainer(gpus=1, precision=32, callbacks=[logger], max_epochs=300)


# Test!
trainer.test(model, test_dataloader)
