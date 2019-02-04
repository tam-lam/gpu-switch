# gpu-switch
 Simple CLI shortcut to manually hot-switch between integrated and discrete GPUs for __dual-GPU Macs__ by running a few selected `pmset` commands
 
## Usage
After successful installation, make sure "Automatically graphics switching" option is enable in "Engery Saver" in Mac's System Preferences.

Type `gpu-switch` commands in terminal app as follow:

* To use iGPU in both battery and charging modes:  ```gpu-switch -i``` 
* To use dGPU in both battery and charging modes: ```gpu-switch -d```
* To enable automatical graphics switching in both modes: ```gpu-switch -a```
* To use iGPU in battery mode and dGPU while charging: ```gpu-switch -bc```
* Reset to default settings: ```gpu-switch -r```
* View list of all commands: ```gpu-switch -h```

## Installation
#### Installation:
Copy __gpu-switch__ executable file to `usr/local/bin` directory manually  or running __install__ file
#### Uninstallation:
Delete __gpu-switch__ executable file from `usr/local/bin` directory manually or running __uninstall__ file
your
## Warnings
* This script only works if  Mac is dual-GPU and works with `pmset` commands
* For compatibility check: run `pmset -g` in terminal.
* This script is simply a shortcut for `pmset` commands which __requires root permission__ as does `pmset`

## Recommendation
__gfxCardStatus__ is recommended regradless to keep track of which GPU is activated as all time

## Tested
on a 15'' MBP 2018
