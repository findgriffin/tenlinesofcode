
build: style types test

install:
	pip3 install -r requirements.txt

style:
	flake8 tenloc

types:
	mypy tenloc tests

test:
	coverage run --source tenloc -m unittest discover
	coverage html
	coverage report --fail-under=90

deploy:	build git-clean
	git push
	
git-clean:
	git diff-index --quiet HEAD
	test -z "$(git status --porcelain)"

run:
	./run.py

all:
	./run.py --all

say_my_name:
	./run.py say_my_name

clean:
	rm -rf **/__pycache__
	rm -rf **/*.pyc
