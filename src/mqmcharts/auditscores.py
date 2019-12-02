import matplotlib

matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt
import typing


def generate_score_summary(dates: typing.List[str], score_percentages: typing.List[float], filename: str):
	plt.figure(figsize=(11, 7))

	dates_copy = dates[::]

	while len(dates_copy) < 12:
		dates_copy.append('N/A')

	scores_copy = score_percentages[::]

	while len(scores_copy) < 12:
		scores_copy.append(0.0)

	x = np.arange(0, 24, 2)

	bar = plt.bar(x=x, height=scores_copy, color='#00d1b2', width=1.5)

	check = [i for i in range(len(scores_copy)) if scores_copy[i] < 80]

	for i in check:
		bar[i].set_color('#ff3860')

	plt.yticks(np.arange(0, 110, 10))
	plt.xticks(np.arange(0, 24, 2))

	plt.title('Audit Scores Summary (Rolling last 12 audits)', fontsize=16, weight='bold')

	plt.xlabel('Date', fontsize=13, weight='bold')
	plt.ylabel('Audit Score', fontsize=13, weight='bold')

	plt.gca().yaxis.grid(True)
	plt.gca().set_axisbelow(True)

	plt.gca().spines['right'].set_visible(False)
	plt.gca().spines['top'].set_visible(False)
	plt.gca().set_xticklabels(dates_copy, rotation=45, weight='bold')

	for i in range(len(scores_copy)):
		if dates_copy[i] != 'N/A':
			annotation = f'{scores_copy[i]:.0f}%'
			offset = 0.25 if len(annotation) == 3 else 0.3
			plt.annotate(annotation, (x[i] - offset, scores_copy[i] + .8), weight='bold')

	plt.savefig(filename, bbox_inches='tight')

	plt.clf()


def generate_scores_across_all(sites: typing.List[typing.Tuple[str, typing.Tuple[str, ...], typing.Tuple[float, ...]]], filename: str):
	fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(11, 7), sharey=True)

	fig.suptitle('Audit Score Summary (across all sites)', fontsize=16, weight='bold')

	all_sites = []
	all_scores = []

	x = np.arange(0, 8, 2)

	for i, (site_name, _, scores) in enumerate(sites):
		all_sites.append(site_name)
		all_scores.append(scores)

		scores_copied = list(scores[::])

		while len(scores_copied) < 4:
			scores_copied.append(0)

		for j, score in enumerate(scores_copied):
			if(j == 0):
				axes[i].bar(x[j], score, width=1.25, color="#209cee")
			elif(j == 1):
				axes[i].bar(x[j], score, width=1.25, color="#00d1b2")	
			elif(j == 2):
    				axes[i].bar(x[j], score, width=1.25, color="#23d160")	
			elif(j == 3):
				axes[i].bar(x[j], score, width=1.25, color="#ff3860")					
			else:
				axes[i].bar(x[j], score, width=1.25)

	for i in range(4):
		axes[i].yaxis.grid(True)
		axes[i].set_axisbelow(True)

		axes[i].set_xticks(np.arange(0, 8, 2))

		axes[i].set_title(all_sites[i], fontsize=13)

		date_for_this_site = sites[i][1]

		axes[i].set_xticklabels(date_for_this_site, rotation=45, weight='bold')

		if i == 0:
			axes[i].set_ylabel('Scores', fontsize=13)

	for j in range(4):
		for i in range(4):
			scores = all_scores[j]

			current_score = scores[i]

			annotation = f'{current_score:.0f}%'
			offset = 0.7 if len(annotation) == 4 else 0.5

			axes[j].annotate(annotation, (x[i] - offset, current_score * 1.015), weight='bold')

	fig.savefig(filename, bbox_inches='tight')

	plt.clf()
