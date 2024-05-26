from base.base import GraphBaseMixin


class Account(GraphBaseMixin):
    # Account node representation.
    def __init__(self):
        super().__init__()
        self.urls_routes = {
            self.routes[0]: f'{self.base_url}{self.account_id}/{self.routes[0]}',
            self.routes[1]: f'{self.base_url}{self.account_id}/{self.routes[1]}',
            self.routes[2]: f'{self.base_url}{self.account_id}/{self.routes[2]}',
        }

    def generic_search(self, params: dict = None, route: str = None, process_return: bool = True) -> dict:
        return self.basic_search(params=params, url=self.urls_routes.get(route), process_return=process_return)


class Child:
    # Class to represent a child of an account
    def __init__(self, name, route_name):
        self.name = name
        self.route_name = route_name


class ChildMixin(Account):
    """

    Class representing a mixin child of an account, add wrap to many operations, as:
        - create father
        - search ids
        - build routes

    More details of implementation, see 'example_child.py' in 'childs'

    """
    def __init__(self, child: Child):
        super().__init__()
        self.child = child
        if not self.limited_resources_mode:
            self.account = self.build_father()
            self.ids = self.build_ids()
            self.routes_urls = self.build_routes(self.ids)

    @staticmethod
    def build_father():
        return Account()

    def build_ids(self):
        params = {
            'limit': 99999
        }
        return self.account.generic_search(params=params, route=self.child.route_name, process_return=True)

    def build_route(self, child_id: str, route: str):
        return f'{self.base_url}{child_id}/{route}'

    def build_routes(self, child_id_list):
        routes_url = []
        for child_id in child_id_list:
            routes_url.append(self.build_route(child_id, self.child.route_name))
        return routes_url
