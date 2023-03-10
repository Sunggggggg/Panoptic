############################################
# Download KITTI Dataset From 
# "https://s3.eu-central-1.amazonaws.com/avg-kitti/"
# 
# You Have to Know ".zip" name. Enter above URL
############################################

from __future__ import print_function

import argparse
import os
import sys

from subprocess import call
import glob

URL_BASE = "https://s3.eu-central-1.amazonaws.com/avg-kitti/"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--kitti_dir', type=str, default= "/content/kitti/")
    parser.add_argument('--zip_name', type=str, default= "data_odometry_color.zip")

    return parser.parse_args(sys.argv[1:])


def main():
    args = parse_args()
    kitti_dir = args.kitti_dir
    zip_name = args.zip_name

    if not os.path.exists(kitti_dir) : os.makedirs(kitti_dir, exist_ok = True)
    os.chdir(kitti_dir)
    
    print("Current dir {}".format(os.getcwd()))
    url = URL_BASE + zip_name

    if os.path.exists(zip_name):
        print("File {} exists. Not re-downloading.".format(zip_name))
    else:
        url = URL_BASE + zip_name
        
        print("Downloading file {} to folder {}.".format(zip_name, kitti_dir))
        call(['wget', url])
        
        call(['unzip', '-o', zip_name])


    return 0


if __name__ == '__main__':
    sys.exit(main())
