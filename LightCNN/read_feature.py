import numpy as np
import glob

PATH = 'E:\\2021WIN\\SI681\\LightCNN\\CACD_feature_val'
dir_list = glob.glob(PATH + '\\' + '*')
dir_name = [x.split('\\')[-1] for x in dir_list]

Xtrain = list()
ytrain = list()

for dir in dir_name:
    feat_list = glob.glob(PATH + '\\' + dir + '\\' + '*.feat')
    feat_name = [x.split('\\')[-1] for x in feat_list]
    for feat_path in feat_list:
        feat = np.fromfile(feat_path, dtype=np.float32)
        Xtrain.append(np.asarray(feat))
        ytrain.append(dir)

print(Xtrain)
print(ytrain)
np.savez_compressed('E:\\2021WIN\\SI681\\LightCNN\\CACD_val.npz', np.asarray(Xtrain), np.asarray(ytrain))