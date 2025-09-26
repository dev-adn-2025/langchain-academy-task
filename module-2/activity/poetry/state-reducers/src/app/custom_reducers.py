from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

from operator import add
from typing import Annotated

def reduce_list(left: list | None, right: list | None) -> list:
    """Safely combine two lists, handling cases where either or both inputs might be None.

    Args:
        left (list | None): The first list to combine, or None.
        right (list | None): The second list to combine, or None.

    Returns:
        list: A new list containing all elements from both input lists.
               If an input is None, it's treated as an empty list.
    """
    if not left:
        left = []
    if not right:
        right = []
    return left + right

class DefaultState(TypedDict):
    foo: Annotated[list[int], add]

class CustomReducerState(TypedDict):
    foo: Annotated[list[int], reduce_list]

def node_1(state):
    print("---Node 1---")
    return {"foo": [2]}

# # Build graph
# builder = StateGraph(DefaultState)
# builder.add_node("node_1", node_1)

# # Logic
# builder.add_edge(START, "node_1")
# builder.add_edge("node_1", END)

# # Add
# graph = builder.compile()

# try:
#     print(graph.invoke({"foo" : None}))
# except TypeError as e:
#     print(f"TypeError occurred: {e}")

# Build graph
builder = StateGraph(CustomReducerState)
builder.add_node("node_1", node_1)

# Logic
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

# Add
graph = builder.compile()

try:
    print(graph.invoke({"foo" : None}))
except TypeError as e:
    print(f"TypeError occurred: {e}")