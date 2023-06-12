import pathlib
import tensorflow as tf
from pyunpack import Archive

# Downloading data
def download_dataset(data_path):
  data_dir = pathlib.Path(data_path)
  if not data_dir.exists():
    tf.keras.utils.get_file(
        origin="https://storage.googleapis.com/kaggle-data-sets/17776/23297/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230612%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230612T144601Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7f2cc6834b670b6c7261c351afcbe7af148d10b4c177fc3b64b14f9c02404ab7f5331964432ab38826d7423e7d5a6b3956ff0e35f2e5bf56819c36cec028927c8b4ca735ec9c6f718f4cb0207a2c465954b9fcf9f9ff33c9eb635556bd49a5f04c3a02876886d43681c26eb27f946c0f374bbe1611720b8ed7aa10ecd7a24c5d084fe2a725df60d83b949e9257b3c956b8d124b8c20338084b5cf95eb0fdaf4fd4ee18b166bfbe1e56318ae606049ca53ce3522b7a6ca58e2d60e6882835b81e69f71e37d32df515739dc08ee891b96c76e6f66744264aca36cb64e29554459c5f0e334a8e38da9e7efb6afca860733baa22ddb6c85a1e2170d186b236e96504",
        cache_dir='.', cache_subdir='data')
  Archive('data/archive.zip').extractall("data")


