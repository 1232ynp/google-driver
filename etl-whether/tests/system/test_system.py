from googleapiclient import discovery
from googleapiclient import errors
import pytest


class TestCloudScheduler:
    @pytest.fixture
    def job_name(self, request):
        return "projects/" + request.config.getoption('--project') + "/locations/" + request.config.getoption('--location') + "/jobs/" + request.config.getoption('--name')

    @pytest.fixture
    def client(self):
        return discovery.build('cloudscheduler', 'v1')

    def test_exist(self, job_name, client):
        request = client.projects().locations().jobs().get(name=job_name)
        response = request.execute()
        assert response["name"] == job_name

    def test_run(self, job_name, client):
        body = {}
        request = client.projects().locations().jobs().run(name=job_name, body=body)
        response = request.execute()
        assert isinstance(response, dict)


class TestCloudFunctions:
    @pytest.fixture
    def func_name(self, request):
        return "projects/" + request.config.getoption('--project') + "/locations/" + request.config.getoption('--location') + "/functions/" + request.config.getoption('--name')

    @pytest.fixture
    def client(self):
        return discovery.build('cloudfunctions', 'v2')

    def test_exist(self, func_name, client):
        request = client.projects().locations().functions().get(name=func_name)
        response = request.execute()
        assert response["name"] == func_name

    def test_run(self):
        # cloud_functionsが正常に実行できるか
        return


class TestCloudPubsub:
    @pytest.fixture
    def topic_name(self, request):
        return "projects/" + request.config.getoption('--project') + "/topics/" + request.config.getoption('--name')

    @pytest.fixture
    def client(self):
        return discovery.build('pubsub', 'v1')

    def test_exist(self, topic_name, client):
        request = client.projects().topics().get(topic=topic_name)
        response = request.execute()
        assert response["name"] == topic_name

    def test_run(self, topic_name, client):
        body = {
            "messages": [
                {
                    "data": "test",
                }
            ]
        }
        request = client.projects().topics().publish(topic=topic_name, body=body)
        response = request.execute()
        assert isinstance(response, dict)

