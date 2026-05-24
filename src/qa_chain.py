import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

from langchain_classic.chains.retrieval import (
    create_retrieval_chain
)

from src.prompt import CUSTOM_PROMPT


load_dotenv()


def build_qa_chain(retriever):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0
    )

    document_chain = create_stuff_documents_chain(
        llm,
        CUSTOM_PROMPT
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    return retrieval_chain