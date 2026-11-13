from relnotes.notes import read_notes
from relnotes.settings import load_settings
from relnotes.web import create_app


def test_health_ok():
    client = create_app().test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "ok"


def test_notes_read():
    assert read_notes()[0][0] == "1.1.0"


def test_settings_by_app_env():
    assert load_settings("staging")["APP_MODE"] == "staging"
    assert load_settings("production")["APP_MODE"] == "production"
    assert load_settings("")["APP_MODE"] == "default"


def test_deliberate_failure_first_push():
    assert False, "first push fails on purpose to test the deliver skip line"
