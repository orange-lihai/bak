import os, sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='ks script ...')
    parser.add_argument('--task', type=str, default = 'push')
    task = parser.parse_args()
    # print args.task
    task = args.task
    if task == 'pwd':
        pass
    elif args == 'pull':
        pass
    elif task == 'push':
        pass
    else:
        print 'UnKown --task ' + task
        
    
if __name__ == "__main__":
    main()