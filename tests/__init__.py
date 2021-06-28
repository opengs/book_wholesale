from os import environ
from starlette.testclient import TestClient

testClient:TestClient = None

from src.main import app

def get_test_client() -> TestClient:
    global testClient
    return testClient

def setup_module(module):
    global testClient
    global tempConfigDir
    environ["DB_URL"] = "sqlite://:memory:"

    testClient = TestClient(app).__enter__()

def teardown_module(module):
    global testClient
    testClient.__exit__()
