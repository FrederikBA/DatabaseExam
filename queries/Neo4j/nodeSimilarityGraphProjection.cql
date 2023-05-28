// Graph projection. Used for node similarity algorithm to recommend movies based on the movies you rent.

 # First query
    graph.run("""
        CALL gds.graph.project(
            'NodeSimilarity',
            ['Movie', 'Actor'],
            {
                FEATURES: {
                }
            }
        );
    """)
    sleep(20)

    # Second query
    graph.run("""
        CALL gds.nodeSimilarity.write.estimate('NodeSimilarity', {
            writeRelationshipType: 'SIMILAR',
            writeProperty: 'Score'
        })
        YIELD nodeCount, relationshipCount, bytesMin, bytesMax, requiredMemory
    """)
    sleep(20)

    # Third query
    graph.run("""
        CALL gds.nodeSimilarity.stream('NodeSimilarity', { topK: 10 })
        YIELD node1, node2, similarity
        RETURN gds.util.asNode(node1).Title AS Movie1, gds.util.asNode(node2).Title AS Movie2, similarity
        ORDER BY similarity DESCENDING, Movie1, Movie2
    """)
    sleep(30)

    # Fourth query
    graph.run("""
        CALL gds.nodeSimilarity.stats('NodeSimilarity')
        YIELD nodesCompared, similarityPairs
    """)
    sleep(10)

    # Fifth query
    graph.run("""
        CALL gds.nodeSimilarity.mutate('NodeSimilarity', {
            mutateRelationshipType: 'SIMILAR',
            mutateProperty: 'Score'
        })
        YIELD nodesCompared, relationshipsWritten
    """)
    sleep(20)

    # Sixth query
    graph.run("""
        CALL gds.nodeSimilarity.write('NodeSimilarity', {
            writeRelationshipType: 'SIMILAR',
            writeProperty: 'Score'
        })
        YIELD nodesCompared, relationshipsWritten
    """)