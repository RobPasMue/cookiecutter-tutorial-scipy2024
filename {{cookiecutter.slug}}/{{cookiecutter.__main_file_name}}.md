---
title: "{{ cookiecutter.title }}"
tags:
- python
status: work-in-progress
---

# {{ cookiecutter.title }}

## More Info

{% if cookiecutter.reference_docs %}
* [{{cookiecutter.reference_docs.title}}]({{cookiecutter.reference_docs.url}})
{% endif %}
{% if cookiecutter.howto_docs %}
* [{{cookiecutter.howto_docs.title}}]({{cookiecutter.howto_docs.url}})
{% endif %}
* [How to use strings as name aliases in Python enums](https://www.notinventedhere.org/articles/python/how-to-use-strings-as-name-aliases-in-python-enums.html)
