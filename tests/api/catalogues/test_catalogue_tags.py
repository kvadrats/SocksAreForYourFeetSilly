from tests.api.catalogues.common import CataloguesTestCase


class TestCatalogueTag(CataloguesTestCase):
    def test_catalogue_tag(self):
        payload = self.requests.CATALOGUE_GET_TAGS
        payload["tags"]
        result = self.json.send_request(payload)
        print(result)
