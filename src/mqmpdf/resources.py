import os
import typing
import base64


def render_image_format(root_directory: str, resource_name: str) -> str:
	filepath = os.path.join(root_directory, resource_name)

	with open(filepath, 'rb') as f:
		image_data = f.read()

	image_data = base64.b64encode(image_data).decode('utf8')

	x = f'<img src="data:image/png;base64, {image_data}"/>'

	return x


def render_image_from_path(image_filename: str, **styles) -> str:
	with open(image_filename, 'rb') as f:
		image_data = f.read()

	image_data = base64.b64encode(image_data).decode('utf8')

	style_string = ' '.join([
		f'{key}="{val}"'
		for key, val in styles.items()
	])

	x = f'<img src="data:image/png;base64, {image_data}" {style_string}/>'

	return x


def render_css_format(root_directory: str, resource_name: str) -> str:
	filepath = os.path.join(root_directory, resource_name)

	with open(filepath, 'r') as f:
		css_data = f.read()

	return f'<style>\n{css_data}\n</style>'


def render_js_format(root_directory: str, resource_name: str) -> str:
	raise Exception('no')


resource_format_mapping: typing.Dict[str, typing.Callable[[str, str], str]] = {
	'image': render_image_format,
	'css': render_css_format,
	'js': render_js_format
}


def render_resource(root_directory: str, resource_name: str, resource_type: str, *args, **kwargs) -> str:
	return resource_format_mapping[resource_type](root_directory, resource_name, *args, **kwargs)
