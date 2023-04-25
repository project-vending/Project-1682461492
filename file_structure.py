
import os

# Create directory structure
if not os.path.exists('Image_Data_Processing_Pipeline'):
    os.makedirs('Image_Data_Processing_Pipeline')
if not os.path.exists('Image_Data_Processing_Pipeline/data'):
    os.makedirs('Image_Data_Processing_Pipeline/data')
if not os.path.exists('Image_Data_Processing_Pipeline/models'):
    os.makedirs('Image_Data_Processing_Pipeline/models')
if not os.path.exists('Image_Data_Processing_Pipeline/processed'):
    os.makedirs('Image_Data_Processing_Pipeline/processed')
    
# Create empty files in each folder
open('Image_Data_Processing_Pipeline/data/raw_data.txt', 'a').close()
open('Image_Data_Processing_Pipeline/models/my_model.h5', 'a').close()
open('Image_Data_Processing_Pipeline/processed/processed_data.txt', 'a').close()
