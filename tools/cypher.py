import streamlit as st

# tag::import[]
from langchain.chains import GraphCypherQAChain

from llm import llm
from graph import graph
# end::import[]


# tag::cypher-qa[]
cypher_qa = GraphCypherQAChain.from_llm(
    llm,          # <1>
    graph=graph,  # <2>
)
# end::cypher-qa[]

# tag::generate-response[]
def generate_response(prompt):
    """
    Use the Neo4j recommendations dataset to provide
    context to the LLM when answering a question
    """

    # Handle the response
    response = cypher_qa.run(prompt)

    return response
# end::generate-response[]