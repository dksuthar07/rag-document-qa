from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader
)


def load_document(filepath):

    if filepath.endswith(".pdf"):
        loader = PyPDFLoader(filepath)

    elif filepath.endswith(".docx"):
        loader = Docx2txtLoader(filepath)

    else:
        raise ValueError("Unsupported file type")

    return loader.load()