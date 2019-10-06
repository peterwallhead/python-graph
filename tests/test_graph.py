import pytest

from core.graph import Graph



def test_can_create_graph():
    graph = Graph()
    output = graph.showGraph()
    assert output == {}

def test_can_add_node():
    graph = Graph()
    output = graph.addNode("test")
    assert output == True

def test_can_find_node():
    graph = Graph()
    graph.addNode("test")
    output = graph.findNode("test")
    assert output == True

def test_can_get_node():
    graph = Graph()
    graph.addNode("test")
    output = graph.getNode("test")
    assert output == {'edges':{}}

def test_can_remove_node():
    graph = Graph()
    graph.addNode("test")
    output = graph.removeNode("test")
    assert output == True

def test_can_add_edge():
    graph = Graph()
    graph.addNode("start")
    graph.addNode("end")
    output = graph.addEdge("start", "end")
    assert output == True

def test_can_find_edge():
    graph = Graph()
    graph.addNode("start")
    graph.addNode("end")
    graph.addEdge("start", "end")
    output = graph.findEdge("start", "end")
    assert output == True

def test_can_remove_edge():
    graph = Graph()
    graph.addNode("start")
    graph.addNode("end")
    graph.addEdge("start", "end")
    output = graph.removeEdge("start", "end")
    assert output == True
