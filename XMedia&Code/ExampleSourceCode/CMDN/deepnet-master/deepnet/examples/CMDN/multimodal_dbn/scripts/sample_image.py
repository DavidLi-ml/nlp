"""Samples image conditioned on text."""
from deepnet import inference
from deepnet import trainer as tr
import sys


def SampleImage(model_file, op_file, base_output_dir, data_proto, gpu_mem, main_mem):
  #datasets = ['test']
  #datasets = ['train']
  #datasets = ['validation']
  for datasets in [['test'], ['train'], ['validation']]:
    layernames = ['joint_hidden', 'image_hidden2']
    layernames_to_unclamp = ['image_hidden2']
    method = 'mf'  # 'gibbs'
    steps = 10

    inference.DoInference(model_file, op_file, base_output_dir, layernames,
                        layernames_to_unclamp, memory='1G', method=method,
                        steps=steps, datasets=datasets, gpu_mem=gpu_mem,
                        main_mem=main_mem, data_proto=data_proto)

def main():
  model_file = sys.argv[1]
  op_file = sys.argv[2]
  output_dir = sys.argv[3]
  data_proto = sys.argv[4]
  if len(sys.argv) > 5:
    gpu_mem = sys.argv[5]
  else:
    gpu_mem = '2G'
  if len(sys.argv) > 6:
    main_mem = sys.argv[6]
  else:
    main_mem = '30G'
  board = tr.LockGPU()
  SampleImage(model_file, op_file, output_dir, data_proto, gpu_mem, main_mem)
  tr.FreeGPU(board)

if __name__ == '__main__':
  main()
