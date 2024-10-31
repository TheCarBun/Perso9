import os, shutil
import tempfile
import streamlit as st
from streamlit import session_state as sst
from streamlit_chat import message
from embedchain import App

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def initialize_app(db_path):
  """Initialize Embedchain App with LLM, Vector Database and Embedder"""

  return App.from_config(
    config={
      "llm": {
        "provider": "openai", 
        "config": {"api_key": OPENAI_API_KEY}
      },

      "vectordb": {
        "provider": "chroma", 
        "config": {"dir": db_path}
      },

      "embedder": {
        "provider": "openai", 
        "config": {"api_key": OPENAI_API_KEY}
      },
    }
  )

def initialize_chat_history():
    sst.chat_history = [
      {
        'role': 'ai',
        'content': "Hello I'm Perso9! Upload a PDF and ask me anything about it."
      }
    ]

def show_chat(messages:list):
  for i, msg in enumerate(messages):
    message(message=msg['content'], is_user=msg['role'] == 'user', key=str(i))

def reinitialize_app(dbpath:str):
  initialize_chat_history()
  shutil.rmtree(dbpath)
  sst.db_path = tempfile.mkdtemp()

def main():
  st.set_page_config(
    page_icon='🦊',
    page_title='Perso9',
    initial_sidebar_state='expanded'
  )
  st.title("🦊 Perso9")

  if 'db_path' not in sst:
    sst.db_path = tempfile.mkdtemp() # Create temporary directory for chromadb

  app = initialize_app(sst.db_path) # Initialize embedchain app

  # ---- Sidebar Content ----

  # Upload PDF and add to VectorDB
  with st.sidebar:
    pdf_file = st.file_uploader(
    "Upload a PDF file", 
    type="pdf", 
    label_visibility='hidden'
    )

    if pdf_file:
      with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        f.write(pdf_file.getvalue())
        app.add(f.name, data_type="pdf_file")
      os.remove(f.name)
      st.toast(f"Added {pdf_file.name} to knowledge base!")
    
    if st.button('Clear Vector DB'):
      reinitialize_app(sst.db_path)
    
    if st.button('Clear Chat_History'):
      initialize_chat_history()
  
  if 'chat_history' not in sst:
    initialize_chat_history()

  show_chat(sst.chat_history)

  prompt = st.chat_input("Ask a question about the PDF")

  if prompt:

    message(prompt, is_user=True)

    sst.chat_history.append(
      {
        'role': 'user',
        'content': prompt
      }
      )

    with st.spinner("Thinking..."):
      answer = app.chat(prompt)

      message(answer)
    
      sst.chat_history.append(
        {
          'role': 'ai',
          'content': answer
        }
      )

if __name__ == '__main__':
    main()