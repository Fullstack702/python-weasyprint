from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
from functools import partial

from mqmpdf.pdfgen import PdfGenerator
from mqmpdf.resources import render_resource, render_image_from_path
from weasyprint import HTML, CSS

root_environment_path: str = os.path.abspath(os.path.dirname(__file__))
root_template_path: str = os.path.join(root_environment_path, 'templates')
root_static_path: str = os.path.join(root_environment_path, 'static')


def get_page_body(boxes):
	for box in boxes:
		print(box)
		if box.element_tag == 'body':
			return box

		return get_page_body(box.all_children())


def generate_pdf(template_name: str, pdf_filename: str, **template_args) -> None:
	jinja_env = Environment(
		autoescape=select_autoescape(enabled_extensions=[]),
		loader=FileSystemLoader(searchpath=root_template_path),
	)

	# with this should be possible to call render_resource('image.png', 'image')
	jinja_env.globals['render_resource'] = partial(render_resource, root_static_path)
	jinja_env.globals['render_image_from_path'] = render_image_from_path

	header_html = jinja_env.get_template('header.html').render()

	templated_html = jinja_env.get_template(template_name).render(**template_args)

	pdf = PdfGenerator(templated_html, header_html).render_pdf()

	pdf.write_pdf(pdf_filename)
