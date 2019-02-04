#!/usr/bin/env python3
import os, subprocess
import argparse

parser = argparse.ArgumentParser(description= "GPU hot switch for dual-gpu Macs")
switchCommands = parser.add_mutually_exclusive_group()
switchCommands.add_argument('-i','--integrated',action = 'store_true', help = "switch to integrated GPU in both battery and charging modes" )
switchCommands.add_argument('-d','--discrete',action = 'store_true', help = "switch all to discrete GPU in both battery and charging modes" )
switchCommands.add_argument('-a','--automatic',action = 'store_true', help = "automatically switch bettween GPUs in both battery and charging modes" )
switchCommands.add_argument('-bc',action = 'store_true', help = "Use integrated GPU in battery mode, discrete GPU while charging" )
switchCommands.add_argument('-r','--reset', action = 'store_true', help = "Reset every settings to automatic" )
args = parser.parse_args()

#mode flag
BATTERYMODE = "-b"
CHARGINGMODE= "-c"
ALLMODE = "-a"

#gpu value
INTEGRATED = 0
DISCRETE = 1
AUTOMATIC = 2
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "Administrator/root permission is required\n[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

def switch(mode,gpu):
    if prompt_sudo() != 0:
        print("Need root permission")
    command1 = "sudo pmset"
    command2= "gpuswitch"
    os.system("%s %s %s %d" % (command1,mode,command2,gpu))
    promptResult(mode,gpu)

def promptResult(mode,gpu):
    if mode == ALLMODE:  
        if gpu == INTEGRATED:
            print("Using iGPU in in both battery and charging modes")
        elif gpu == DISCRETE:
            print("Using dGPU in in both battery and charging modes")
        elif gpu == AUTOMATIC:
            print("Automatic graphics switching is enabled for all modes (Default setting)")
    else:
        if mode == BATTERYMODE:
            print("Battery mode: using integrated GPU")
            return
        if mode == CHARGINGMODE:
            print("Charing mode: using discrete GPU")
            return
            
if __name__ == "__main__":
    if args.integrated :
        switch(ALLMODE,INTEGRATED)
    elif args.discrete: 
        switch(ALLMODE,DISCRETE)
    elif args.automatic:
        switch(ALLMODE,AUTOMATIC)
    elif args.bc:
        switch(BATTERYMODE,INTEGRATED)
        switch(CHARGINGMODE,DISCRETE)
    elif args.reset:
        switch(ALLMODE,AUTOMATIC)
    else:
        print("Unknown arugment\nType \"gpu-switch -h\" to view list of all arugments")

