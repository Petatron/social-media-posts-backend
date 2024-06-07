import yaml

with open('environment.yml') as file:
    env = yaml.safe_load(file)

dependencies = env['dependencies']
pip_deps = None

for dep in dependencies:
    if isinstance(dep, dict) and 'pip' in dep:
        pip_deps = dep['pip']
        break

with open('requirements.txt', 'w') as req_file:
    for dep in pip_deps:
        req_file.write(f"{dep}\n")