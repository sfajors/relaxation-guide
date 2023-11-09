import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import font as tkfont
import openai

class RelaxationGuide:
    def __init__(self, root):
        self.root = root
        root.title("Relaxation Guide")

        # Define color scheme and styles
        self.colors = {
            "background": "#F0F8FF",
            "button": "#ADD8E6",
            "button_active": "#87CEEB",
            "text": "#000000",
            "conversation_bg": "#FFFFFF"
        }
        self.title_font = tkfont.Font(size=16, weight="bold")
        self.button_font = tkfont.Font(size=12)
        self.label_font = tkfont.Font(size=14)

        # Initialize UI components
        self.initialize_ui()

    def initialize_ui(self):
        self.frames = {}

        # Main Frame
        main_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["main"] = main_frame
        main_frame.pack(pady=20, padx=20, expand=True, fill="both")

        tk.Label(main_frame, text="How are you feeling today?", bg=self.colors["background"], fg=self.colors["text"], font=self.title_font).pack(pady=10)

        self.feelings = self.initialize_feelings()

        btn_frame = tk.Frame(main_frame, bg=self.colors["background"])
        btn_frame.pack(pady=10)
        for feeling in self.feelings:
            btn = tk.Button(btn_frame, text=feeling, command=lambda f=feeling: self.show_exercises(f), width=20, height=2, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
            btn.pack(side=tk.LEFT, padx=10, pady=5)

        # Conversation Button
        conversation_btn = tk.Button(main_frame, text="Have a Conversation", command=lambda: self.show_frame("conversation"), width=25, height=2, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        conversation_btn.pack(pady=20)

        # Exercises Frame
        exercises_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["exercises"] = exercises_frame

        # Conversation Frame
        conversation_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["conversation"] = conversation_frame
        self.initialize_conversation_ui(conversation_frame)

    def initialize_feelings(self):
        return {
            "Stressed": {
                "Deep Breathing": "Take a deep breath in through your nose, hold for a few seconds, and exhale through your mouth. Repeat several times.",
                "Box Breathing": "Inhale for a count of 4, hold for 4, exhale for 4, and wait for 4. Repeat the cycle."
            },
             "Anxious": {
                "4-7-8 Breathing": "Inhale for a count of 4, hold for 7, and exhale for 8. This pattern helps to calm the nervous system.",
                "Progressive Relaxation": "Tense and then relax each muscle group, starting from your toes and working up to your head."
            },
            "Sad": {
                "Diaphragmatic Breathing": "Place one hand on your chest and the other on your stomach. Breathe deeply such that the hand on your stomach rises. Exhale and repeat.",
                "Gratitude Meditation": "Focus on things in your life you are grateful for. Visualize them and hold onto the positive feelings."
            },
            "Angry": {
                "Counted Breathing": "Inhale slowly to the count of four, then exhale to the count of four. Focus on the numbers to divert attention from anger.",
                "Compassion Meditation": "Visualize the person or situation causing anger. Send them positive energy and wishes. This helps to release negative emotions."
            },
            "Overwhelmed": {
                "Abdominal Breathing": "Place your hands on your abdomen. Take a deep breath in, letting your abdomen rise. Exhale slowly and feel it fall. Repeat.",
                "Guided Imagery": "Close your eyes and visualize a peaceful place or scenario. Engage all your senses and immerse yourself in the visualization."
            }
        }

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.pack(pady=20, padx=20, expand=True, fill="both")
        frame.tkraise()

    def show_exercises(self, feeling):
        print(f"Showing exercises for: {feeling}")  # Debugging print statement
        exercises_frame = self.frames["exercises"]
    
        # Clear previous buttons
        for widget in exercises_frame.winfo_children():
            widget.destroy()

        # Add exercise buttons
        for exercise, description in self.feelings[feeling].items():
            btn = tk.Button(exercises_frame, text=exercise, command=lambda d=description: self.show_description(d))
            btn.pack(fill=tk.X, padx=20, pady=5)

        self.show_frame("exercises")

    def initialize_conversation_ui(self, conversation_frame):
        # Chat Display
        chat_display = scrolledtext.ScrolledText(conversation_frame, wrap=tk.WORD, width=50, height=10, bg=self.colors["conversation_bg"], font=self.label_font)
        chat_display.pack(padx=20, pady=(20, 10), expand=True, fill='both')

        # Lower Frame for User Input and Buttons
        lower_frame = tk.Frame(conversation_frame, bg=self.colors["background"])
        lower_frame.pack(padx=20, pady=10, fill='x')

        # User Input Field
        user_input = tk.Entry(lower_frame, width=40, font=self.label_font)
        user_input.pack(side=tk.LEFT, padx=(0, 10), expand=True, fill='x')

        # Send Button
        send_button = tk.Button(lower_frame, text="Send", command=lambda: self.send_message(user_input, chat_display), bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        send_button.pack(side=tk.RIGHT, padx=(0, 10))

        # Back Button
        back_button = tk.Button(conversation_frame, text="Back", command=lambda: self.show_frame("main"), bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        back_button.pack(pady=5)

        # Binding Return Key to Send Button
        conversation_frame.bind('<Return>', lambda event=None: send_button.invoke())

        # Configure tags for chat bubbles
        chat_display.tag_configure('user', background="#697896", relief='raised', borderwidth=1, wrap='word')
        chat_display.tag_configure('aurora', background="#ff8a8a", relief='raised', borderwidth=1, wrap='word')
        chat_display.tag_configure('both', justify='left', lmargin1=10, lmargin2=10, rmargin=10, spacing3=10)

    def show_description(self, description):
        messagebox.showinfo("Exercise Description", description)

    def send_message(self, user_input, chat_display):
        user_message = user_input.get()
        if not user_message:
            return
        # Insert user message with styling
        chat_display.insert(tk.END, f"You: {user_message}\n", 'user')
        chat_display.tag_add('both', 'end-1c linestart', 'end-1c')
        user_input.delete(0, tk.END)
        
        openai.api_key = 'INSERT_API_KEY'

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        gpt_response = response.choices[0].message.content.strip()
        
        # Insert Aurora's response with styling
        chat_display.insert(tk.END, f"Aurora: {gpt_response}\n", 'aurora')
        chat_display.tag_add('both', 'end-1c linestart', 'end-1c')

        # Auto-scroll to the end
        chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = RelaxationGuide(root)
    app.show_frame("main")
    root.mainloop()