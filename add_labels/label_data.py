import pandas as pd 
import subprocess
import sys
import os

source = sys.argv[1]
dest = sys.argv[2]
labels = sys.argv[3]

df = pd.read_csv(labels)

df = df.fillna('EMPTY')

subprocess.call(['mkdir', '-p', dest])
for subjects in list(set(df.Subject)):
	subject_list = subjects.split(', ')
	for subject in subject_list:
		subprocess.call(['mkdir', '-p', os.path.join(dest, subject)])

folders = [file.split('/')[-2] for file in df.SourceFile]
filenames = [file.split('/')[-1] for file in df.SourceFile]
for folder, filename, subjects in zip(folders, filenames, df.Subject):
	subject_list = subjects.split(', ')
	for subject in subject_list:
		subprocess.call(['mv', os.path.join(source, folder, filename), os.path.join(dest, subject, filename)])