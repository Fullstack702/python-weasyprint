import typing
import altair as alt
import pandas as pd


def generate_failures_chart(questions: typing.List[str], failures: typing.List[int]) -> alt.Chart:
	data = pd.DataFrame({'questions': questions, 'failures': failures})

	chart = alt.Chart(data).mark_bar().encode(
		x=alt.X(
			'questions',
			axis=alt.Axis(title='Question', labelAngle=0),
			sort=alt.EncodingSortField(
				field="failures",  # The field to use for the sort
				order="descending"  # The order to sort in
			)
		),
		y=alt.Y('failures', title='Failures'),
		color=alt.value('red'),
	)

	return chart
