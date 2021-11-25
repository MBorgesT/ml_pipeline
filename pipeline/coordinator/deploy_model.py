import sys


def run(run_id):
    return 'Model deployed successfully'


if __name__ == '__main__':
    argv_len = len(sys.argv)
    if argv_len < 2:
        raise ValueError('Please inform the run id as a parameter')
    if argv_len != 2:
        raise ValueError('Please inform just one value as a parameter')

    run_id = sys.argv[1]
    run(run_id)
    
