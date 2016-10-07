from elasticsearch import Elasticsearch
import json

class Indexer(object):
    def __init__(self, index_name, doc_type):

        # Load configuration from file
        with open("../config.json", "r") as fig:
            config = json.load(fig)

        host = config['host']
        port = int(config['port'])

        # create an Elasticsearch index
        es = Elasticsearch([{'host': host, 'port': port}])

        self.index_name = index_name
        self.es = es
        self.doc_type = doc_type

    def index(self, doc_id=None, doc_body=None):
        self.es.index(
            index=self.index_name,
            doc_type=self.doc_type,
            id=doc_id,
            body=doc_body)
