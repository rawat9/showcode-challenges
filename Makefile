add:
	trash ./build ./src.egg-info
	python3 scripts/main.py --name $(name)
	pip3 install . --use-pep517
