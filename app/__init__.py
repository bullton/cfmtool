from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *


app = Flask(__name__)
app.config.from_object('config')
nav = Nav()

Bootstrap(app)


from app import views

@nav.navigation()
def mynavbar():
    return Navbar(
        'Customer Fault Mamagement Tool',
        View('Home', 'index'),
        Subgroup('File',
                View('Export','index'),
        ),
        Subgroup('Rule',
                View('New Rule','index'),
                View('Edit Rule','index'),
                View('Delete Rule','index'),
        ),
        Subgroup('Static',
                View('System Module/Severity Overview','index'),
                View('Category Overview','index'),
                View('Dedicated Test Finding','index'),
                View('TOP Pronto','index'),
                View('TOP Bloker','index'),
        ),
        Subgroup('Trend',
                View('Customer Pronto Trend','index'),
                View('Pronto Trend','index'),
                View('Top Pronto Trend','index'),
        ),
        View('Help', 'index'),
    )

# ...

nav.init_app(app)
