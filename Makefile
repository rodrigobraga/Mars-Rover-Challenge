venv:
	python3 -m venv env


install: venv
	bash -c "source env/bin/activate && pip install -r requirements.txt"


codestyle:
	bash -c "source env/bin/activate && pycodestyle rover.py mission.py tests.py"


unittest:
	bash -c "source env/bin/activate && py.test tests.py -s"


coverage:
	bash -c "source env/bin/activate && py.test tests.py --cov-report term-missing --cov rover.py"


test: codestyle unittest coverage


mission:
	python3 mission.py
