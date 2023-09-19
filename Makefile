install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest --nbval Project/*.ipynb
	python -m pytest -vv --cov=lib --cov=script --cov-report term-missing Project/test_*.py

format:	
	black Project/*.py
	nbqa black Project/*.ipynb  

lint:
	nbqa ruff Project/*.ipynb
	ruff check Project/*.py 

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here
		
all: install lint test format deploy
