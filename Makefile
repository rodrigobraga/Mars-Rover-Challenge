build:
	docker-compose build


codestyle:
	docker-compose run --rm application pycodestyle rover.py mission.py tests.py


unittest:
	docker-compose run --rm application py.test tests.py -s


coverage:
	docker-compose run --rm application py.test tests.py --cov-report term-missing --cov rover.py


test: codestyle unittest coverage


mission:
	docker-compose run --rm application python mission.py
