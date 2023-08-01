# TestBuilder
This application is designed for employees to pass tests. The director creates tests and adds users. Employees pass these tests
The program works locally, that is, the creation and passing of tests is done on the same computer

____

How to install:
```
git clone https://github.com/IlyaM1/TestBuilder.git
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Create file config.json:
```json
{
  "name": "YOUR_NAME_FOR_ADMIN",
  "password": "YOUR_PASSWORD_FOR_ADMIN",
  "path": "YOUR_PATH_FOR_FOLDER_WITH_PROJECT"
}
```
Change the input fields, replace YOUR_NAME_FOR_ADMIN, YOUR_PASSWORD_FOR_ADMIN, YOUR_PATH_FOR_FOLDER_WITH_PROJECT
YOUR_PATH_FOR_FOLDER_WITH_PROJECT looks like: C:\\Some_folder\\TestBuilder

Run main.py with `venv\Scripts\python.exe main.py`    

Front-end: https://github.com/IlyaM1    
Back-end: https://github.com/akrisfx
Design: https://github.com/MrMondego
