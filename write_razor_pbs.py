#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC Razor cluster

# define some variables
jobname = 'test'
queue = 'onenode16core'
joboutput = 'smaddala.out'
numnodes = 1
numproc = 1
wall = 3 # this is in hours


# This section prints the header/required info for the PBS script
print('#PBS -N', jobname) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STOUT and STDERR into single file
print('#PBS -o', joboutput + '$PBS_JOBID') # set the name of the job output file
print('#PBS -l nodes=' + str(numnodes) + ':ppn=' + str(numproc)) # how many resources to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hour)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')

