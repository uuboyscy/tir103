install:
	pipenv install $(package) && pipenv requirements > requirements.txt && pipenv requirements --dev > requirements-dev.txt

uninstall:
	pipenv uninstall $(package) && pipenv requirements > requirements.txt && pipenv requirements --dev > requirements-dev.txt

lock:
	pipenv lock && pipenv requirements > requirements.txt && pipenv requirements --dev > requirements-dev.txt
