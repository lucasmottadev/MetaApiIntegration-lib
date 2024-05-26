from abc import ABC, abstractmethod

import requests
from pathlib import Path


class GraphBase(ABC):
    def __init__(self, act_id: str = None):
        self.access_token = self.search_access_token
        self.routes = [
            "campaigns",
            "adsets",
            "adcreatives",
        ]
        self.versions = [
            "v13.0",
            "v14.0",
            "v15.0",
            "v16.0",
            "v17.0",
            "v18.0",
            "v19.0",
        ]
        self.HOST = "https://graph.facebook.com/"
        self.base_url = f'{self.HOST}{self.versions[-1]}/'
        self.account_id = act_id
        self.limited_resources_mode = False

    @property
    def search_access_token(self) -> str:
        __path__ = Path(__file__)
        while __path__.name != 'IntegrationMeta':
            __path__ = __path__.parent
        return open(f'{__path__}/base/keys/access_token.txt').read().strip()

    @abstractmethod
    def basic_search(self):
        raise NotImplementedError

    def _append_token(self, params: dict = None):
        if params is None:
            params = {'access_token': self.access_token}
        elif params.get('access_token') is None:
            params['access_token'] = self.access_token
        return params


class GraphBaseMixin(GraphBase):
    def __init__(self):
        super().__init__()

    def basic_search(self,
                     params: dict = None,
                     url: str = None,
                     process_return: bool = False,
                     type_process_return: str = None
                     ):
        if url is None:
            url = f'{self.base_url}{self.account_id}/'

        if params is None:
            params = {'metadata': 1}

        response = requests.get(url=url, params=self._append_token(params))

        if response.status_code == 200:
            response_data = response.json().get('data')

            if response_data is None:
                response_data = response.json()

            if response_data and len(response_data) >= 1:
                if process_return:
                    if type_process_return is not None:
                        return [response_item[f'{type_process_return}'] for response_item in response_data]
                    return [response_item['id'] for response_item in response_data]

                return response_data
        else:
            print(f'Error in process {url}')
