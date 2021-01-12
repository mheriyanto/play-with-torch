[![HitCount](http://hits.dwyl.com/ezygeo-ai/machine-learning-and-geophysical-inversion.svg)](http://hits.dwyl.com/mheriyanto/DetectorPi)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mheriyanto/DetectorPi/issues)
![GitHub contributors](https://img.shields.io/github/contributors/mheriyanto/DetectorPi)
![GitHub last commit](https://img.shields.io/github/last-commit/mheriyanto/DetectorPi)
![GitHub top language](https://img.shields.io/github/languages/top/mheriyanto/DetectorPi)
![GitHub language count](https://img.shields.io/github/languages/count/mheriyanto/DetectorPi)
![GitHub repo size](https://img.shields.io/github/repo-size/mheriyanto/DetectorPi)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mheriyanto/DetectorPi)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555)](https://id.linkedin.com/in/mheriyanto)

# DetectorPi
Repository for playing the computer vision apps: **face recognition** on Raspberry Pi. 

## Tools
### Tested Hardware
+ RasberryPi 4 Model B [here](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/), RAM: **4 GB** and Processor **4-core @ 1.5 GHz** 
+ microSD Card **64 GB**
+ 5M USB Retractable Clip 120 Degrees WebCam Web Wide-angle Camera Laptop U7 Mini or [Raspi Camera](https://www.raspberrypi.org/documentation/hardware/camera/)

### Tested Software
+ Ubuntu Desktop 20.10 [aarch64](https://ubuntu.com/download/raspberry-pi/thank-you?version=20.10&architecture=desktop-arm64+raspi ) **64 bit**, install on RasberriPi 4
+ PyTorch: torch 1.6.0 [aarch64](https://github.com/ljk53/pytorch-rpi/blob/master/torch-1.6.0a0%2Bb31f58d-cp38-cp38-linux_aarch64.whl) and torchvision 0.7.0 [aarch64]()
+ Python min. ver. 3.6 (3.8 recommended)

### Install the prerequisites 

+ Install packages

```console
$ sudo apt install build-essential make cmake git python3-pip libatlas-base-dev
$ sudo apt install libssl-dev
$ sudo apt install libopenblas-dev libblas-dev m4 python3-yaml
$ sudo apt install libomp-dev
```

+ make swap space to 2048 MB

```console
$ free -h
$ sudo swapoff -a
$ sudo dd if=/dev/zero of=/swapfile bs=1M count=2048
$ sudo mkswap /swapfile
$ sudo swapon /swapfile
$ free -h
```

+ Install torch 1.6.0 

```console
$ pip3 install torch-1.6.0a0+b31f58d-cp38-cp38-linux_aarch64.whl

```

## Getting Started
+ run command below
```console
$ git clone https://github.com/mheriyanto/DetectorPi.git
$ cd DetectorPi
$ cd test
$ python3 test_torch.py
```

# Credit to
+ [Share PyTorch binaries built for Raspberry Pi](https://github.com/ljk53/pytorch-rpi)

## Reference
+ Victor Huang - PyTorch Template Project ([here](https://github.com/victoresque/pytorch-template#folder-structure))
