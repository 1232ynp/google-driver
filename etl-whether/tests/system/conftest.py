import pytest


def pytest_addoption(parser):
    parser.addoption('--project', action='store')
    parser.addoption('--location', action='store')
    parser.addoption('--name', action='store')


@pytest.fixture
def project(request):
    return request.config.getoption("--project")


def location(request):
    return request.config.getoption("--location")


def name(request):
    return request.config.getoption("--name")