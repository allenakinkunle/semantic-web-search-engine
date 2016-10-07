from elasticsearch import Elasticsearch

class Indexer(object):
    def __init__(self, index_name, doc_type):
        # create an Elasticsearch index
        es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

        self.index_name = index_name
        self.es = es
        self.doc_type = doc_type

    def index(self, doc_id=None, doc_body=None):
        self.es.index(
            index=self.index_name,
            doc_type=self.doc_type,
            id=doc_id,
            body=doc_body)



