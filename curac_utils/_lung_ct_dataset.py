import numpy as np
import urllib.request
from torch.utils.data import Dataset
import torch
import progressbar


class MyProgressBar():
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


class LungCTDataset(Dataset):
    def __init__(self, size=(512, 512), download=True):
        self._url = ""
        if self._url == "":
            raise ValueError("""Data set file missing.
You can download the data set at https://www.kaggle.com/kmader/finding-lungs-in-ct-data""")
        # I removed the private link to the data set file
        # you can download the data set at https://www.kaggle.com/kmader/finding-lungs-in-ct-data

        if download:
            print("Downloading data")
            urllib.request.urlretrieve(self._url, "ct_data.npz", MyProgressBar())
        
        npy_file = np.load("ct_data.npz")
        self._images = npy_file['imgs']
        self._labels = npy_file['labels']
        self._size = size
    
    def __len__(self):
        assert self._images.shape[0] == self._labels.shape[0]
        return self._images.shape[0]
    
    def __getitem__(self, idx):
        x = torch.FloatTensor(self._images[idx]).unsqueeze(0).unsqueeze(0)
        y = torch.FloatTensor(self._labels[idx]).unsqueeze(0).unsqueeze(0)

        x = torch.nn.functional.interpolate(x, self._size)[0]
        y = torch.nn.functional.interpolate(y, self._size)[0, 0].long()

        return x, y
