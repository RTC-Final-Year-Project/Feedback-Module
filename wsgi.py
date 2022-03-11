import click
from flask import Flask
from flask.cli import with_appcontext
from App.main import app
from App.controllers import create_user
from App.database import init_db

@app.cli.command("init")
def initiialize():
    init_db(app)
    print('database intialized')

@app.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')