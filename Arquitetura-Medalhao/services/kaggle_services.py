# Utilizar o kagglehub para fazer o download de um dataset
import kagglehub


def download_dataset(dataset_name):
    path = kagglehub.dataset_download(dataset_name)

    return path
