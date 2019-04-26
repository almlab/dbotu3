#!/usr/bin/env python3
#
# author: scott olesen <swo@alum.mit.edu>

from dbotu import call_otus
import argparse
import sys

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='dbOTU3: Distribution-based OTU calling')
    p.add_argument('table', type=argparse.FileType('r'), help='sequence count table')
    p.add_argument('fasta', help='sequences (trimmed if unpaired, merged if paired-end; always unaligned)')

    g = p.add_argument_group(title='criteria')
    g.add_argument('--dist', '-d', type=float, default=0.1, metavar='D', help='maximum genetic dissimilarity between sequences; more dissimilar sequence pairs do not pass the genetic criterion (default: 0.1)')
    g.add_argument('--abund', '-a', type=float, default=10.0, metavar='A', help='minimum fold difference for comparing two OTUs (0=no abundance criterion; default 10.0)')
    g.add_argument('--pval', '-p', type=float, default=0.0005, metavar='P', help='minimum p-value for merging OTUs (default: 0.0005)')

    g = p.add_argument_group(title='output options')
    g.add_argument('--output', '-o', default=sys.stdout, type=argparse.FileType('w'), metavar='FILE', help='OTU table output (default: stdout)')
    g.add_argument('--membership', '-m', default=None, type=argparse.FileType('w'), metavar='FILE', help='QIIME-style OTU mapping file output')
    g.add_argument('--log', '-l', default=None, type=argparse.FileType('w'), metavar='FILE', help='progress log output')
    g.add_argument('--debug', default=None, type=argparse.FileType('w'), metavar='FILE', help='debug log output')
    args = p.parse_args()

    call_otus(args.table, args.fasta, args.output, args.dist, args.abund, args.pval, log=args.log, membership=args.membership, debug=args.debug)
