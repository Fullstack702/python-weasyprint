from os.path import expanduser
import matplotlib

matplotlib.use('agg')
import os
import matplotlib.font_manager as font_manager

home = expanduser("~")


def install_fonts_to_matplotlib():
	fonts_folder = os.path.join(home, '.fonts')

	font_dirs = [fonts_folder]
	font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
	font_list = font_manager.createFontList(font_files)
	font_manager.fontManager.ttflist.extend(font_list)

	matplotlib.rcParams['font.family'] = 'Roboto'
