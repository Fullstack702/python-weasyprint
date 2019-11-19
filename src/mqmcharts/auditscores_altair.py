import altair as alt
import pandas as pd
import typing


def generate_audit_score_chart(days: typing.List[str], scores: typing.List[float], *,
							   score_color_percentage: float = 80.0) -> alt.Chart:
	data = pd.DataFrame({'days': days, 'scores': [score / 100.0 for score in scores]})

	root_chart = alt.Chart(data).mark_bar().encode(
		x=alt.X('days', axis=alt.Axis(title='Date', labelAngle=0)),
		y=alt.Y('scores', title='Audit Score')
	)

	bars = root_chart.mark_bar().encode(
		color=alt.condition(
			alt.datum.scores > score_color_percentage / 100.0,
			alt.value('orange'),
			alt.value('red')
		)
	)

	text = root_chart.mark_text(
		color='black',
		fontSize=13,
		dy=-15
	).encode(
		text=alt.Text('scores:Q', format='.2%')
	)

	return (bars + text).properties(background='white')


ScoreType = typing.List[typing.Tuple[str, typing.Tuple[typing.Union[int, float], ...]]]


def generate_rolling_audit_score_chart(audit_numbers: typing.List[str], site_scores: ScoreType) -> alt.Chart:
	sites = []
	scores = []
	audits = []

	for site, question_scores in site_scores:
		for i in range(len(question_scores)):
			sites.append(site)
			scores.append(question_scores[i])
			audits.append(audit_numbers[i])

	df = pd.DataFrame({'sites': sites, 'audits': audits, 'scores': scores})

	root_chart = alt.Chart(df).mark_bar().encode(
		x=alt.X('audits', title='', axis=alt.Axis(title='', labelAngle=0)),
		y=alt.Y('scores', title='Scores'),
		column=alt.Column('sites', title=''),
		color=alt.Color('audits', legend=None)
	)

	return root_chart.properties(background='white')
