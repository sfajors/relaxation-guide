import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import font as tkfont
from tkinter import ttk
import openai

class RelaxationGuide:
    def __init__(self, root):
        self.root = root
        root.title("Relaxation Guide")

        # Define color scheme and styles
        self.colors = {
            "background": "#968769",
            "button": "#968769",
            "button_active": "#C9C1B1",
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

        # Header Frame
        header_frame = tk.Frame(self.root, bg=self.colors["background"])
        header_frame.pack(fill="both")

        # Header Title
        header_label = tk.Label(header_frame, text="Relaxation Guide", bg=self.colors["background"], fg=self.colors["text"], font=self.title_font)
        header_label.pack(pady=10)

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

        # Add a Back button to the exercises frame
        back_button_exercises = tk.Button(exercises_frame, text="Back", command=self.back_to_main, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        back_button_exercises.pack(pady=5)

        # Conversation Frame
        conversation_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["conversation"] = conversation_frame
        self.initialize_conversation_ui(conversation_frame)

    def initialize_feelings(self):
        return {
            "Stressed": {
                "Deep Breathing": "Take a deep breath in through your nose, hold for a few seconds, and exhale through your mouth. Repeat several times.",
                "Box Breathing": "Inhale for a count of 4, hold for 4, exhale for 4, and wait for 4. Repeat the cycle.",
                "Progressive Muscle Relaxation": "This technique involves tensing and then releasing each muscle group in your body, starting from your toes and working your way up to your head. It can help release physical tension and promote relaxation.",
                "Visualization": "Close your eyes and imagine yourself in a calm and peaceful place, such as a beach or forest. Visualizing a serene environment can help reduce stsress and promote relaxation",
                "Journaling": "Write down your thoughts and feelings in a journal. Expressing your emotions on paper can help you gain clarity, process your stressors, and find a solution"
            },
             "Anxious": {
                "4-7-8 Breathing": "Inhale for a count of 4, hold for 7, and exhale for 8. This pattern helps to calm the nervous system.",
                "Progressive Relaxation": "Tense and then relax each muscle group, starting from your toes and working up to your head.",
                "Grounding Techniques": "Focus on your senses to ground yourself in the present. Describe five things you can see, four things you can touch, three things you can hear, two things you can smell, and one thing you can taste.",
                "Positive Affirmations": "Repeat positive statements to yourself, such as 'I am calm and in control' or 'I can handle this situation.' Affirmations can counteract negative thoughts and reduce anxiety.",
                "Mindful Body Scan": "Close your eyes and mentally scan your body, paying attention to any areas of tension or discomfort. Breathe into those areas and release the tension.",
            },
            "Sad": {
                "Diaphragmatic Breathing": "Place one hand on your chest and the other on your stomach. Breathe deeply such that the hand on your stomach rises. Exhale and repeat.",
                "Gratitude Meditation": "Focus on things in your life you are grateful for. Visualize them and hold onto the positive feelings.",
                "Creative Expression": "Engage in creative activities like art, music, or writing. Expressing your emotions through creativity can be therapeutic and provide an outlet for sadness.",
                "Physical Activity": "Engage in physical exercise, even if it's a short walk. Exercise releases endorphins, which can help improve your mood and alleviate sadness.",
                "Connect with Loved Ones": "Reach out to friends or family members for support and companionship. Talking to someone you trust can help you feel less alone in your sadness.",
            },
            "Angry": {
                "Counted Breathing": "Inhale slowly to the count of four, then exhale to the count of four. Focus on the numbers to divert attention from anger.",
                "Compassion Meditation": "Visualize the person or situation causing anger. Send them positive energy and wishes. This helps to release negative emotions.",
                "Take a Timeout": "When you feel anger rising, step away from the situation or conversation if possible. Take a break to cool off and regain composure before addressing the issue.",
                "Use 'I' Statements": "Express your anger assertively using 'I' statements to communicate your feelings and needs without blaming or accusing others. For example, say 'I feel frustrated when...' instead of 'You always make me angry.'",
                "Seek Support": "Talk to a trusted friend, family member, or therapist about your anger. Sharing your feelings and getting support can help you process and manage anger.",  
            },
            "Overwhelmed": {
                "Abdominal Breathing": "Place your hands on your abdomen. Take a deep breath in, letting your abdomen rise. Exhale slowly and feel it fall. Repeat.",
                "Guided Imagery": "Close your eyes and visualize a peaceful place or scenario. Engage all your senses and immerse yourself in the visualization.",
                "Prioritize Tasks": "Make a list of tasks or responsibilities, then prioritize them based on importance and deadlines. Focus on completing one task at a time to reduce the feeling of overwhelm.",
                "Time Management Techniques": "Use time management methods like the Pomodoro Technique or the two-minute rule to structure your work and break it into focused intervals.",
                "Delegate Responsibility": "If possible, delegate tasks to others when you have too much to handle. Delegating can lighten your workload and reduce feelings of overwhelm.",
            }
        }

    def show_frame(self, frame_name):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show the requested frame
        frame = self.frames[frame_name]
        frame.pack(pady=20, padx=20, expand=True, fill="both")
    
    def back_to_main(self):
        # Hide all frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Show the main frame
        self.frames["main"].pack(pady=20, padx=20, expand=True, fill="both")

    def show_feeling_info(self, feeling):
        feeling_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["feeling"] = feeling_frame

        # Back button
        back_button_feeling = tk.Button(feeling_frame, text="Back", command=lambda: self.back_to_main(feeling_frame), bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        back_button_feeling.pack(pady=5)

        # Display feeling information and exercises
        tk.Label(feeling_frame, text=feeling, bg=self.colors["background"], fg=self.colors["text"], font=self.title_font).pack(pady=10)
        for exercise, description in self.feelings[feeling].items():
            tk.Label(feeling_frame, text=exercise, bg=self.colors["background"], fg=self.colors["text"], font=self.label_font).pack(pady=5)
            tk.Label(feeling_frame, text=description, bg=self.colors["background"], fg=self.colors["text"], font=self.label_font, wraplength=600).pack(pady=5)
        
        self.show_frame("feeling")

    def show_exercises(self, feeling):
        exercises_frame = self.frames["exercises"]

        # Clear previous content
        for widget in exercises_frame.winfo_children():
            widget.destroy()

        # Create exercise buttons
        for exercise, description in self.feelings[feeling].items():
            btn = tk.Button(exercises_frame, text=exercise, command=lambda d=description: self.show_exercise_description(d), bg=self.colors["button"], font=self.label_font, activebackground=self.colors["button_active"])
            btn.pack(pady=5, expand=True, fill='x')

        # Back button
        back_button = tk.Button(exercises_frame, text="Back", command=self.back_to_main, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        back_button.pack(pady=5)

        self.show_frame("exercises")

    def show_exercise_description(self, description):
        description_frame = tk.Frame(self.root, bg=self.colors["background"])
        self.frames["description"] = description_frame

        # Display the description
        description_label = tk.Label(description_frame, text=description, bg=self.colors["background"], fg=self.colors["text"], font=self.label_font, wraplength=600)
        description_label.pack(pady=10, padx=20, expand=True, fill='both')

        # Back button to return to the main screen
        back_button = tk.Button(description_frame, text="Back", command=self.back_to_main, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
        back_button.pack(pady=5)

        self.show_frame("description")

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
        back_button = tk.Button(conversation_frame, text="Back", command=self.back_to_main, bg=self.colors["button"], font=self.button_font, activebackground=self.colors["button_active"])
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
        
        openai.api_key = 'OPENAI_API_KEY'

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