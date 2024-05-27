from base.base import GraphBaseMixin
from base.adobjects.father.account_object import Account, Child, ChildMixin


class Adsets(ChildMixin):
    def __init__(self):
        self.me = Child(name='adsets', route_name='adset')
        ChildMixin.__init__(self, self.me)

    def search_adsets(self, adset_id, route):
        params = {
            'limit': 99999,
            'time_increment': 1,
            'fields': 'id, name'
        }
        url = f'{self.base_url}{adset_id}/{route}'
        return self.basic_search(params=params, url=url)
