isort:
	isort books/

isort_test:
	isort tests/

style:
	flake8 books/

style_test:
	flake8 tests/

types:
	mypy books/

pytest:
	python -m pytest 

test:
	make isort_test style_test pytest

check:
	make isort style types
