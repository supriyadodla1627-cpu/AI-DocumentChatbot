import os

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


def ask_question(vectorstore, query):
    # Retrieve relevant documents
    docs = vectorstore.similarity_search(query, k=5)

    context = "\n\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Answer ONLY from the context below.
If the answer is not present, reply:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}
"""
    )

    messages = prompt.format_messages(
        context=context,
        question=query
    )

    response = llm.invoke(messages)

    return response.content