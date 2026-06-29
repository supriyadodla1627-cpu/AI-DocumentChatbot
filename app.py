import streamlit as st
from dotenv import load_dotenv

from pdf_reader import read_pdf
from vector_store import build_vectorstore
from chatbot import ask_question

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Document Chatbot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 AI Document Chatbot")
st.write("Upload a PDF and ask questions about its content.")

# Initialize session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

# Process PDF
if uploaded_file is not None:

    if st.session_state.vectorstore is None:

        with st.spinner("Reading PDF..."):
            text = read_pdf(uploaded_file)

        with st.spinner("Creating vector database..."):
            st.session_state.vectorstore = build_vectorstore(text)

        st.success("✅ PDF processed successfully!")

# Ask Question
if st.session_state.vectorstore is not None:

    question = st.text_input("Ask a question about your PDF")

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("Searching document..."):

                answer = ask_question(
                    st.session_state.vectorstore,
                    question
                )

            st.subheader("Answer")
            st.success(answer)

        else:
            st.warning("Please enter a question.")