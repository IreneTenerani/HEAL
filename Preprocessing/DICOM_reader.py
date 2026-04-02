#!/usr/bin/env python
# coding: utf-8

# # DICOM reader
# 

# In[1]:


import os
import pydicom
import matplotlib.pyplot as plt


# In[5]:


import os
import pydicom
import matplotlib.pyplot as plt

def get_one_image(data_folder, image, slice_index):
    """
    Retrieves one specific image and plots a specific slice of a DICOM image and returns the dataset, pixel array and pixel array in HU.

    Parameters:
        data_folder (str): Path to the folder containing the DICOM image.
        image (str): Filename of the DICOM image.
        slice_index (int): Index of the slice to retrieve.

    Returns:
        dataset (pydicom.Dataset): DICOM dataset of the image.
        pixel_array (numpy.ndarray): Pixel array data of the image.
        hu (numpy.ndarray): Pixel array data of the image in Hounsfield units (HU).
    """

    # Get the current directory
    current_dir = os.getcwd()

    # Get the parent directory
    parent_dir = os.path.dirname(current_dir)

    # Change to the parent directory
    # os.chdir(parent_dir)

    # Get the absolute path of the parent directory
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Print the parent directory path
    print(parent_dir)

    # Get the Data directory path
    Data_dir = os.path.join(parent_dir, data_folder)
    print(Data_dir)

    # Construct the file name
    file_name = os.path.join(Data_dir, image)

    # Read the DICOM dataset
    dataset = pydicom.dcmread(file_name)
    print(type(dataset.pixel_array))

    # Get the pixel array data
    pixel_array = dataset.pixel_array

    # Plot the specified slice
    plt.imshow(pixel_array[slice_index, :, :], cmap=plt.cm.gray)
    plt.show()

    # Convert to Hounsfield units (HU)
    # HU = m*P + b
    # m = slope, P = pixel value, b = intercept
    hu = dataset.RescaleSlope * pixel_array + dataset.RescaleIntercept

    # Plot the specified slice in Hounsfield units (HU)
    plt.imshow(hu[slice_index, :, :], cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()
    
    
    # Return the dataset and pixel array
    return dataset, pixel_array, hu


# In[6]:


if __name__=='__main__':
    my_dataset, my_pixel_array, hu=get_one_image("Dati_Catphan/Dati_1_26_05/acquisizioni_original_cq_standard_2023-05-29_1549/Serie separate_STD", "FBP_CQ_1.dcm", 24)


# In[ ]:




