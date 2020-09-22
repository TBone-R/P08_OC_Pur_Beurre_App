from requests import get as re_get


class Request:
    """ Handle request to API Open Food Fact"""

    @staticmethod
    def db_sample_request():
        """Retrieve data of many products using a Search Requests"""

        url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        params = {"action": "process",
                  "tagtype_0": "purchase_places",
                  "tag_contains_0": "contains",
                  "tag_0": "france",
                  "sort_by": "unique_scans_n",
                  "page_size": 1000,
                  "json": 1}

        res = re_get(url, params=params)

        if res.status_code != 200:
            raise ConnectionError()

        return res.json()
