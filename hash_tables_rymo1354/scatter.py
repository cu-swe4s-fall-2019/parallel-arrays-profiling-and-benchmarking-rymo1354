import os
import matplotlib.pyplot as plt
import sys
import argparse
import matplotlib
matplotlib.use('Agg')


def check_path(path):
    """
    Determines if passed path exists and has read access
    Arguments
    _________
    path: string of the path of interest

    Returns
    _______
    True : if path exists and is readable
        Otherwise, returns False
    """

    if os.path.isfile(path) and os.access(path, os.R_OK):
        return True
    else:
        return False


if __name__ == '__main__':
    # adding arguments
    parser = argparse.ArgumentParser(
        description='A script to draw scatter plot from STDIN.',
        prog='scatter')

    parser.add_argument('--out_file', type=str,
                        help='Name of the output file', required=True)
    parser.add_argument('--x_label', type=str,
                        help='Name of the x-axis label', required=True)
    parser.add_argument('--y_label', type=str,
                        help='Name of the y-axis label', required=True)

    args = parser.parse_args()

    if check_path(args.out_file) is False:
        print('File does not exist or is not accessible')
        sys.exit(1)

    X = []
    Y = []
    i = 0
    for line in sys.stdin:
        A = line.rstrip().split()
        if len(A) >= 2:
            try:
                X.append(float(A[0]))
                Y.append(float(A[1]))
            except ValueError:
                print(str(A[0]) + ' not valid integer')
                continue
        elif len(A) == 1:
            try:
                X.append(float(i))
                Y.append(float(A[0]))
                i += 1
            except ValueError:
                print(str(A[0]) + ' not valid integer')
                continue
        else:
            print('Empty file')
            sys.exit(1)

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel(args.x_label)
    ax.set_ylabel(args.y_label)

    plt.savefig(args.out_file, bbox_inches='tight')
