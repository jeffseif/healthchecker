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
            '<html><tt>{s:s}</tt></html>'
            .format(s=s)
            .replace('\n', '<br>')
        )

    return inner


def register_endpoint(rule, function):
    app.add_url_rule(
        rule,
        endpoint=rule.split('/')[1],
        view_func=str_function_wrapper(function),
    )


list(itertools.starmap(
    register_endpoint,
    (
        ('/', lambda: 'hello world ☃'),
        ('/ls', ls),
        ('/stats', stats),
        *maker_generator(app)
    )
))
