# Introduction
The World Wide Web is a large collection of documents and other resources identified through Uniform Resource Locators (URL) accessed through the Internet. Humans can read the information contained in web documents, but this is difficult for machines to do. This is because of noise in natural language and the complexity of the document structure of these web documents. To make machines understand the information contained within web documents and aid them in extracting the information accordingly, explicit instructions must be added to the web documents to instruct the machine what the information denotes.

Addressing this problem of adding semantics to information within web documents, the Semantic Web movement provides technologies for publishing machine-readable data on the web. The core technology is Resource Description Framework (RDF). RDF uses Uniform Resources Identifiers (URI) to identify information and entities within documents as well as relationships between these entities <sup>[1]</sup>. These entities and the relationships between them are defined in statements comprising of a subject, predicate and an object. This subject- predicate-object statement is called a triple. A collection of RDF statements is called a RDF document. RDF can be embedded into web documents using RDFa <sup>[1][2]</sup>, such that the data can be linked, shared and reused across applications and enterprise boundaries.

There has been a rise in the number of RDF data on the web due to the availability of tools and standards like RDF and OWL (Web Ontology Language) for publishing these semantic data <sup>[1][3]</sup>. A popular example is DBpedia, which is a collection of RDF documents extracted from Wikipedia. DBpedia uses RDF to describe the entities in Wikipedia articles and their properties. The RDF data can be accessed through SPARQL queries which is a SQL-like language for querying RDF documents. In line with the vision of the Semantic Web of sharing data across applications, DBpedia is linked with external RDF datasets like GeoNames and US Census data.

Given this increase in the amount of RDF datasets on the web, it is imperative to provide a way to find and discover this data through a semantic web search engine. Following the linked data approach that all items should be identified using URI references, the search engine would crawl the Semantic Web, following resource URIs and indexing the found resources [2].

This repo contains code for a linked data person search engine that crawls the Semantic Web, finding resources of type ’Person’, indexing these found resources. It indexes these found resources on resource URIs, human-readable labels of the resources and in line with linked data approach of linking semantic data, it keeps a list of resources that are linked to the found Person resource. It also provides a web-based user interface through which human users can find these resources.

# References
<a name="references">
[1] Hogan, A., Harth, A., Umbrich, J., Kinsella, S., Polleres, A. Decker, S. 2011, ”Searching and browsing Linked Data with SWSE: The Semantic Web Search Engine”, Web Semantics: Science, Services and Agents on the World Wide Web, vol. 9, no. 4, pp. 365-401.

[2] Tummarello, G., Delbru, R. Oren, E. 2008, ”Sindice.com: Weaving the Open Linked Data” in Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 552-565.

[3] Delbru, R., Campinas, S. Tummarello, G. 2012, ”Searching web data: An entity retrieval and high-performance indexing model”, Web Semantics: Science, Services and Agents on the World Wide Web, vol. 10, pp. 33-58.
</a>
