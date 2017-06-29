import os
import sys
from argparse import ArgumentParser

def list_all_files(dirPath):
	'''List all files under dirPath directory'''
	if os.isdir(dirPath):
		return os.listdir(dirPath)
	else:
		return []

def change_all_files_under_directory(dirPath):
	if not dirPath:
		print 'No files existed under this path'
		return
	fileList = list_all_files(dirPath)
	for fileName in fileList:
		
def build_parser():
	parser = ArgumentParser()
	parser.add_argument('--directoryPath', type = str,
			dest = 'dirPath', help = 'dir to change files names under', default = '.')
	return parser
def main():
	parser = build_parser()
	options = parser.parse_args()
	dirPath = options.dirPath
	change_all_files_under_directoryPath(dirPath)
	print 'Changing complete.'
	show_all_files_list(dirPath)

if __name__ == '__main__':
	main()
