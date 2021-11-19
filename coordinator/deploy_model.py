import sys
import os
from shutil import copyfile


WORKING_DIR = os.environ['WORKDIRPATH']
RUNS_PATH = WORKING_DIR + 'mlruns/0/'


def run(run_id):
    if not os.path.isdir(RUNS_PATH + run_id):
        raise ValueError('Please inform a valid run id')

    copyfile(
        RUNS_PATH + run_id + '/artifacts/model/data/model.h5',
        WORKING_DIR + 'production_model.h5'
    )
    print('Model deployed successfully')


if __name__ == '__main__':
    argv_len = len(sys.argv)
    if argv_len < 2:
        raise ValueError('Please inform the run id as a parameter')
    if argv_len != 2:
        raise ValueError('Please inform just one value as a parameter')

    run_id = sys.argv[1]
    run(run_id)
    
