import os
import argparse

parser = argparse.ArgumentParser(description= "GPU hot switch for dual-gpu Macs")
switchCommands = parser.add_mutually_exclusive_group()
switchCommands.add_argument('-i','--integrated',action = 'store_true', help = "switch to integrated GPU" )
switchCommands.add_argument('-d','--discrete',action = 'store_true', help = "switch to discrete GPU" )
switchCommands.add_argument('-a','--automatic',action = 'store_true', help = "automatically switch bettween GPUs" )
args = parser.parse_args()
INTEGRATED = 0
DISCRETE = 1
AUTOMATIC = 2

def executeCommand(gpu):
    command = "sudo pmset -a gpuswitch"
    os.system("%s %d" % (command,gpu))
    
if __name__ == "__main__":
    if args.integrated :
        executeCommand(INTEGRATED)
    elif args.discrete: 
        executeCommand(DISCRETE)
    elif args.automatic:
        executeCommand(AUTOMATIC)
    else:
        print("Unknown arugment\nUse flag -h to view list of all arugments")

