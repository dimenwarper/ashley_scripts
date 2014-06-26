import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    parser.add_argument('script', type=str)
    parser.add_argument('directory', type=str)
    parser.add_argument('--outdir', type=str, default='./')
    parser.add_argument('--args', type=str, nargs='+')

    args = parser.parse_args()

    scripts = []
    for fname in os.listdir('directory'):
        fullpath = os.path.abspath(args.directory + '/' + fname)
        scriptf = open('%s/%s_%s.sh' % (args.outdir, args.name, fname.replace('/','')))
        scriptf.write('#!/bin/bash\n')
        scriptf.write('sh %s %s %s\n' % (args.script, fullpath, args.args))
        scriptf.close()
        scripts.append(os.path.abspath(scriptf.name))

    masterf = open('%s/master_%s.sh' % (args.outdir, args.name), 'w')
    masterf.write('#!/bin/bash\n')
    for s in scripts:
        masterf.write('qsub %s\n' % s)
    masterf.close()

