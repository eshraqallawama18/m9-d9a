"""Five SPARQL queries against fixtures/mini_kg.ttl.

Each function returns a SPARQL query string. The autograder parses the
fixture into an `rdflib.Graph` and runs your query against it.
"""


from rdflib  import Graph

def q1():
    """Q1 — Return all (book, title) pairs.

    Result: 5 rows. Variables in the SELECT: ?book ?title (in that order).
    """
    
    return """
    SELECT ?book ?title
    WHERE {
        ?book rdfs:label ?title .
    }
"""


def q2():
    """Q2 — Return all books and their year, filtered to books published
    after 2010.

    Result: 1 row. Variables in the SELECT: ?book ?year.
    Use FILTER (?year > 2010) — strict, not >=.
    """
    return ""


def q3():
    """Q3 — Return all (book, author_name) pairs. author_name is the
    rdfs:label of the author resource.

    Result: 7 rows. Books with multiple authors produce one row per
    author. Variables in the SELECT: ?book ?author_name.
    """
    return ""


def q4():
    """Q4 — Return all books and their topic, with the topic OPTIONAL.

    Result: 5 rows (every book appears; ?topic unbound for books with no
    :topic triple). Variables in the SELECT: ?book ?topic.
    """
    return ""


def q5():
    """Q5 — Return TRUE if any book has more than one :author triple;
    otherwise FALSE.

    Result: TRUE on this fixture. Use ASK with FILTER (?a1 != ?a2) over
    two distinct author bindings.
    """
    return ""



if __name__ == "__main__":
    g = Graph()
    g.parse("fixtures/mini_kg.ttl", format="ttl")
    results = g.query(q1())
    for row in results:
        print(row)  
        
        
    