from flask import Flask, render_template, request
from elasticsearch import Elasticsearch

# create our little application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/search', methods=['POST'])
def search():

    query_string = request.form['query']

    if 'http://' in query_string:
        results = run_elasticsearch_query('uri', query_string)

        # Return the highest scoring document
        results = [results[0]]
    else:
        results = run_elasticsearch_query('label', query_string)

    return render_template('search_results.html', results=results)


@app.route('/result')
def get_result():

    uri = request.args.get('uri')

    results = run_elasticsearch_query('uri', uri)

    return render_template('resource_details.html', results=results)


def run_elasticsearch_query(field, query_keywords):
    es = Elasticsearch()

    # Build the search query
    query = {
        "query": {
            "match": {
                field: query_keywords
            }
        }
    }

    # Get the documents that match the search query
    res = es.search(index="people", doc_type="person", body=query)

    return res['hits']['hits']


if __name__ == '__main__':
    app.run(debug=True)
