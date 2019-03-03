# gpu-switch
Simple CLI shortcut to manually hot-switch between integrated and discrete GPUs for __dual-GPU MacBooks__ by running a few selected `pmset` commands
 
## Usage
After successful installation, make sure "Automatic graphics switching" option is enable in "Engery Saver" in System Preferences under Energy Saver.

Type `gpu-switch` commands in Terminal app as follows:

* To use iGPU in both battery and charging modes:  ```gpu-switch -i``` 
* To use dGPU in both battery and charging modes: ```gpu-switch -d```
* To use automatic graphics switching in both modes: ```gpu-switch -a```
* To use iGPU in battery mode and dGPU while charging: ```gpu-switch -bc```
* Reset to default settings: ```gpu-switch -r```
* View list of all commands: ```gpu-switch -h```

## Installation
#### Installation:
Copy __gpu-switch__ executable file to `usr/local/bin` directory manually or by running __install__ file
#### Uninstallation:
Delete __gpu-switch__ executable file from `usr/local/bin` directory manually or by running __uninstall__ file

## Warnings
* This script only works if Mac is dual-GPU and works with `pmset` commands.
* For compatibility check: run `pmset -g` in Terminal.
* This script is simply a shortcut for `pmset` commands which __requires root permission__ as does `pmset`.
* Remember to go back to automatic switching or discrete graphics in newer Mac models to use external displays.

## Recommendation
__gfxCardStatus__ is recommended regardless to keep track of which GPU is activated at all times

## Tested
on a 15'' MBP 2018
