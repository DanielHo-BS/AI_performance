# Intruduction

It shows how to test the GPU performance by AI-benchmark.  
Using the device **ROScube-X**.

[AI benchmark](https://ai-benchmark.com/alpha)  
[RANK](https://ai-benchmark.com/ranking_deeplearning_detailed.html)  


# Usage


### Note

You can create a [Virtual Environment](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html#install_multiple_versions_tensorflow) to manage your local environment.  
If you want different version python or tensorflow.
***
1. Install [jetpack](https://docs.nvidia.com/jetson/jetpack/install-jetpack/index.html)

2. Install [tensorflow](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html)

3. Install ai-benchmark  

    pip install ai-benchmark

4. Open and write down the code in ``test.py``  

    from ai_benchmark import AIBenchmark  
    results = AIBenchmark().run()

5. Run the ``test.py``  

    ./test.py

# Result

*  TF Version: 2.6.2
*  Platform: Linux-4.9.253-rqx580-aarch64-with-Ubuntu-18.04-bionic
*  CPU: N/A
*  CPU RAM: 31 GB
*  GPU/0: Xavier
*  GPU RAM: 22.3 GB
*  CUDA Version: 10.2
*  CUDA Build: V10.2.300

The benchmark is running...
The tests might take up to 20 minutes
Please don't interrupt the script
***
### 1/19. MobileNet-V2

1.1 - inference | batch=50, size=224x224: 152 ± 25 ms  
1.2 - training  | batch=5### 0, size=224x224: 768 ± 32 ms

### 2/19. Inception-V3

2.1 - inference | batch=20, size=346x346: 298 ± 25 ms  
2.2 - training  | batch=20, size=346x346: 1056 ± 58 ms

### 3/19. Inception-V4

3.1 - inference | batch=10, size=346x346: 292 ± 2 ms  
3.2 - training  | batch=10, size=346x346: 1077 ± 18 ms

### 4/19. Inception-ResNet-V2

4.1 - inference | batch=10, size=346x346: 371 ± 5 ms  
4.2 - training  | batch=8, size=346x346: 1078 ± 7 ms

### 5/19. ResNet-V2-50

5.1 - inference | batch=10, size=346x346: 187 ± 3 ms  
5.2 - training  | batch=10, size=346x346: 622 ± 7 ms

### 6/19. ResNet-V2-152

6.1 - inference | batch=10, size=256x256: 271 ± 7 ms  
6.2 - training  | batch=10, size=256x256: 925 ± 38 ms

### 7/19. VGG-16

7.1 - inference | batch=20, size=224x224: 4931 ± 127 ms  
7.2 - training  | batch=2, size=224x224: 12089 ± 310 ms

### 8/19. SRCNN 9-5-5

8.1 - inference | batch=10, size=512x512: 463 ± 9 ms  
8.2 - inference | batch=1, size=1536x1536: 420 ± 2 ms  
8.3 - training  | batch=10, size=512x512: 1325 ± 10 ms

### 9/19. VGG-19 Super-Res

9.1 - inference | batch=10, size=256x256: 445 ± 4 ms  
9.2 - inference | batch=1, size=1024x1024: 915 ± 2 ms  
9.3 - training  | batch=10, size=224x224: 1512 ± 4 ms

### 10/19. ResNet-SRGAN

10.1 - inference | batch=10, size=512x512: 526 ± 2 ms  
10.2 - inference | batch=1, size=1536x1536: 470 ± 3 ms  
10.3 - training  | batch=5, size=512x512: 832 ± 3 ms

### 11/19. ResNet-DPED

11.1 - inference | batch=10, size=256x256: 775 ± 4 ms  
11.2 - inference | batch=1, size=1024x1024: 1334 ± 3 ms  
11.3 - training  | batch=15, size=128x128: 1060 ± 75 ms                                               

### 12/19. U-Net

12.1 - inference | batch=4, size=512x512: 1222 ± 21 ms  
12.2 - inference | batch=1, size=1024x1024: 1303 ± 45 ms  
12.3 - training  | batch=4, size=256x256: 1190 ± 88 ms

### 13/19. Nvidia-SPADE

13.1 - inference | batch=5, size=128x128: 671 ± 14 ms  
13.2 - training  | batch=1, size=128x128: 866 ± 37 ms

### 14/19. ICNet

14.1 - inference | batch=5, size=1024x1536: 444 ± 37 ms  
14.2 - training  | batch=10, size=1024x1536: 1746 ± 350 ms

### 15/19. PSPNet

15.1 - inference | batch=5, size=720x720: 2473 ± 44 ms  
15.2 - training  | batch=1, size=512x512: 851 ± 29 ms

### 16/19. DeepLab

16.1 - inference | batch=2, size=512x512: 677 ± 34 ms  
16.2 - training  | batch=1, size=384x384: 726 ± 36 ms

### 17/19. Pixel-RNN

17.1 - inference | batch=50, size=64x64: 2008 ± 51 ms  
17.2 - training  | batch=10, size=64x64: 6806 ± 231 ms

### 18/19. LSTM-Sentiment

18.1 - inference | batch=100, size=1024x300: 1977 ± 83 ms  
18.2 - training  | batch=10, size=1024x300: 2728 ± 83 ms

### 19/19. GNMT-Translation

19.1 - inference | batch=1, size=1x20: 529 ± 16 ms
***
### Score

* Device Inference Score: 2142
* Device Training Score: 2192
* Device AI Score: 4334
***
### Note

If you can't show the cuda version, like **N/A**.  
Make sure install cuda, then you can find it in ``/usr/local/cuda-*.*`` .  
Add cuda's path to bashrc by following commands below:

    gedit ~/.bashrc

In ``.bachrc`` add these lines:

    export PATH=/usr/local/cuda-10.2/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH

Finally, refresh and check the cuda:

    source~ ~/.bachrc
    nvcc -V
