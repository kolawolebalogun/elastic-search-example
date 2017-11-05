import json
import os

from elasticsearch import Elasticsearch, helpers

# Setting ElasticSearch global Param
es_index_name = "insydo-index"
es_doc_type = "insydo-doc"
con_es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'timeout': 180}], verify_certs=True)


def mapping_config():
    """
    ElasticSearch mapping config
    :return string
    """
    mapping = '''{
        "mappings": {
            "''' + es_doc_type + '''": {
                "properties": {
                    "business": {
                        "type": "nested"
                    },
                    "keyword": {
                        "type": "nested"
                    }
                }
            }
        }
    }'''
    return mapping


def load_json():
    """
    Reads all data from specified directory
    To avoid loading all in memory, I make use of generator
    """
    directory = os.path.dirname(os.path.realpath(__file__)) + "/data"
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as open_file:
                yield json.load(open_file)


def es_connection(connection, index_name, mapping):
    """
    Reset ElasticSearch Index
    :type connection elasticsearch.Elasticsearch
    :param connection: ElasticSearch Client.
    :type index_name str
    :param index_name: ElasticSearch Index name.
    :type mapping str
    :param index_name: ElasticSearch mapping config.
    :return None
    """
    connection.indices.delete(index=index_name, ignore=[400, 404])
    connection.indices.create(index=index_name, body=mapping)


def run():
    """
    Initialized ElasticSearch index and index data file
    :return None
    """
    print("Initializing elastic search data")
    mapping = mapping_config()
    es_connection(con_es, es_index_name, mapping)

    helpers.bulk(con_es, load_json(), index=es_index_name, doc_type=es_doc_type)


def search(keyword):
    """
    Query ElasticSearch index
    :type keyword str
    :param keyword: Keyword to search.
    :return dict
    """
    query = {
        "_source": False,
        "query": {
            "bool": {
                "should": [
                    {
                        "nested": {
                            "path": "business",
                            "query": {
                                "match": {"business.name": "{}".format(keyword)}
                            },
                            "inner_hits": {}
                        }
                    },
                    {
                        "nested": {
                            "path": "keyword",
                            "query": {
                                "match": {"keyword.name": "{}".format(keyword)}
                            },
                            "inner_hits": {}
                        }
                    }
                ]
            }
        }
    }
    res = con_es.search(index=es_index_name, doc_type=es_doc_type, body=query)

    return res
