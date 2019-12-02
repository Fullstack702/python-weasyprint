import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt
import typing


def create_failure_pie_chart(questions: typing.List[str], failures: typing.List[int], title: str, filename: str):
	plt.figure(figsize=(11, 7))
	wedges, texts, val = plt.pie(failures, wedgeprops=dict(width=0.5), autopct='%1.0f%%', pctdistance=1.1, colors=['#209cee', '#00d1b2','#23d160', '#ff3860','#9467bd','#8c564b','#e377c2'],
	# wedges, texts, val = plt.pie(failures, wedgeprops=dict(width=0.5), autopct='%1.0f%%', pctdistance=1.1, 
								 startangle=-40)

	bbox_props = {
		'boxstyle': 'square,pad=0.3',
		'fc': 'w',
		'ec': 'k',
		'lw': 0.72
	}

	kw = {
		'arrowprops': {
			'arrowstyle': '-'
		},
		'bbox': bbox_props,
		'zorder': 0,
		'va': 'center'
	}

	plt.title(title, fontsize=15, weight='bold')

	plt.legend(
		wedges,
		questions,
		loc='upper center',
		bbox_to_anchor=(0.5, -0.00),
		fancybox=True
	)

	plt.savefig(filename, bbox_inches='tight')
