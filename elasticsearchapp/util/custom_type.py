from elasticsearch_dsl import DocType, Nested, String, Integer


class CustomType(DocType):
    business = Nested(
        properties={
            'id': Integer(),
            'name': String(),
        }
    )
