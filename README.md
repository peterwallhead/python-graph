[![Build Status](https://travis-ci.com/peterwallhead/python-graph.svg?branch=master)](https://travis-ci.com/peterwallhead/python-graph)


## Running tests

### Install pytest with pipenv
```pipenv --python /path/to/your/python/installation/python3 install --dev```

### Run tests
```pipenv run pytest```

## Usage

### Import Graph
```from core.graph import Graph```

### Create a new graph
```graph = Graph()```

### Add a node to the graph
Returns True.

```node = graph.addNode("test")```

### Search nodes
Returns True if node exists, or False if it doesn't.

```found_node = graph.findNode("test")```

### Return an existing node and its edges
```node = graph.getNode("test")```

### Delete an existing node
Returns True.

```deleted_node = graph.removeNode("test")```

### Add an edge between two nodes
*Nodes must exist before edge can be added.*

```edge = graph.addEdge("start", "end")```

### Search edges using the start and end nodes
Returns True if edge exists, or False if it doesn't.

```output = graph.findEdge("start", "end")```

### Delete an existing edge
Returns True.

```deleted_edge = graph.removeEdge("start", "end")```