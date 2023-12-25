import unittest
from acdh_wikidata_pyutils import WikiDataPerson, NoWikiDataUrlException


ARTHUR_SCHNITZLER_URL = "https://www.wikidata.org/wiki/Q44331"
ARTHUR_SCHNITZLER_ID = "Q44331"


class TestTestTest(unittest.TestCase):
    """Tests for `acdh-wikidata-pyutils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_testsetup(self):
        self.assertTrue(True)

    def test_002_valid_url(self):
        item = WikiDataPerson(ARTHUR_SCHNITZLER_URL)
        self.assertEqual(item.wikidata_id, ARTHUR_SCHNITZLER_ID)

    def test_003_non_valid_url(self):
        with self.assertRaises(NoWikiDataUrlException):
            WikiDataPerson(ARTHUR_SCHNITZLER_URL.replace("wikidata", "hansi"))
