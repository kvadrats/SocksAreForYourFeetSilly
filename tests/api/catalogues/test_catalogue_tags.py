from tests.api.catalogues.common import CataloguesTestCase


class TestCatalogueTag(CataloguesTestCase):
    def test_catalogue_tag(self):
        result = self.json.send_get_request()
        assert(result == {'tags': ['brown', 'geek', 'formal', 'blue', 'skin', 'red', 'action', 'sport', 'black', 'magic', 'green'], 'err': None})
