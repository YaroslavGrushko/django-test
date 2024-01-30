**Django useful Tips:**

1. Open Vs Code > ctrl+shift+p > Python: Create Environment > Venv > Select recommended Interpreter > install libs from requirements.txt
2. VS Code > Launch Django debugger

To make changes from Model structure to Db:
1. **py manage.py makemigrations test_example**
2. **py manage.py migrate**

To create admin user:
**py manage.py createsuperuser**

Admin panel:
**127.0.0.1:8000/admin/**

To collect static files:
**py manage.py collectstatic**
