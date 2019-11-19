import os
from chromemgmt.chromepaths import bin_path


def install_chromedriver_to_path():
	current_path = os.environ['PATH']
	os.environ['PATH'] = f'{bin_path}:{current_path}'
