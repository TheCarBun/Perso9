# 🦊 Perso9 - Create Your Personalized AI Chat Assistant!  
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/TheCarBun/Perso9?style=for-the-badge) 
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-raw/TheCarBun/Perso9?style=for-the-badge) 
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr-raw/TheCarBun/Perso9?style=for-the-badge) 
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-closed-raw/TheCarBun/Perso9?style=for-the-badge) 
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues-pr-closed-raw/TheCarBun/Perso9?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/TheCarBun/Perso9?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/TheCarBun/Perso9?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/TheCarBun/Perso9?style=for-the-badge)
### 🦊 About
Perso9 is designed to make conversational AI more personal and fun. Whether you're building an assistant or just chatting for fun, Perso9 adapts to your needs!
Perso9 is a powerful and customizable AI chatbot built with **Streamlit** and **OpenAI**. With Perso9, users can define the personality, role, tone, and knowledge scope of their AI assistant and have meaningful conversations tailored to their preferences.


![image](https://github.com/user-attachments/assets/94c478d8-17f4-40d4-b610-271da08db46e)

<details>
  <summary>📌 Table of Contents</summary>
  
  - [Features](#-features)
  - [Installation](#-installation)
  - [How to Use](#-how-to-use)
  - [Customization Options](#-customization-options)
  - [Tech Stack](#-tech-stack)
  - [Contributing](#-contributing)
  - [License](#-license)
</details>

---

## ✨ Features
- **Dynamic AI Personality**: Customize how your AI behaves, from tone of voice to knowledge scope.  
- **Interactive Chat**: Intuitive chat interface that adapts to your custom AI definition.  
- **Predefined or Custom Configurations**: Start with a friendly assistant or create your own unique AI.  
- **Easy Deployment**: Deploy on **Streamlit Cloud** or run locally.  
- **Responsive Design**: Styled with custom CSS for a clean and modern look.  

---

## 🛠 Installation
### Prerequisites
- Python 3.8 or later  
- OpenAI API Key  

### Steps
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-repo/perso9.git
   cd perso9
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:  
   Add the API key to a `.streamlit/secrets.toml` file:
   ```toml
   [secrets]
   OPENAI_API_KEY = "your_openai_api_key"
   ```

4. Run the app:  
   ```bash
   streamlit run app.py
   ```

---

## 🎮 How to Use
1. Launch the app.  
2. Use the **sidebar** to customize your AI assistant:  
   - Define personality, tone, knowledge scope, and more.  
3. Start chatting in the input field at the bottom of the screen.  
4. Watch your AI respond dynamically based on your customization.  

---

## 🎨 Customization Options
| Field                  | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **AI Personality**     | Define the AI's personality (e.g., "Curious philosopher").                  |
| **AI Role**            | Specify the AI's role (e.g., "Technical advisor").                         |
| **Tone of Voice**      | Choose between Formal, Casual, Inspirational, or Technical.                |
| **Knowledge Scope**    | Define the topics the AI knows about (e.g., "Cryptocurrency and blockchain"). |
| **Preferred Language** | Choose the AI's language for responses.                                    |
| **Custom Instructions**| Add unique instructions for your AI to follow.                            |

---

## 🚀 Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: [OpenAI API](https://platform.openai.com/docs/)  
- **Styling**: Custom CSS  

---

## 🤝 Contributing
Contributions are welcome! Follow these steps to get started:  
1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:  
   ```bash
   git push origin feature-branch-name
   ```
5. Open a Pull Request.  

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
