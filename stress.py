from multiprocessing import Pool
import os
import sys
import getopt

PHANTONJS = '/opt/phantomjs/bin/phantomjs'


def f(url):
    os.system("%s stress.js %s" % (PHANTONJS, url))
    return True


def usage():
    print 'Usage: python stress.py [options] [http[s]://]hostname[:port]/path'
    print 'Options are:'
    print '    -n requests     Number of requests to perform (default: 1)'
    print '    -c concurrency  Number of multiple requests to make (default: 1)'
    print '    -h              Display usage information (this message)'
    sys.exit(2)

if __name__ == '__main__':
    try:
        options, args = getopt.getopt(sys.argv[1:], "hc:n:", ["help"])
    except getopt.GetoptError:
        usage()
    c = 1
    n = 1
    for opt, arg in options:
        if opt == '-c':
            c = int(arg)
        if opt == '-n':
            n = int(arg)
        if opt == '-h' or opt == '--help':
            usage()
    if not args:
        usage()
    url = args[0]
    pool = Pool(processes=c)
    pool.map(f, [url] * n)
