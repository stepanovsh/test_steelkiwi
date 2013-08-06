default: 
	requirements db init run

requirements:
	@echo "Installing requirements"
	@pip install -r requirements.txt

db:
	python manage.py syncdb --settings=test_steelkiwi.settings.local

run:
	python manage.py runserver --settings=test_steelkiwi.settings.local

test:
	python manage.py test student -v 2

init:
	python manage.py loaddata --settings=test_steelkiwi.settings.local group/group.json
	python manage.py loaddata --settings=test_steelkiwi.settings.local student/student.json
