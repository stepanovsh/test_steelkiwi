make:
    python manage.py syncdb --settings=test_steelkiwi.settings.local
    python manage.py loaddata --settings=test_steelkiwi.settings.local group/group.json
    python manage.py loaddata --settings=test_steelkiwi.settings.local student/student.json

runserver:
	$(MANAGE) runserver --settings=test_steelkiwi.settings.local

shell:
	$(MANAGE) shell --settings=test_steelkiwi.settings.local

syncdb:
	$(MANAGE) syncdb --settings=test_steelkiwi.settings.local

