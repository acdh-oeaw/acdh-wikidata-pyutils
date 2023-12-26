import unittest

from acdh_wikidata_pyutils import NoWikiDataUrlException, WikiDataPerson

ARTHUR_SCHNITZLER_URL = "https://www.wikidata.org/wiki/Q44331"
ARTHUR_SCHNITZLER_ID = "Q44331"
POOR_DATA_URL = "https://www.wikidata.org/wiki/Q122733648"

ARTHUR_SCHNITZLER = WikiDataPerson(ARTHUR_SCHNITZLER_URL)
POOR_DATA_ITEM = WikiDataPerson(POOR_DATA_URL)


class TestTestTest(unittest.TestCase):
    """Tests for `acdh-wikidata-pyutils` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_testsetup(self):
        self.assertTrue(True)

    def test_002_valid_url(self):
        item = ARTHUR_SCHNITZLER
        self.assertEqual(item.wikidata_id, ARTHUR_SCHNITZLER_ID)

    def test_003_non_valid_url(self):
        with self.assertRaises(NoWikiDataUrlException):
            WikiDataPerson(ARTHUR_SCHNITZLER_URL.replace("wikidata", "hansi"))

    def test_004_label(self):
        item = ARTHUR_SCHNITZLER
        self.assertEqual(item.label, "Arthur Schnitzler")

    def test_005_poor_data(self):
        item = POOR_DATA_ITEM
        apis_person = item.get_apis_person()
        self.assertFalse(apis_person["first_name"])

    def test_006_no_name(self):
        item = POOR_DATA_ITEM
        apis_person = item.get_apis_person()
        self.assertEqual(apis_person["name"], "Peter Andorfer")
