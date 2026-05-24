def get_retriever(vector_db, top_k=3):

    retriever = vector_db.as_retriever(
        search_kwargs={"k": top_k}
    )

    return retriever