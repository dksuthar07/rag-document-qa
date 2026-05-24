import tempfile
import streamlit as st

from src.loader import load_document
from src.splitter import split_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_vectorstore
from src.retrieval import get_retriever
from src.qa_chain import build_qa_chain
import time

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="RAG Document QA",
    layout="wide"
)

st.title(
    "📄 RAG-Powered Document Q&A System"
)


# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title(
    "Settings"
)

top_k = st.sidebar.slider(
    "Retrieved Chunks",
    min_value=1,
    max_value=20,
    value=8
)


# -------------------------
# SESSION STATE
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_count" not in st.session_state:
    st.session_state.uploaded_count = 0


# -------------------------
# FILE UPLOAD
# -------------------------

uploaded_files = st.file_uploader(
    "Upload PDF / DOCX files",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


# -------------------------
# RESET CHAT ON NEW UPLOADS
# -------------------------

current_count = len(uploaded_files) if uploaded_files else 0

if current_count != st.session_state.uploaded_count:

    st.session_state.messages = []

    st.session_state.uploaded_count = current_count

#time
start = time.time()


# -------------------------
# PROCESS DOCUMENTS
# -------------------------

if uploaded_files:

    all_docs = []

    with st.spinner(
        "Processing documents..."
    ):

        for uploaded_file in uploaded_files:

            suffix = "." + uploaded_file.name.split(".")[-1]

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as tmp:

                tmp.write(
                    uploaded_file.read()
                )

                filepath = tmp.name

            docs = load_document(
                filepath
            )

            # ADD SOURCE METADATA

            for doc in docs:

                doc.metadata["source"] = (
                    uploaded_file.name
                )

            all_docs.extend(
                docs
            )

        # CHUNKING

        chunks = split_documents(
            all_docs
        )

        # EMBEDDINGS

        embeddings = get_embeddings()

        # VECTOR STORE

        vector_db = create_vectorstore(
            chunks,
            embeddings
        )

        # RETRIEVER

        retriever = get_retriever(
            vector_db,
            top_k
        )

        # QA CHAIN

        qa_chain = build_qa_chain(
            retriever
        )

    st.success(
        f"{len(uploaded_files)} document(s) loaded successfully."
    )

    # -------------------------
    # CHAT HISTORY
    # -------------------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

    # -------------------------
    # CHAT INPUT
    # -------------------------

    question = st.chat_input(
        "Ask a question about your documents..."
    )

    if question:

        # USER MESSAGE

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message(
            "user"
        ):

            st.markdown(
                question
            )

        # ASSISTANT RESPONSE

        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Generating answer..."
            ):

                response = qa_chain.invoke(
                    {
                        "input": question
                    }
                )

                answer = response["answer"]

                st.markdown(
                    answer
                )

                # SOURCE CITATIONS

                with st.expander(
                    "Retrieved Sources"
                ):

                    for i, doc in enumerate(
                        response["context"],
                        start=1
                    ):

                        source = doc.metadata.get(
                            "source",
                            "Unknown File"
                        )

                        st.markdown(
                            f"### Source {i}"
                        )

                        st.markdown(
                            f"**File:** {source}"
                        )

                        st.info(
                            doc.page_content[:700]
                        )

        # SAVE CHAT

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

end = time.time()
st.write(
    f"Response Time: {end-start:.2f} sec"
)