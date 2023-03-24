import sys
from sorting_algo import sorting


def main(args):
    for arg_idx in (args):
        algo_1 = sorting()
        algo_1.main(int(arg_idx))

if __name__ == "__main__":
    argv_list = sys.argv[1:]
    main(argv_list)
