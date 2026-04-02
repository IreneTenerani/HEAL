#Open a dicom file in a specific folder
import os
import pydicom
#
# Construct the path
dicom_file_path = os.path.join('../..', 'PHILIPS_SERIE301_unico.dcm')
#
print(dicom_file_path)
#
# Load the DICOM file
ds = pydicom.dcmread(dicom_file_path)
#
# show the image
import matplotlib.pyplot as plt
plt.imshow(ds.pixel_array[10,:,:], cmap=plt.cm.bone)
plt.show()

