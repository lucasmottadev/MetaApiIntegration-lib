from base.adobjects.father.account_object import Account, ChildMixin, Child


class Adcreatives(ChildMixin):
    def __init__(self):
        self.me = Child(name='adcreatives', route_name='adcreatives')
        ChildMixin.__init__(self, self.me)

    def search_adcreatives(self, adcreative_id, route):
        params = {
            'limit': 99999,
            'time_increment': 1,
            'fields': 'id, name'
        }
        url = f'{self.base_url}{adcreative_id}/{route}'
        return self.basic_search(params=params, url=url)
