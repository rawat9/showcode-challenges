# python3 -m unittest discover tests "test_*.py"

clean:
	trash ./build ./src.egg-info

add:
	python3 scripts/main.py --name $(name)
	pip3 install .
