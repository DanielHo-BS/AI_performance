import tensorflow as tf
from ai_benchmark import AIBenchmark


## GPU Memory Setting
"""
gpu_options = tf.compat.v1.GPUOptions(allow_growth = True)
sess = tf.compat.v1.Session(config = tf.compat.v1.ConfigProto(gpu_options = gpu_options))
"""

benchmark = AIBenchmark()
results = benchmark.run() ##run all (training + inference)
# results = benchmark.run_inference() ##run inference only (GPU ram >= 2G)
# results = benchmark.run_training() ##run training only (GPU ram >= 4G)
