import os
import pathlib
import shutil

import tensorflow as tf
from pyunpack import Archive
from tqdm import tqdm

# Downloading data
def download_dataset(data_path):
  data_dir = pathlib.Path(data_path)
  if not data_dir.exists():
    tf.keras.utils.get_file(
        origin="https://storage.googleapis.com/kaggle-data-sets/17776/23297/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230608%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230608T135121Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=9d668e9f12442909d797adbdacd2c4a24cf08f031d78f35df2de830f5b624aa34369890820a96d9b0bae24c77281847c14c004aaeb261bc24aa4bfa9d0827b139fae8fedf30d983e11e1d89e4f680c310dd83edd24e5730aa7de087833ac619a89481b22030fcfd9eca19bb9718bc1e649f95157ceb51f71dc4c462a0d71eb924a99e516e19edcf33d94f75e98d69fffcaaf08b5a92a1c47f2e4ddb1dc273dbb6853ed82bd85cbc5511239a1de2209a9424ad14458a067cb2326eeb7625270d2221ceb01b202f3ab32f23864142b8a60109f7c397d7ffda559751c4b1c9a8c72ddaa52fa9720b66878b76d1c6284a7f4bb1e4822a154279931e3b8aa6dc83b0a",
        cache_dir='.', cache_subdir='data')
  Archive('data/archive.zip').extractall("data")


