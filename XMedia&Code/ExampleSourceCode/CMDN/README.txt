1.Environment
	Set up deepnet as the instruction of deepnet-master/INSTALL.txt
2.Data
	cd to the deepnet-master/deepnet/examples/CMDN/feature dir
	put the data with matlab format in this folder, and run mat2npy.py to convert matlab format to numpy format. Detailed data format please see in mat2npy.py.
3.Set
	parameter 'size' and 'dimensions' in the following files need to be modified according to the data scale
	-sae_img/data/wikipedia.pbtxt
	-sae_txt/data/wikipedia.pbtxt
	-multimodal_dbn/data/wikipedia.pbtxt
	where parameter 'size' means the number of data, parameter 'dimensions' means the dimension of data
4.Run
	$sh runall.sh