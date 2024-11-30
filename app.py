import streamlit as st
from streamlit import session_state as sst
from streamlit_chat import message
from openai import OpenAI

client = OpenAI(
    api_key= st.secrets['OPENAI_API_KEY']
)

def initialize_chat_history():
  """
  Initialize chat history with a welcome message from Perso9🦊.
  """
  sst["chat_history"] = [
    {
      'role': 'assistant',
      'content': "Hi! I'm Perso9🦊. Ask me anything you want to know. You can even configure me from the sidebar!"
    }
  ]

def show_chat(messages: list):
  """
  Display chat messages stored in session state.

  Args:
      messages (list): List of messages in the chat history.
  """
  for i, msg in enumerate(messages):
    message(
      message=msg['content'], 
      is_user=msg['role'] == 'user', 
      key=str(i)
    )

def add_to_chat(role, content):
  """
  Add a message to the chat history and display it.

  Args:
      role (str): 'user' or 'assistant' to indicate message origin.
      content (str): Text content of the message.
  """
  sst.chat_history.append(
    {
      "role": role, 
      "content": content
    }
  )
  
  message(
    message=content, 
    is_user=(role == 'user')
  )

# Function to generate AI response
def generate_response(ai_definition:str, chat_history:list):
  """Generate response with chat history and provided AI definition

  Args:
      ai_definition (str): How the AI should behave as
      chat_history (list): Chat History list

  Returns:
      str: AI response
  """
  messages = [{"role": "system", "content": ai_definition}] + chat_history
  response = client.chat.completions.create(
          messages=messages,
          model="gpt-4o"
      )
  return response.choices[0].message.content

def main():
  # Streamlit App
  st.set_page_config(
    page_title="Perso9", 
    page_icon='🦊', 
    layout="wide", 
    initial_sidebar_state='expanded'
  )
  st.title("Perso9 🦊")

  # Form for AI customization
  with st.sidebar:
    with st.form("ai_customization_form"):
      ai_personality = st.text_input("AI Personality", "Friendly and helpful assistant")
      ai_role = st.text_input("AI Role", "General assistant")
      ai_tone = st.selectbox("Tone of Voice", ["Formal", "Casual", "Inspirational", "Technical"], index=1)
      ai_scope = st.text_input("Knowledge Scope", "General knowledge across various topics")
      ai_language = st.selectbox("Preferred Language", ["English", "Spanish", "French", "Other"], index=0)
      custom_instructions = st.text_area("Custom Instructions (Optional)")
      submitted_form = st.form_submit_button("Create AI")

  # Combine fields into a system prompt
  if submitted_form:
    ai_definition = f"""
    Personality: {ai_personality}.
    Role: {ai_role}.
    Tone of voice: {ai_tone}.
    Knowledge scope: {ai_scope}.
    Preferred language: {ai_language}.
    Custom instructions: {custom_instructions}.
    """
    sst.ai_definition = ai_definition
    st.success("AI created successfully! Start chatting below.")

  # Default AI definition if the form isn't submitted
  if "ai_definition" not in sst:
    sst.ai_definition = "You are a friendly and helpful assistant."

  # Chat interface
  if "chat_history" not in sst:
    initialize_chat_history()
  show_chat(sst.chat_history)

  prompt = st.chat_input("Your Message:")

  if prompt:
    add_to_chat(role= "user", content= prompt)
    ai_response = generate_response(sst.ai_definition, sst.chat_history)
    add_to_chat(role= "assistant", content= ai_response)


if __name__ == '__main__':
  main()