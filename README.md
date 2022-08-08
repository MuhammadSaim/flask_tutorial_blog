# Blog & Private Journaling WebApp

## Requirements
- Python >= 3.8
- Flask  >= 2.2.0
- Flask SQLAlchemy >= 2.5.1
- Flask Migrate >= 3.1.0

### Configuration

1. Clone the repo
```shell
git clone https://github.com/MuhammadSaim/flask_tutorial_blog.git
```
2. Step into folder
```shell
cd blog
```
3. Create virtual environment
```shell
virtualenv venv 
```
4. Activate the venv
```shell
source venv/bin/activate
```
5. Install the dependencies
```shell
pip install -r requirements.txt
```

6. Copy the <kbd>.env.example</kbd> to <kbd>.env</kbd> and setup your DB on <kbd>.env</kbd>

7. Run the migrations.
```shell
flask db upgrade
```

8. Run the flask app
```shell
python run.py
```

Happy Coding