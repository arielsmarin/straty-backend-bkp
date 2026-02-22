def test_upload_tiles_parallel_caps_workers_at_4(monkeypatch):
    from storage import storage_r2

    class _FakeS3:
        def put_object(self, **kwargs):
            return kwargs

    class _FakeFuture:
        def __init__(self, fn, *args):
            self._fn = fn
            self._args = args

        def result(self):
            return self._fn(*self._args)

    class _FakeExecutor:
        def __init__(self, max_workers):
            captured["workers"] = max_workers

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def submit(self, fn, *args):
            return _FakeFuture(fn, *args)

    captured = {}
    monkeypatch.setattr(storage_r2, "s3_client", _FakeS3())
    monkeypatch.setattr(storage_r2, "ThreadPoolExecutor", _FakeExecutor)
    monkeypatch.setattr(storage_r2, "as_completed", lambda futures: futures)

    storage_r2.upload_tiles_parallel(
        [("clients/a/cubemap/s/tiles/b/t.jpg", b"jpg")],
        max_workers=99,
    )

    assert captured["workers"] == 4
