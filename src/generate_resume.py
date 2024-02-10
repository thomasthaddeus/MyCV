"""generate_resume.py
_summary_

_extended_summary_
"""

import json
from jinja2 import Environment, FileSystemLoader

# Load the config file
with open('.conf/details_config.json', mode='r', encoding='utf-8') as file:
    config = json.load(file)

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('src/templates/template.html')

# Render the template with the config data
resume_html = template.render(config)

# Save the rendered HTML to a file
with open('resume.html', mode='w', encoding='utf-8') as file:
    file.write(resume_html)

print('Resume generated successfully!')
