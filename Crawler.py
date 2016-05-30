from SPARQLWrapper import SPARQLWrapper, JSON
from Indexer import Indexer

class Crawler(object):

    __resourcesQueue = set()

    def __init__(self, seed_URL):
        self.seed_URL = seed_URL
        self.indexer = Indexer("people", "person")
        self.__walk()

    def __walk(self):
        #Extract the resources from the seed URL
        self.__resourcesQueue |= self.__extractResources(self.seed_URL)

        #Extract the people from the seed URL
        self.__extractPeople(self.seed_URL)


        while ((len(self.__resourcesQueue) != 0)):
            resource_url = self.__resourcesQueue.pop()

            # Find the linked resources from this resource
            self.__resourcesQueue |= self.__extractResources(resource_url)

            self.__extractPeople(resource_url)


    def __extractResources(self, resource_url):
        print "Looking for resources in %s" % resource_url

        resources_query = """
        PREFIX foaf:<http://xmlns.com/foaf/0.1/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT ?resource
        WHERE {
            <%s> ?p ?resource
        }""" % resource_url

        resources = set(self.__run_query(resources_query, 'Resources'))

        print "Found %s resources" % len(resources)

        return resources


    def __extractPeople(self, resource_url):
        print "Looking for people in %s" %resource_url
        people_query = """
        PREFIX foaf:<http://xmlns.com/foaf/0.1/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?person, ?label, ?mentioned_by
        WHERE {
            <%s> ?p ?person .
            ?person rdf:type foaf:Person .
            ?person rdfs:label ?label .
            ?mentioned_by ?pred ?person
        }""" % resource_url

        people = self.__run_query(people_query, 'People', resource_url)

        print "Found %s people" % len(people)


        # Index the returned people object
        if (len(people) != 0):
            for person in people:
                # Remove duplicate entries in the mentioned_by field
                people[person]['mentioned_by'] = list(people[person]['mentioned_by'])
                self.indexer.index(person, people[person])

            print "Done indexing batch"

    def __run_query(self, query, type, resource_url=None):

        query_result_list = []
        people_json = {}
        people_found =  set()

        try:
            # Set the SPARQL endpoint to run queries against
            sparql = SPARQLWrapper("http://dbpedia.org/sparql")
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)

            results = sparql.query().convert()

            if (type == 'Resources'):

                for result in results['results']['bindings']:
                    # Only follow resources that are URIs
                    if (result['resource']['type'] == 'uri'):
                        query_result_list.append(result['resource']['value'])

                return query_result_list


            if (type == 'People'):

                for result in results['results']['bindings']:

                    people_found.add(result['person']['value'])

                # For each distinct person found, create an object for them
                for person in people_found:
                    people_json[person] = {
                        'uri': person,
                        'mentioned_by': set()
                    }

                for result in results['results']['bindings']:
                    # For each result, get the label and append to the mentioned_by array
                    person_uri = result['person']['value']
                    person_label = result['label']['value']
                    label_lang = result['label']['xml:lang']
                    person_mentioned_by = result['mentioned_by']['value']

                    if (label_lang == 'en'):
                        people_json[person_uri]['label'] = person_label
                    people_json[person_uri]['mentioned_by'].add(person_mentioned_by)

                return people_json

        except Exception:
            if (type == 'Resources'):
                return query_result_list
            elif (type == 'People'):
                return people_json