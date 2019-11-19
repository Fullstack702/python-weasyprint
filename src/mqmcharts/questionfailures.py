import typing
import numpy as np
import matplotlib.pyplot as plt


def generate_failures_chart(questions: typing.List[int], failures: typing.List[int], title: str, filename: str):
	x = [f'#{q}' for q in questions]

	y = failures
	key = []

	for i in x:
		l = i
		k = 'Question' + str(i.replace('#', ''))
		if len(i) == 3:
			key.append(l + ' : ' + k)
		else:
			key.append(l + '   : ' + k)

	plt.figure(figsize=(11, 6))
	textstr = '\n'.join(key)
	bar = plt.bar(x=x, height=y, color="red")
	plt.yticks(np.arange(0, max(y) + 5, 5))
	plt.title(title, fontsize=15, weight='bold')
	plt.xlabel('Question', fontsize=13)
	plt.ylabel('Failures', fontsize=13)
	# plt.text(5, 5, textstr, fontsize=14)
	plt.gca().yaxis.grid(True)
	plt.gca().set_axisbelow(True)

	plt.savefig(filename, bbox_inches='tight')

	plt.clf()