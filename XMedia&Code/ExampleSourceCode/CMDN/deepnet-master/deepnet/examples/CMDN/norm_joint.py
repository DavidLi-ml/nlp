from __future__ import division
import numpy as np
import os, sys


def normalize_func(minVal, maxVal, newMinValue=0, newMaxValue=1):
  def normalizeFunc(x):
    r=(x-minVal)*newMaxValue/(maxVal-minVal)+newMinValue
    return r
  return np.frompyfunc(normalizeFunc,1,1)

for modal in ['img', 'txt']:
    for datasets in ['train', 'test', 'validation']:
        prefix= os.path.join(('joint_'+modal), ('joint_reps/joint_'+modal+'_LAST'), datasets)
        data=np.load(prefix+'/joint_'+modal+'_hidden-00001-of-00001.npy')
        minVal=np.amin(data)
        maxVal=np.amax(data)

        outuFuncXArray=normalize_func(minVal,maxVal,0,1)(data)
        dataXArray=outuFuncXArray.astype(float)

        np.save(os.path.join(('ff_'+modal), 'data', datasets, ('joint_'+modal+'hidden-00001-of-00001.npy')), dataXArray)
