#!/usr/bin/python3
import time
username = input("Enter your username to sign in: ")
print("Welcome to MindConnect, {}!".format(username))
time.sleep(1)

disclaimer = """
Disclaimer: 

The MindConnect App and its integrated support chatbot provide information and tools to promote mental health wellbeing. However, they are not a substitute for professional medical advice or treatment. Users should consult qualified healthcare professionals for personalized guidance. Users interact with the app and chatbot at their own risk and are responsible for their decisions. In case of an emergency, please seek immediate assistance from a medical professional or call your local emergency number.
"""

print(disclaimer)
time.sleep(1)


import sys
import random
import sqlite3
import webbrowser

'''Define a class MentalHealthApp'''


class MentalHealthApp:
    '''present a menu of th app'''
    
    def __init__(self):
    
        self.resources = ["ALU Wellness Center", "Better Help (https://www.betterhelp.com/)", "Suicide Prevention hotline 8015"]
         
        self.self_assessment_tools = [
            "Welcome to the Mental Health Assessment Quiz!",
            "Please answer the following questions with 'yes' or 'no'.",
            "Do you often feel sad or depressed?",
            "Do you have trouble sleeping or sleeping too much?",
            "Do you often feel anxious or worried?",
            "Do you have trouble concentrating or making decisions?",
            "Do you have thoughts of harming yourself or others?"
        ]
        self.chatbot_responses = [
            "I'm here to listen. How can I help?",
            "Remember, you're not alone in this.",
            "Don't hesitate to talk about your feelings.",
            "It's okay to ask for help.",
            "I'm here for you. What's on your mind?",
            "Challenge negative thoughts and replace them with more positive ones.",
            "Believe in your ability to overcome challenges; you've done it before.",
        ]
        self.community_forum_posts = []
        self.conn = sqlite3.connect('community_forum.db')
        self.create_table()

    def create_table(self):
        '''create a table to store the forum posts'''
        self.conn.execute('''CREATE TABLE IF NOT EXISTS forum_posts
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            POST TEXT NOT NULL,
                            username TEXT NOT NULL);''')
        self.conn.commit()
    def show_self_assessment_tools(self):
        print("\n==== Self-Assessment Tool ====")
        print("Press Enter to start the quiz.")
        input()
        print("Please answer the following questions with 'yes' or 'no'.")
        input()  # Wait for Enter to start

        score = 0
        for question in self.self_assessment_tools[2:]:
            answer = input(question + " ")
            if answer.lower() == "yes":
                score += 1

        print("\nThank you for taking the quiz!")
        print("Your score is:", score)
        if score == 0:
            print("You seem to be doing well mentally.")
        elif score <= 2:
            print("You may be experiencing some mental health issues. Consider seeking help.")
        else:
            print("You may be experiencing significant mental health issues. Please seek help immediately.")

    def show_community_forum(self):
        print("\n==== Community Forum ====")
        cursor = self.conn.execute("SELECT POST, username FROM forum_posts")
        posts = cursor.fetchall()
        if not posts:
            print("No posts yet. Be the first to start a conversation!")
        else:
            for post in posts:
                print("- {} (posted by {})".format(post[0], post[1]))

        new_post = input("Write your post (or 'exit' to go back to the main menu): ")
        if new_post.lower() != "exit":
            self.conn.execute("INSERT INTO forum_posts (POST, username) VALUES (?, ?)", (new_post, username))
            self.conn.commit()
            print("Post added successfully!")
    import time



    def show_menu(self):
        menu_lines = [
            "==== Mental Health Awareness App ====",
            "1. Resources",
            "2. Self-Assessment Tools",
            "3. Support Chatbot",
            "4. Community Forum",
            "0. Exit",
            "====================================="
        ]

        delay_between_lines = 0.5  

        for line in menu_lines:
            print(line)
            time.sleep(delay_between_lines)





    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice (0-4): ")
            if choice == "1":
                self.show_resources()
            elif choice == "2":
                self.show_self_assessment_tools()
            elif choice == "3":
                self.start_chatbot()
            elif choice == "4":
                self.show_community_forum()
            elif choice == "0":
                print("Exiting the app. Take care!")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_resources(self):
        print("\n==== Resources ====")
        for index, resource in enumerate(self.resources, start=1):
            print("{}. {}".format(index, resource))
        input("Press Enter to go back to the main menu.")



    

    def start_chatbot(self):
        print("\n==== Support Chatbot ====")
        print("Type 'exit' to end the chat.")
        while True:
            user_input = input("{}: ".format(username))
            if user_input.lower() == "exit":
                break
            else:
                print("Bot:", random.choice(self.chatbot_responses))

    

if __name__ == "__main__":
    '''run it on terminal'''
    app = MentalHealthApp()
    app.run()
