import os
from langchain_openai import ChatOpenAI
import streamlit as st

from langchain.globals import set_debug  # debug what is langchaing doing

#Import ChatOpenAI class from langchain_openai to work
# with the OpenAi chat model

set_debug("true")  # enable langchain debug

#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
llm = ChatOpenAI(model="gpt-4o",api_key=OPENAI_API_KEY)

#  Give page a title
st.title("Ask me Anything :-)")

#  Text box widget to enter the question
question = st.text_input("Ask a question: ")

#  send question to the llm
response = llm.invoke(question)

#  show rsponse in browser (localhost:8502)
if question:
     st.write(response.content)

