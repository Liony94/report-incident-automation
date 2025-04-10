import yaml
from jinja2 import Environment, FileSystemLoader

with open('iocs.yaml', 'r') as file:
    data = yaml.safe_load(file)

#config jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.txt')

report = template.render(files=data['files'])

with open('incident_report.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(report)
