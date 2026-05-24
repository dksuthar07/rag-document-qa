from langchain_community.vectorstores import FAISS


def create_vectorstore(
    chunks,
    embeddings
):

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vector_db