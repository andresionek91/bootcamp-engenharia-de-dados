import jinja2
import yaml
import os


def renderiza_template():
    with open('redshift.yaml.j2', 'r') as f:
        redshift_yaml = f.read()

    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)


    redshift_template = jinja2.Template(redshift_yaml)
    redshift_rendered = redshift_template.render({**config, **os.environ})

    with open('redshift.yaml', 'w') as f:
        f.write(redshift_rendered)
