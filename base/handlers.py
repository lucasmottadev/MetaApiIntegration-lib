class Handler:

    @staticmethod
    def create_fields(url: str, fields):
        if url.__contains__('?fields='):
            url += fields
        elif url.endswith('&'):
            url += fields
        else:
            url += '?fields=' + fields
        return url

    @staticmethod
    def create_response(fields: str):
        if fields.__contains__('{'):
            layout = ""
            count = 0
            layouts = []
            uni_layout = ""
            for field in fields.split('{'):
                if field.__contains__('}'):
                    field = field.replace('}', '')
                if count == 0:
                    uni_layout = f'.get("{field}").get("data")'
                    layout += uni_layout
                    layouts.append(uni_layout)
                    continue
                uni_layout = f".get('{field}').get('data')"
                layout += uni_layout
                layouts.append(uni_layout)
                count += 1

            return layout, layouts

