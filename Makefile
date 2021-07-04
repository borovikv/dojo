test:
	find . -name "*.pyc" -exec rm -f {} \;
	PYTHONPATH=./src/ \
	py.test -s -vv