import random

from mpltools.install_local_fonts_folder import install_fonts_to_matplotlib
from mqmcharts.auditscores import generate_score_summary, generate_scores_across_all
from mqmcharts.piefailures import create_failure_pie_chart
from mqmcharts.questionfailures import generate_failures_chart
from mqmpdf.render import generate_pdf
from faker import Faker


import os


def main():
	install_fonts_to_matplotlib()

	audit_stats = [
		('Audit Start Time', '10th October 2019 at 10.30am GMT'),
		('Audit End Time', '10th October 2019 at 12.32pm GMT'),
		('Audit Duration', '2 hours 2 minutes'),
		('Date of last audit submission', '20/09/2019'),
		('Auditor Name', 'Auditor #1'),
		('Premises', 'Restaurant #1'),
		('Premises Group', 'Restaurants'),
		('Premises Manager', 'Manager #1'),
		('Score', '96%')
	]

	audit_results = [
		('PURCHASE, DELIVERY AND AMBIENT STORAGE', '5', '4', '0', '0'),
		('FROZEN, REFRIGERATED STORAGE AND PROBES', '10', '9', '0', '0'),
		('STOCK CONTROL', '5', '4', '1', '0'),
		('PREPARATION', '13', '11', '0', '0'),
		('COOKING, REHEATING AND COOLING', '10', '10', '0', '0'),
		('FOOT SERVICE AND DISPLAY', '8', '8', '0', '0'),
		('STAFF MEMBERS AND PERSONAL HYGIENE', '14', '12', '2', '0'),
		('CLEANING', '9', '8', '1', '0'),
		('PEST CONTROL AND REFUSE STORAGE', '5', '5', '0', '0'),
		('MANAGEMENT CONTROL AND DUE DILIGENCE', '9', '8', '0', '0'),
		('STRUCTURE AND EQUIMENT AUDIT', '16', '16', '0', '0')
	]

	site_scores = [
		('Site A', ('2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'), (68.0, 81.3, 91.0, 98.0)),
		# a story of redemption
		('Site B', ('2019-01-01', '2019-01-10', '2019-01-12', '2019-01-15'), (100.0, 100.0, 100.0, 100.0)),
		# 5 star restaurant
		('Site C', ('2019-02-01', '2019-02-02', '2019-02-03', '2019-02-04'), (100.0, 96.0, 80.0, 64.0)),
		# a fall from grace
		('Site D', ('2019-05-01', '2019-05-02', '2019-05-03', '2019-05-04'), (70.0, 85.0, 85.0, 85.0))
		# minimum wage minimum effort
	]

	generate_score_summary(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04'], [91.0, 92.0, 80.0, 74.0],
						   'audit_score_summary')
	generate_scores_across_all(site_scores, 'scores_across_all.png')
	
	table_height = 500
	questions = list(range(1, 11))
	td_len_1 = len(questions)
	td_height_1 = table_height / td_len_1
	

	# ie_1122_begin
	fake = Faker()
	questions_str = []
	for i in questions:
		k=fake.text(max_nb_chars=400)
		questions_str.append((i, k))
	# ie_1122_end
	
	questions.sort(key=lambda _: random.random())

	failures = [
		random.randint(1, 24)
		for _ in range(len(questions))
	]
	
	questions_2 = list(range(1,5))
	td_len_2 = len(questions_2)
	td_height_2 = table_height / td_len_2
	
	fake = Faker()
	questions_str_2 = []
	for i in questions_2:
		k=fake.text(max_nb_chars=400)
		questions_str_2.append((i, k))
	#page 4
	generate_failures_chart(questions, failures, 'Non-Conforming Areas - THIS SITE', 'failures_for_this_site.png')
	# generate_failures_chart(questions, questions_str, failures, 'Non-Conforming Areas - THIS SITE', 'failures_for_this_site.png')

	failures = [
		int(item * random.randint(1, 3))
		for item in failures
	]

	
	generate_failures_chart(questions_2, failures, 'Non-Conforming Areas - ALL SITES', 'failures_for_all_sites.png')
	# generate_failures_chart(questions, questions_str, failures, 'Non-Conforming Areas - ALL SITES', 'failures_for_all_sites.png')


	

	sections = [
		'Red Lights',
		'Layout, constructions, equipment, and utensils',
		'Housekeeping, cleaning, and waste practices',
		'Food storage condition and practices, temperature control practices',
		'People, personal hygiene practice, good hygienic practices, knowledge and competence',
		'Pest prevention and control',
		'HACCP based food safety management system and controls, supplier assurance, allergen information, traceability, incidents & complaints'
	]

	failures = [
		random.randint(1, 14)
		for _ in range(len(sections))
	]

	create_failure_pie_chart(sections, failures, "Audit Fails By Section (this location)",
							 'section_failures_at_this_location.png')

	failures = [
		int(item * random.randint(1, 3))
		for item in failures
	]

	create_failure_pie_chart(sections, failures, "Audit Fails By Section (All locations)",
							 'section_failures_at_all_locations.png')

	generate_pdf('mqmreport.html', 'hello.pdf', audit_stats=audit_stats, all_graphs=map(os.path.abspath, [
		'audit_score_summary.png',
		'scores_across_all.png',
		'failures_for_this_site.png',
		'failures_for_all_sites.png',
		'section_failures_at_this_location.png',
		'section_failures_at_all_locations.png'
	]), 
	questions = questions_str,
	td_height_1 = td_height_1,
	td_height_2 = td_height_2,
	questions_2 = questions_str_2,
	red_lights=[
		(1,
		 fake.text(max_nb_chars=400),
		 'only washbasin available located in customer bathroom twelve meters away from kitchen', '', '', ''),
		 (17,
		 fake.text(max_nb_chars=400),
		 'only washbasin available located in customer bathroom twelve meters away from kitchen', '', '', ''),
		 (2,
		 fake.text(max_nb_chars=400),
		 'only washbasin available located in customer bathroom twelve meters away from kitchen', '', '', '')
	], non_conforming_areas=[
		('Storage and Handling of Waste', [
			(25,
			 'All refuse must be discarded into closable waste containers which must be clean, constructed of appropriate material, in good condition, and designed to prevent hand contamination',
			 'lid missing for two of six waste containers'),
			 (125,
			 fake.text(max_nb_chars = 400),
			 'lid missing for two of six waste containers'),
			 			 (67,
			 fake.text(max_nb_chars = 400),
			 'lid missing for two of six waste containers')
		]),
		('Allergen Management', [
			(113,
			 'Information on allergens in raw materials must be available, kept up to date and used to generate customer allergen information documents detailing allergens present in all meals. Allergen signage must be visible to customers',
			 'signage/paper menus not updated to reflect addition of gluten to menu item'),
(13,
			 fake.text(max_nb_chars = 400),
			 'signage/paper menus not updated to reflect addition of gluten to menu item'),			 
(63,
			 fake.text(max_nb_chars = 400),
			 'signage/paper menus not updated to reflect addition of gluten to menu item')			 
		])
	], staff_competence=[
		(125, 101,
		 'There are signed off and verified cleaning records in place which reflect each area or item detailed on the cleaning schedule or matrix', '', '', 'Pass'),
		(126, 114,
		 'Records must be in place to facilitate traceability from raw materials to meals prepared - as a minimum incoming goods records must identify lot/batch codes, or date code for all incoming product', '', '', 'Pass'),
		(127, 120,
		 'Critical Control Points must be identified and this identification must be documented with clear reasoning behind the decision to identify them as CCP\'s, such as the use of a decision tree. Or Safe Food Better Business be implemented', '', '', 'Fail'),
		(128, 30,
		 'Utensils that are not in immediate use must be protected from contamination by environmental sources by ensuring proper and clean storage, including covering as appropriate', '', '', 'Pass'),
		(129, 22,
		 'Wash-up and hand wash sinks must be in sound condition, clean, constructed of appropriate materials, free from leaks of any kind and have an adequate supply of hot and cold water', '', '', 'Pass')
	], audit_results=audit_results)


if __name__ == '__main__':
	main()
