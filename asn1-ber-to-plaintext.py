import sys

with open(sys.argv[1], 'rb') as f:
    data = f.read()

print('\n'.join(['0x%.2X -- [%s]' % (c, bin(c)[2:].rjust(8, '0')) for c in data]))
