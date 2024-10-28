# Utilizar o Boto3 para se conectar ao um bucket s3 do Supabase

import os
import boto3
from kaggle_services import download_dataset
from dotenv import load_dotenv

# Carregar as variaveis de ambiente para conexão
load_dotenv()
REGION_NAME = os.getenv('REGION_NAME')
ENDPOINT_URL = os.getenv('ENDPOINT_URL')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Função para se conectar
def connect_to_supabase_s3():
  s3 = boto3.client(
    's3',
    region_name=REGION_NAME,
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
  )

  return s3

# Função para fazer upload do dataset
def upload_file_to_supabase_s3(s3, file_path, bucket_name, object_name):
  s3.upload_file(file_path, bucket_name, object_name)

# Conectar ao s3
s3 = connect_to_supabase_s3()

# Fazer download do dataset
path = download_dataset('arnabchaki/data-science-salaries-2023')

# Fazer upload do dataset
upload_file_to_supabase_s3(s3, f'{path}/ds_salaries.csv', 'dados-ao-cubo', 'ds_salaries.csv')
