import typing
import numpy as np
import matplotlib.pyplot as plt


# def generate_failures_chart(questions: typing.List[int], questions_str: typing.List[str], failures: typing.List[int], title: str, filename: str):

def generate_failures_chart(questions: typing.List[int], failures: typing.List[int], title: str, filename: str):
	combined_questions = list(zip(questions, failures))

	sorted_combined = sorted(combined_questions, key=lambda item: item[1], reverse=True)

	questions = [i[0] for i in sorted_combined]
	failures = [i[1] for i in sorted_combined]

	plt.figure(figsize=(5, 7))

	questions_copy = questions[::]

	questions_annotated = [f'#{q}' for q in questions_copy]

	failures_copy = failures[::]

	x = np.arange(0, len(questions_copy) * 2, 2)

	bar = plt.bar(x=x, height=failures_copy, color='#ff3860', width=1.5)


	y_height = int(round(max(failures_copy) * 0.1)*10)
	y_offset = 0.015*y_height
	
	plt.yticks(np.arange(0, int(max(failures_copy) * 1.5), 10))
	# plt.yticks(np.arange(0, int(100), 10))
	plt.xticks(np.arange(0, len(questions_copy) * 2, 2))

	plt.title(title, fontsize=16, weight='bold', y=1.05)

	plt.xlabel('Question', fontsize=13, weight='bold')
	plt.ylabel('Failure Count', fontsize=13, weight='bold')
	# ie_1122_begin
	# textstr = '\n'.join(questions_str)
	# plt.text(25, 3, textstr, fontsize=14)	
	# ie_1122_end
	plt.gca().yaxis.grid(True)
	plt.gca().set_axisbelow(True)

	plt.gca().spines['right'].set_visible(False)
	plt.gca().spines['top'].set_visible(False)
	plt.gca().set_xticklabels(questions_annotated, weight='bold')

	for i in range(len(failures_copy)):
		annotation = f'{failures_copy[i]}'
		offset = 0.5 if len(failures_copy) > 4 else 0.2		
		# offset = 0.2 if len(annotation) == 2 else 0.15
		plt.annotate(annotation, (x[i] - offset, failures_copy[i]+y_offset), weight='bold')

	plt.savefig(filename, bbox_inches='tight')

	plt.clf()