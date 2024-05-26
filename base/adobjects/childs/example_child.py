from base.adobjects.father.account_object import ChildMixin, Child


class ExampleChild(ChildMixin):
    """
        Creating mixin of the object child, the mixin object is sufficient
        to create if 'limited_resources_mode parameter' is False, for default is False:

            - create father
            - search ids
            - build routes

        OBS: The creation of father, search your bind ids, generates a direct impact on the
        consumption of more processing memory and API calls, so if you are using a server
        hosted in the cloud, it is worth considering.
    """
    def __init__(self):
        # Creating child object to specify the value of route and name child object
        self.me = Child(name='adcreatives', route_name='adcreatives')
        ChildMixin.__init__(self, self.me)

    def search_adcreatives(self, example_child_id: str, route: str):
        """

        Creation suggestion if 'limited_resources_mode parameter' is True

        :param example_child_id: child_id of your object
        :param route: route
        :return: depends on your route
        """
        params = {
            'limit': 99999,
            'time_increment': 1,
            'fields': 'id, name'
        }
        url = f'{self.base_url}{example_child_id}/{route}'
        return self.basic_search(params=params, url=url)
