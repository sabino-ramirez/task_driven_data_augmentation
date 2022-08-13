import sys
import argparse
from matplotlib.pyplot import axis
import numpy as np
import nibabel as nib

# parser = argparse.ArgumentParser()
# parser.add_argument('--type', type=str, default='np', choices=['nii', 'np'])
# parse_config = parser.parse_args()

# try:
#     dir = sys.ar[1]
# except:
#     print('pass directory name')

# img_id=["007","008","013"]
# slice_id_list=list(range(0,20))

def make3d(index):

    for slice in range(20):
        img_tmp = np.load("/home/sabino/task_driven_data_augmentation/train_model/single_image_deform/deform/deform_slice{}.npy".format(slice))
        label_3channel = np.load("/home/sabino/task_driven_data_augmentation/train_model/single_image_deform/deform/labels/deform_slice{}.npy".format(slice))[:,:,1]
        # print(label_3channel.shape)
        h, w = label_3channel.shape
        label_tmp = label_3channel.reshape(h, w, 1)
        if slice == 0:
            img_final = img_tmp
            label_final = label_tmp
            print(img_final.shape) #(224, 224, 1)
            print(label_final.shape) #(224, 224, 1)
        else:
            img_final=np.concatenate((img_final,img_tmp), axis=2)
            label_final=np.concatenate((label_final,label_tmp), axis=2)
            # label_final=np.append(label_final, label_tmp)
            print(img_final.shape) #(224, 224, 1)
            print(label_final.shape) #(224, 224, 1)

    nib.save(nib.Nifti1Image(img_final, np.eye(4)), "/home/sabino/task_driven_data_augmentation/train_model/single_image_deform/generated_pairs/generated" + str(index) + ".nii.gz")
    nib.save(nib.Nifti1Image(label_final, np.eye(4)), "/home/sabino/task_driven_data_augmentation/train_model/single_image_deform/generated_pairs/labels/generated" + str(index) + ".nii.gz")


# def make3d(dir):
#     count=0
#     for study_id in train_ids_list:
#         img_fname = str(self.data_path_tr_cropped)+str(study_id)+'/img_cropped.npy'
#         img_tmp=np.load(img_fname)
#         if(label_present==1):
#             mask_fname = str(self.data_path_tr_cropped)+str(study_id)+'/mask_cropped.npy'
#             mask_tmp=np.load(mask_fname)

#         if(count==0):
#             img_cat=img_tmp
#             if(label_present==1):
#                 mask_cat=mask_tmp
#             count=1
#         else:
#             img_cat=np.concatenate((img_cat,img_tmp),axis=2)
#             if(label_present==1):
#                 mask_cat=np.concatenate((mask_cat,mask_tmp),axis=2)
#     if(label_present==1):
#         return img_cat,mask_cat
#     else:
#         return img_cat
