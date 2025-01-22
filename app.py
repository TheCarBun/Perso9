import streamlit as st
from streamlit import session_state as sst
from streamlit_chat import message
from openai import OpenAI
import json, os

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

def load_presets(file_path="presets.json"):
  """
  Load presets from a JSON file.
  
  Args:
    file_path (str): Path to the JSON file containing presets.

  Returns:
    dict: Dictionary of presets.
  """
  if not os.path.exists(file_path):
    print("❗Error: Preset file not found.")
    return {}
  try:
    with open(file_path, "r") as file:
      return json.load(file)
  except Exception as e:
    print(f"❗Error loading presets: {e}")
    return {}

def load_css() -> str:
    """
    Loads CSS stylesheet from local files.

    Returns:
    - str: The content of the CSS file.
    """
    try:
        with open('static/styles.css') as f:
            custom_css = f.read()
        return custom_css
    except FileNotFoundError:
        print("❗Error loading stylesheet: File not found.")
    except Exception as e:
        print(f"❗Error loading stylesheet: {e}")

def main():
  # Streamlit App
  st.set_page_config(
    page_title="Perso9", 
    page_icon='🦊', 
    layout="wide", 
    initial_sidebar_state='expanded'
  )
  st.title("Perso9 🦊")

  # Custom CSS
  st.markdown(f'<style>{load_css()}</style>', unsafe_allow_html=True)

  # Load presets
  presets = load_presets()

  # Form for AI customization
  with st.sidebar:
    st.markdown("# 🦊 Create Your AI Character")
    with st.container(border=True):
      st.write("🎨 Personalize your AI by filling in a few details or choose a preset!")

      # Character Presets
      preset_choice = st.radio(
            "Choose a Character Preset:",
            list(presets.keys()) + ["Custom"],
            index=0
        )

    if preset_choice == "Custom":
      with st.form("ai_customization_form"):
        st.write("✨ Customize your AI below:")
        character_name = st.text_input("Character Name", "Perso9")
        personality_description = st.text_area("Describe the Personality", "Friendly and helpful.")
        favorite_topics = st.text_input("Topics of Interest", "Technology, Science, Art")
        communication_style = st.selectbox(
            "Communication Style", 
            ["Casual", "Formal", "Motivational", "Technical"], 
            index=0
        )
        preferred_language = st.selectbox("Preferred Language", ["English", "Spanish", "French"], index=0)
        submitted_form = st.form_submit_button("Create AI")
    else:
      # Use the selected preset
      preset_data = presets[preset_choice]
      character_name = preset_choice
      personality_description = preset_data["personality_description"]
      favorite_topics = preset_data["favorite_topics"]
      communication_style = preset_data["communication_style"]
      preferred_language = preset_data["preferred_language"]
      submitted_form = True
    
    if "chat_history" in sst:
      if st.button("Clear Chat History", type='primary', use_container_width=True):
        initialize_chat_history()
        st.toast("🧹 Chat cleared successfully")

  if submitted_form:
    # Generate the AI definition based on inputs
    sst.ai_definition = f"""
    Name: {character_name}.
    Personality: {personality_description}.
    Topics: {favorite_topics}.
    Communication Style: {communication_style}.
    Language: {preferred_language}.
    """
    st.toast(f"✅ {character_name} created successfully! Start chatting below.")

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