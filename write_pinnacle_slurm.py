#! /usr/bin/env python3

# This script generates a slurm file for the AHPCC Pinnacle cluster

# define some variables
jobname = 'test'
queue = 'comp06'
joboutput = 'smaddala.out'
numnodes = 1
numproc = 1
wall = 3 # this is in hours


# This section prints the header/required info for the slurm script
  
print('#SBATCH --job-name=' + jobname)
print('#SBATCH --partition' + queue)
print('#SBATCH -o', joboutput)
print('#SBATCH -e Trinity_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=smaddala@uark.edu')
print('#SBATCH --nodes=' + str(numnodes))
print('#SBATCH --ntasks-per-node=' + str(numproc))
print ('#SBATCH --time=' + str (wall) + ':00:00')
print ()

print('export OMP_NUM_THREADS=32')
 
# load required modules
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
print()
 
# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')

# commands for this job
print('# insert commands here')