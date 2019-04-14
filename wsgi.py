import functools
import itertools
import subprocess

import flask
import psutil

from healthchecker.ls import ls
from healthchecker.maker import maker_generator
from healthchecker.stats import stats


app = flask.Flask(__name__)


def str_function_wrapper(function):

    @functools.wraps(function)
    def inner(*args, **kwargs):

        s = function(*args, **kwargs)
        if isinstance(s, bytes):
            s = s.decode('utf-8')

        return (
            f'<html><tt>{s:s}</tt></html>'
            .replace('\n', '<br>')
        )

    return inner


def registrar(rule, function):
    route_registrar = app.route(rule)
    wrapped_function = str_function_wrapper(function)
    route_registrar(wrapped_function)


list(itertools.starmap(registrar, (
    ('/', lambda: 'hello world ☃'),
    ('/ls', ls),
    ('/stats', stats),
    *maker_generator(app)
)))
