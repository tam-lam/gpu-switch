import os
import argparse

parser = argparse.ArgumentParser(description= "GPU hot switch for dual-gpu Macs")
switchCommands = parser.add_mutually_exclusive_group()
switchCommands.add_argument('-i','--integrated',action = 'store_true', help = "switch all to  integrated GPU" )
switchCommands.add_argument('-d','--discrete',action = 'store_true', help = "switch all to discrete GPU" )
switchCommands.add_argument('-a','--automatic',action = 'store_true', help = "automatically switch bettween GPUs" )
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
BCMODE = 3

def switch(mode,gpu):
    command1 = "sudo pmset"
    command2= "gpuswitch"
    os.system("%s %s %s %d" % (command1,mode,command2,gpu))
    promptResult(mode,gpu)

def promptResult(mode,gpu):
    if mode == BATTERYMODE:
        print "Battery mode: using integrate GPU \nCharing mode: using discrete GPU"
        return
    if mode == CHARGINGMODE:
        return
    else:   
        if gpu == INTEGRATED:
            print "Using iGPU"
        elif gpu == DISCRETE:
            print "Using dGPU"
        elif gpu == AUTOMATIC:
            print "All automatic switching is enabled"

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
        print("Unknown arugment\nUse -h to view list of all arugments")

