isort:
	isort books/

style:
	flake8 books/

types:
	mypy books/

check:
	make isort style types
