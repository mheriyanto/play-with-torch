[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fmheriyanto%2Fplay-with-torch&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mheriyanto/play-with-torch/issues)
![GitHub contributors](https://img.shields.io/github/contributors/mheriyanto/play-with-torch)
![GitHub last commit](https://img.shields.io/github/last-commit/mheriyanto/play-with-torch)
![GitHub top language](https://img.shields.io/github/languages/top/mheriyanto/play-with-torch)
![GitHub language count](https://img.shields.io/github/languages/count/mheriyanto/play-with-torch)
![GitHub repo size](https://img.shields.io/github/repo-size/mheriyanto/play-with-torch)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/mheriyanto/play-with-torch)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555)](https://id.linkedin.com/in/mheriyanto)

# play-with-torch
Repository for playing the computer vision apps: **Face recognition** on Raspberry Pi. 

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

## Folder Structure
  ```
  play-with-torch/
  ├── inference.py - main script to inference model
  ├── train.py - main script to start training
  ├── test.py - evaluation of trained model
  │
  ├── config.json - holds configuration for training
  ├── parse_config.py - class to handle config file and cli options
  │
  ├── docs/ - for documentation
  │   └── play-with-torch.tex
  │
  ├── templates/ - for serving model on Flask
  │   └── index.html
  │
  ├── base/ - abstract base classes
  │   ├── base_data_loader.py
  │   ├── base_model.py
  │   └── base_trainer.py
  │
  ├── data_loader/ - anything about data loading goes here
  │   └── data_loaders.py
  │
  ├── data/ - default directory for storing input data
  │
  ├── model/ - models, losses, and metrics
  │   ├── model.py
  │   ├── metric.py
  │   └── loss.py
  │
  ├── saved/
  │   ├── models/ - trained models are saved here
  │   └── log/ - default logdir for tensorboard and logging output
  │
  ├── trainer/ - trainers
  │   └── trainer.py
  │
  ├── logger/ - module for tensorboard visualization and logging
  │   ├── visualization.py
  │   ├── logger.py
  │   └── logger_config.json
  │  
  └── utils/ - small utility functions
      ├── util.py
      └── ...
  ```


## Usage

```console
$ git clone https://github.com/mheriyanto/play-with-torch.git
$ cd play-with-torch
$ python3 inference.py --source /dev/video0
```

## TO DO

- [ ] Implement Unit-Test: Test-Driven Development (TDD)


# Credit to
+ [Share PyTorch binaries built for Raspberry Pi](https://github.com/ljk53/pytorch-rpi)

## Reference
+ Yunjey Choi - PyTorch Tutorial for Deep Learning Researchers  [here](https://github.com/yunjey/pytorch-tutorial)
+ Victor Huang - PyTorch Template Project ([here](https://github.com/victoresque/pytorch-template#folder-structure))
