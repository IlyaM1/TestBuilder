# Test Builder Application
This application is designed for employees to pass tests. The director creates tests and adds users. Employees pass these tests using a local application installed on their computers.

___
## Installation
To install the Test Builder application, follow these steps:

### Clone the repository:
```git clone https://github.com/IlyaM1/TestBuilder.git```

### Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate
```

### Install the required packages:
```bash
pip install -r requirements.txt
```

### Create a config.json file with the following content:
```json
{
  "name": "YOUR_NAME_FOR_ADMIN",
  "password": "YOUR_PASSWORD_FOR_ADMIN",
  "path": "YOUR_PATH_FOR_FOLDER_WITH_PROJECT"
}
```
Replace `YOUR_NAME_FOR_ADMIN`, `YOUR_PASSWORD_FOR_ADMIN`, and `YOUR_PATH_FOR_FOLDER_WITH_PROJECT` with appropriate values. The path value should point to a folder where the project will be stored (e.g., C:\Some_folder\TestBuilder).

### Run the main script:
`venv\Scripts\python.exe main.py`

## Contributors:
#### Front-end: https://github.com/IlyaM1

#### Back-end: https://github.com/akrisfx

#### Design: https://github.com/MrMondego

## Application Architecture
The Test Builder application consists of three main components:

### Front-end (View):
 Responsible for rendering the user interface and handling user interactions. The front-end is built using PyQt5.
### Back-end (Model):
 Contains the business logic and data access layer. The back-end interacts with the database and performs various operations like user authentication, test creation, and test submission.
### Database:
 Stores user information, tests, and test results. The application uses SQLite as its database.
## Application Workflow
- The director creates a config.json file with their credentials and the project path.
- The director runs the main.py script to start the application.
- The director can create tests and add users to the system.
- Employees receive their credentials and install the application on their computers.
- Employees log in using their credentials and take the assigned tests.
- Test results are stored in the database and can be accessed by the director.
## Directory Structure
- `config.json:` Configuration file with the director's credentials and project path.
- `main.py:` The main script that starts the application.
- `View:` Contains PyQt5 UI files and related classes.
- `Model:` Contains the back-end logic, data access layer, and related classes.
- `db:` Contains SQLite database files and related modules.
- `test:` Contains test data and related scripts.
## Contributing
We welcome contributions to the Test Builder application. To contribute, follow these steps:

### Fork the repository.
Create a new branch for your feature or bug fix.
Make changes and commit them.
Push your changes to your forked repository.
Open a pull request against the original repository.
## License
The Test Builder application is released under the MIT License. See the [LICENSE](https://github.com/IlyaM1/TestBuilder/blob/main/LICENSE) file for more information.
