import re
import os

os.chdir('../full_sim_random')
files = os.listdir('.')

for f in files:
    tmp = re.sub(r"_", 'n_', f)
    tmp = re.sub(r"^fullfn", 'simf', tmp)
    tmp = re.sub(r".csv", 'cv.csv', tmp)
    os.rename(f, tmp)

os.chdir('../full_sim_random')
files = os.listdir('.')

for f in files:
    tmp = re.sub(r"_", 'n_', f)
    tmp = re.sub(r"^fullrn", 'simr', tmp)
    tmp = re.sub(r".csv", 'cv.csv', tmp)
    os.rename(f, tmp)

