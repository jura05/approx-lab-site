#!/usr/bin/env python3

import os.path
import subprocess

def deploy():
    bin_dir = os.path.dirname(__file__)
    remote_server = '158.250.33.64'
    remote_dir = '/var/www/vhosts/approx-lab'
    command = [
        'rsync',
        '-e', 'ssh -p 22018',
        '--recursive',
        '--verbose',
        '--exclude', '.*',
        bin_dir + '/../generated-content/',
        remote_server + ':' + remote_dir,
    ]
    print(command)
    subprocess.check_call(command)

if __name__ == "__main__":
    deploy()
