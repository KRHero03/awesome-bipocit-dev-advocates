from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

Loader = FileSystemLoader('./templates', followlinks=True)
env = Environment(loader=Loader, autoescape=select_autoescape(['html', 'xml']))

if __name__ == "__main__":
    template = env.get_template('readme_template.md')

    with open('members.json') as json_file:
        json_data = json.load(json_file)

    site = {"title": "Awesome BIPOCIT Dev Advocates"}
    content = template.render(advocates = json_data.items(), site=site)
    Path('README.md').write_text(content)
