import sarewt.data_reader as dare
import os
import glob

base_dir = '/eos/project/d/dshep/TOPCLASS/DijetAnomaly/VAE_results/run_101/sample_results/minl1l2_loss'
sample_dirs =  glob.glob(base_dir+'/*q*/*')

print('*'*10+'\ncounting number of events and files in subdirectories of {}\n'.format(base_dir)+'*'*10)

num_files = []
num_events = []

for sample_dir in sample_dirs:
	print('reading events in {}'.format(sample_dir))
	reader = dare.DataReader(sample_dir)
	n_files, n_events = reader.count_files_events_in_dir()
	num_files.append(n_files)
	num_events.append(n_events)

for sample_dir, nn, ff in zip(sample_dirs, num_events, num_files):
	print("{: <40}: {: >10} events in {: >10} files".format(os.path.basename(sample_dir), nn, ff))