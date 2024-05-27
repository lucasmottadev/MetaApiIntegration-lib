from base.adobjects.father.account_object import Account, ChildMixin, Child


class Campaign(ChildMixin):
    def __init__(self):
        self.me = Child(name='campaigns', route_name='campaigns')
        super().__init__(self.me)

    def search_campaigns(self, campaign_id, route):
        params = {
            'limit': 99999,
            'time_increment': 1,
            'fields': 'id, name'
        }
        url = f'{self.base_url}{campaign_id}/{route}'
        return self.basic_search(params=params, url=url)
