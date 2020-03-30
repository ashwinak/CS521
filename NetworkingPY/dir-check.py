#!/usr/bin/python3
from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.exception import *
import multiprocessing
import time
NUM_PROCESSES = 2
USER = 'regress'
PASSWD = 'MaRtInI'
DEVICES = [
   '172.19.64.132',
   '172.19.64.101',
]
DIRECTORY = '/var/tmp/'

def check_directory_usage(host):
    try:
        with Device(host=host, user=USER, password=PASSWD) as dev:
            fs = FS(dev)
            print('Checking %s: ' % host, end='')
            print(fs.directory_usage(DIRECTORY))
    except ConnectRefusedError:
        print('%s: Error - Device connection refused!' % host)
    except ConnectTimeoutError:
        print('%s: Error - Device connection timed out!' % host)
    except ConnectAuthError:
        print('%s: Error - Authentication failure!' % host)

def main():
    time_start = time.time()
    with multiprocessing.Pool(processes=NUM_PROCESSES) as process_pool:
        process_pool.map(check_directory_usage, DEVICES)
        process_pool.close()
        process_pool.join()
    print('Finished in %f sec.' % (time.time() - time_start))

if __name__ == '__main__':
    main()