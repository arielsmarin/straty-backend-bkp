import importlib


def test_factory_defaults_to_r2(monkeypatch):
    monkeypatch.delenv("STORAGE_BACKEND", raising=False)
    from storage import factory

    module = importlib.reload(factory)
    assert module.STORAGE_BACKEND == "r2"


def test_factory_forces_r2_when_local_requested(monkeypatch):
    monkeypatch.setenv("STORAGE_BACKEND", "local")
    from storage import factory

    module = importlib.reload(factory)
    assert module.STORAGE_BACKEND == "r2"
