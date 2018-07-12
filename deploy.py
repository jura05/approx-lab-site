#!/usr/bin/env python3

import os.path
import subprocess

def deploy():
    bin_dir = os.path.dirname(__file__)
    remote_server = '158.250.33.64'
    remote_dir = '/var/www/vhosts/approx-lab'
    command = [
        'rsync',
        '--recursive',
        '--exclude', '.*',
        bin_dir + '/contents/',
        remote_server + ':' + remote_dir,
    ]
    print(command)
    subprocess.check_call(command)

if __name__ == "__main__":
    deploy()
