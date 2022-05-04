import os

import pytest
from starlette.testclient import TestClient

from app import main
from app.config import get_settings, Settings


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


# Fixtures have a scope associated with them  which indićates how often the fixture is invoked (in this case once per
# test module).
@pytest.fixture(scope="module")
def test_app():
    # set up
    # dependency_overrides is a dict of key/value pairs where the key is the dependency name and the value is
    # what we'd like to override it with:
    main.app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:
        # testing
        yield test_client

    # tear down
