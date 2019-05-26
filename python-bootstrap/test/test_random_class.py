import os
from unittest.mock import patch, call, MagicMock

import pytest

from src.random_class import RandomClass


def test_it_should_instantiate_random_class_with_parameter_default_to_one_test_example():
    # When
    random_class = RandomClass()

    # Then
    assert random_class.parameter == 1


@pytest.fixture
def random_class_fixture():
    return RandomClass(parameter=1)


def test_it_should_multiply_random_class_parameter_by_two_fixture_example(random_class_fixture):
    # When
    random_class_fixture.multiply_parameter()

    # Then
    assert random_class_fixture.parameter == 2


@patch('os.getenv')
def test_it_should_call_os_getenv_mock_patch_example(os_getenv_mock, random_class_fixture):
    # When
    path_variable = 'PATH'
    random_class_fixture.retrieve_environment_variable(path_variable)

    # Then
    assert os_getenv_mock.call_count == 1
    assert os_getenv_mock.call_args == call(path_variable)


def test_it_should_retrieve_os_path_stub_example(random_class_fixture):
    # Given
    os.getenv = MagicMock(return_value='stubbed/path')

    # When
    path_variable = 'PATH'
    retrieved_path = random_class_fixture.retrieve_environment_variable(path_variable)

    # Then
    assert retrieved_path == 'stubbed/path'
