# from contextlib import ContextDecorator, ContextBaseClass
import os
import shutil
import subprocess
import tempfile
from os.path import dirname, abspath

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture
def tmp_dir_path():
    tmp_dir_path = tempfile.mkdtemp(suffix='cookiecutter', dir='/tmp')
    yield tmp_dir_path


def test_project_tests_passed(tmp_dir_path):
    template = dirname(dirname(abspath(__file__)))
    extra_context = {
        'function_name': 'mycli'
    }

    result = cookiecutter(template,
                          no_input=True,
                          extra_context=extra_context,
                          output_dir=tmp_dir_path)

    assert subprocess.check_call(['pytest', os.path.join(tmp_dir_path, 'mycli')]) == 0


def test_project_no_license(tmp_dir_path):
    template = dirname(dirname(abspath(__file__)))
    extra_context = {
        'function_name': 'mycli',
        'description': 'Uma breve descrição do seu projeto, para que é usado e como a vida fica incrível quando alguém começa a usá-lo.',
        'open_source_license':'Not open source'
    }

    result = cookiecutter(template,
                          no_input=True,
                          extra_context=extra_context,
                          output_dir=tmp_dir_path)

    assert subprocess.check_call(['pytest', os.path.join(tmp_dir_path, 'mycli')]) == 0