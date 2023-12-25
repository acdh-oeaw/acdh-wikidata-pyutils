[![flake8 Lint](https://github.com/acdh-oeaw/acdh-wikidata-pyutils/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-wikidata-pyutils/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/acdh-wikidata-pyutils/actions/workflows/test.yml/badge.svg)](https://github.com/acdh-oeaw/acdh-wikidata-pyutils/actions/workflows/test.yml)

# acdh-wikidata-pyutils
Utitliy package to fetch data from Wikidata

## development

* create virtual env `python -m venv venv` and activate it `source venv/bin/activate`
* install dev-dependencies `pip install -r requirements_dev.txt`
* install acdh-wikidata-pyutils locally `pip install -e .`
* run tests `coverage run -m pytest`