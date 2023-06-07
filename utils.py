import contextlib
import io
import sys
from unittest import TestCase

@contextlib.contextmanager
def mock_stdin(string: str):
    stream = io.StringIO(string)
    stream.seek(0)
    original = sys.stdin
    sys.stdin = stream
    yield
    sys.stdin = original


@contextlib.contextmanager
def mock_stdout():
    stream = io.StringIO()
    try:
        with contextlib.redirect_stdout(stream):
            yield stream
    except Exception as e:
        raise e
    finally:
        stream.seek(0)