from unittest import TestCase


class TestHttpUtils(TestCase):
    def test_respond(self):
        from pyklatchat_utils.http_utils import respond
        # TODO

    def test_response_ok(self):
        from starlette.responses import JSONResponse
        from pyklatchat_utils.http_utils import response_ok
        self.assertIsInstance(response_ok, JSONResponse)