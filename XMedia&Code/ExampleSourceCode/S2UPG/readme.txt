This is the source code for "Semi-Supervised Cross-Media Feature Learning With Unified Patch Graph Regularization", which is a MATLAB implement of S2UPG. "S2UPG.m" is the main function for this program, and the parameters are also described in file "S2UPG.m". 

Wikipedia dataset is available from http://www.svcl.ucsd.edu/~nikux/, NUS WIDE dataset is available from http://lms.comp.nus.edu.sg/research/NUS-WIDE.htm, and XMedia dataset will be available on our website http://www.icst.pku.edu.cn/mipl/xmedia/ soon.

Here list the feature types used in this paper (S2UPG can also take other features as input) :

Each image is represented by a histogram of a 128-codeword SIFT codebook

Each text is represented by a 10-topic LDA model

Each audio is represented by a 29-dimension MFCC feature

Each video is firstly segmented into separate shots, then represented by histogram of a 128-codeword SIFT codebook

Each 3D model is represented by the concatenated 4700-dimension vector of a set of LightField descriptors
