import random

from chromemgmt.pathinstall import install_chromedriver_to_path
from mqmcharts.auditscores_altair import generate_audit_score_chart, generate_rolling_audit_score_chart
from mqmcharts.piefailures import create_failure_pie_chart
from mqmcharts.questionfailures_altair import generate_failures_chart
from mqmpdf.render import generate_pdf

import os


def main():
	install_chromedriver_to_path()

	chart = generate_audit_score_chart(
		['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08',
		 '2019-01-09', '2019-01-10', '2019-01-11', '2019-01-12'],
		[91.0, 90.0, 91.0, 96.0, 84.0, 68.0, 78.0, 85.0, 85.0, 86.0, 99.9, 100.0]
	).properties(height=350)

	chart.save('audit_score_chart.png')

	audit_stats = [
		('Audit Start Time', 'October 10, 2019 at 10:30 AM EST'),
		('Audit End Time', 'October 10, 2019 at 12:30 PM EST'),
		('Audit Duration', '2 hours'),
		('Date of last audit submission', '10/09/2019'),
		('Auditor Name', 'Auditor #1'),
		('Premises', 'Restaurant #1'),
		('Premises Group', 'Restaurants'),
		('Premises Manager', 'Manager #1'),
		('Score', '96.00%')
	]

	audit_numbers = ['#1', '#2', '#3', '#4']

	site_scores = [
		('Site A', (68.0, 81.3, 91.0, 98.0)),  # a story of redemption
		('Site B', (100.0, 100.0, 100.0, 100.0)),  # 5 star restaurant
		('Site C', (100.0, 96.0, 80.0, 64.0)),  # a fall from grace
		('Site D', (70.0, 85.0, 85.0, 85.0))  # minimum wage minimum effort
	]

	chart = generate_rolling_audit_score_chart(audit_numbers, site_scores).properties(height=300)
	chart.save('rolling_audit_score_chart.png')

	questions = [
		'#1',
		'#2',
		'#3',
		'#4',
		'#5',
		'#6',
		'#7',
		'#8',
		'#9',
		'#10'
	]

	questions.sort(key=lambda _: random.random())

	failures = [
		random.randint(1, 24)
		for _ in range(len(questions))
	]

	chart = generate_failures_chart(questions, failures).properties(width=500, height=500)
	chart.save('failures_current_location.png')

	failures = [
		int(item * random.randint(1, 3))
		for item in failures
	]

	chart = generate_failures_chart(questions, failures).properties(width=500, height=500)
	chart.save('failures_all_locations.png')

	sections = [
		'Red Lights',
		'Layout, constructions, equipment, and utensils',
		'Housekeeping, cleaning, and waste practices',
		'Food storage condition and practices, temperature control practices',
		'People, personal hygiene practice, good hygienic practices, knowledge and competence',
		'Pest prevention and control',
		'HACCP based food safety manegement system and controls, supplier assurance, allergen information, traceability, incidents & complaints'
	]

	failures = [
		random.randint(1, 14)
		for _ in range(len(sections))
	]

	create_failure_pie_chart(sections, failures, 'section_failures_at_this_location.png')

	failures = [
		int(item * random.randint(1, 3))
		for item in failures
	]

	create_failure_pie_chart(sections, failures, 'section_failures_at_all_locations.png')

	generate_pdf(
		'mqmreport.html',
		'hello.pdf',
		audit_stats=audit_stats,
		audit_over_time_chart=os.path.abspath('audit_score_chart.png'),
		rolling_audit_score_chart=os.path.abspath('rolling_audit_score_chart.png'),
		failures_current_location_chart=os.path.abspath('failures_current_location.png'),
		failures_all_locations_chart=os.path.abspath('failures_all_locations.png'),
		pie_failures_at_this_location=os.path.abspath('section_failures_at_this_location.png'),
		pie_failures_at_all_locations=os.path.abspath('section_failures_at_all_locations.png')
	)

if __name__ == '__main__':
	main()
