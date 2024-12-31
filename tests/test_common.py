from io import BytesIO
from unittest import TestCase


class TestCommon(TestCase):
    def test_generate_uuid(self):
        from pyklatchat_utils.common import generate_uuid

        # Default behavior
        self.assertIsInstance(generate_uuid(), str)

        # Maximum len
        long_uuid = generate_uuid(32)
        self.assertIsInstance(long_uuid, str)
        self.assertEqual(len(long_uuid), 32)

        # Minimum len
        long_uuid = generate_uuid(1)
        self.assertIsInstance(long_uuid, str)
        self.assertEqual(len(long_uuid), 1)

        # Error minimum len
        with self.assertRaises(ValueError):
            generate_uuid(0)

        # Error maximum len
        with self.assertRaises(ValueError):
            generate_uuid(33)

    def test_get_hash(self):
        from pyklatchat_utils.common import get_hash
        test_string = "test"

        # Default behavior
        self.assertIsInstance(get_hash(test_string), str)

        # Valid hash
        self.assertIsInstance(get_hash(test_string, algo="sha1"), str)

        # Invalid hash
        with self.assertRaises(ValueError):
            get_hash(test_string, algo="some_invalid_hash")

        # TODO: Test encoding

    def test_buffer_to_base64(self):
        from pyklatchat_utils.common import buffer_to_base64
        from pyklatchat_utils.common import base64_to_buffer

        test_bytes = BytesIO(b"test")
        encoded = buffer_to_base64(test_bytes)
        self.assertIsInstance(encoded, str)
        self.assertEqual(base64_to_buffer(encoded).getvalue(),
                         test_bytes.getvalue())

        # TODO: Test edge/error cases
