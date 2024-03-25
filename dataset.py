import os
import gdown
from dotenv import load_dotenv


#check if a 'dataset' folder exists and if not, create it
if not os.path.exists('dataset'):
    os.makedirs('dataset') 

# Set the path to the dataset folder
# Check if the os is Windows or Linux
if os.name == 'nt':
    DS_PATH = os.getcwd() + '\\dataset'
    print("INFO ===> OS: Windows")
else:
    DS_PATH = os.getcwd() + '/dataset'
    print("INFO ===> OS: Linux")

print("INFO ===> Dataset path: {}".format(DS_PATH))

# Downloading the dataset from Google Drive
# The dataset is a zip file containing the audio files

# Set the file ID of the dataset zip file
load_dotenv()
FILE_ID = os.getenv('DATASET_FILE_ID')
print("INFO ===> Now trying to download the dataset from Google Drive...\nINFO ===> Link: https://drive.google.com/file/d/{}/view".format(FILE_ID))

# Download the LibriSeVoc dataset zip file with gdown
# Check if the file already exists
if os.path.exists('dataset/librisevoc.zip'):
    print("INFO ===> The dataset already exists. Skipping the download...")
else:
    gdown.download('https://drive.google.com/uc?id={}'.format(FILE_ID), 'dataset/librisevoc.zip', quiet=False)
    print("INFO ===> Dataset downloaded successfully!")

