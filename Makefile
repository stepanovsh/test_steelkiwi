requirements:
	@echo "Installing requirements"
	@pip install -v requirements.txt

make:
	python manage.py syncdb --settings=test_steelkiwi.settings.local
	
runserver:
	python manage.py runserver --settings=test_steelkiwi.settings.local

test:
	python manage.py test student -v 2

init:
	python manage.py loaddata --settings=test_steelkiwi.settings.local group/group.json
        python manage.py loaddata --settings=test_steelkiwi.settings.local student/student.json

