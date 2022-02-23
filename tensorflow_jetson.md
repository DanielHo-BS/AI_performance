# Intruduction

It shows how to install Tensorflow for Jetson Platform.  
Copied from [Nvidia](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html).

# Usage 

## Prerequisite and Dependencies

1. Install JetPack.

2. Install system packages required by TensorFlow:  

    sudo apt-get update  
    sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran  

3. Install and upgrade pip3.

    sudo apt-get install python3-pip
    sudo pip3 install -U pip testresources setuptools==49.6.0 

4. Install the Python package dependencies
    
    sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig  
    sudo env H5PY_SETUP_REQUIRES=0 pip3 install -U h5py==3.1.0  

## Installing TensorFlow

Install TensorFlow using the pip3 command. This command will install the latest version of TensorFlow compatible with JetPack 4.6.

    sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v46 tensorflow

If you want to install the latest version of TensorFlow supported by a particular version of JetPack, issue the following command:

    sudo pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v$JP_VERSION tensorflow