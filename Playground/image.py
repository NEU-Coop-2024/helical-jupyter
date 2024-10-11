from graphviz import Source

# Define the graph in DOT format
dot_code = '''
digraph G {
    A -> B [label="Edge from A to B"];
    A -> C [label="Edge from A to C"];
    B -> C [label="Edge from B to C"];
}
'''

# Create a Source object from the DOT code
graph = Source(dot_code)

# Render the graph to a file (e.g., as a PNG)
graph.render('output_graph', format='png')
