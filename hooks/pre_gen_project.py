import re
import sys

def validate_inputs():
    
    project_name = '{{ cookiecutter.title }}'

    # Check if the project name has at least 3 words
    if len(re.findall(r'\w+', project_name)) < 3:
        print('Error: The project name must be at least 3 words long.')
        sys.exit(1)


if __name__ == '__main__':
    validate_inputs()