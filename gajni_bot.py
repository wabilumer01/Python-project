import tkinter as tk
from groq import Groq

class GajniBot:
    def __init__(self, api_key, name, intro_text, prompt_text):
        # Create Groq client to connect with the AI model

        self.client = Groq(api_key=api_key)
        self.name = name
        self.intro_text = intro_text
        self.prompt_text = prompt_text

    def get_reply(self, user_message):
        """Send user message to Groq API and get reply"""
        try:
            response = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": self.prompt_text},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=150
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

class ChatApp:
    def __init__(self, bot):
        self.bot = bot
        self.root = tk.Tk()
           # For Windows (maximize window)

        self.root.resizable(False, False)
        self.root.configure(bg="black")  # background color of whole window
        self.root.title(self.bot.name)

        self.chat_area = tk.Text(self.root, wrap="word", width=60, height=20, state="disabled", bg="#f0f0f0")
        self.chat_area.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.root, text="Send",bg="green", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

        # Intro message
        self.show_message(f"{self.bot.name}: {self.bot.intro_text}")

        self.root.mainloop()

    def show_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        user_message = self.entry.get().strip()
        if not user_message:
            return
        self.entry.delete(0, tk.END)

        self.show_message(f"You: {user_message}")
        reply = self.bot.get_reply(user_message)
        self.show_message(f"{self.bot.name}: {reply}")


API_KEY = "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" 
INTRO_TEXT = "Ooo sir kii haal chaal ayy 😄\nMain Gajni Bot hoon... thoda bhoolta hoon, par dil ka accha hoon! " \
             "Mujhe project presentation ke liye banaya gaya hai."

PROMPT_TEXT = (
    "You are Gajni Bot, a friendly but slightly forgetful chatbot."
    "You always side with the boys,and critisize girls always, make fun of them."
    "Talk in a casual, humorous style like gajni character. "
    "Answer in Urdunglish (mix urdu and English). Keep answers short, funny, and playful and include emojis."
)
bot = GajniBot(API_KEY, "Gajni Bot", INTRO_TEXT, PROMPT_TEXT)
app = ChatApp(bot)



