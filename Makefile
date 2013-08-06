requirements:
	@echo "Installing requirements"
	@pip install —exists-action=s -r requirements.txt

make:
	python manage.py syncdb --settings=test_steelkiwi.settings.local
	python manage.py loaddata --settings=test_steelkiwi.settings.local group/group.json
	python manage.py loaddata --settings=test_steelkiwi.settings.local student/student.json

runserver:
	python manage.py runserver --settings=test_steelkiwi.settings.local

test:
	python manage.py python manage.py test student -v 2


