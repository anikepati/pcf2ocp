from jinja2 import Template

def generate_openshift_deployment(app_name, image):
    with open("templates/deployment.yaml.j2") as f:
        template = Template(f.read())
    return template.render(app_name=app_name, image=image)
