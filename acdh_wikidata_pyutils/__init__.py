from AcdhArcheAssets.uri_norm_rules import get_norm_id, get_normalized_uri
from wikidata.client import Client


class NoWikiDataUrlException(Exception):
    pass


class WikiDataPerson:
    """Class to fetch and return often used data from WikiData Person entries"""

    def __init__(self, wikidata_url):
        if "wikidata" not in wikidata_url:
            raise NoWikiDataUrlException(f"{wikidata_url} is no proper Wikidata URL")
        else:
            self.wikidata_url = get_normalized_uri(wikidata_url)
        self.wikidata_id = get_norm_id(self.wikidata_url)
        self.client = Client()
        self.entity = self.client.get(self.wikidata_id, load=True)
        self.label = f"{self.entity.label}"
