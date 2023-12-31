#!/usr/bin/python3

import sys
import random
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

'''Define a class MentalHealthApp'''


class MentalHealthApp:
    '''present a menu of the app'''
    
    def __init__(self):
        '''Presents resources'''
        self.resources = ["Resource 1", "Resource 2", "Resource 3"]
        self.self_assessment_tools = [
            "Assessment Tool 1",
            "Assessment Tool 2",
            "Assessment Tool 3",
        ]
        self.chatbot_responses = [
            "I'm here to listen. How can I help?",
            "Remember, you're not alone in this.",
            "Don't hesitate to talk about your feelings.",
            "It's okay to ask for help.",
            "I'm here for you. What's on your mind?",
        ]
        self.community_forum_posts = []

    def show_menu(self):
        '''shows menu of the app'''
        print("\n==== MindConnect (Mental Health Awareness App) ====")
        print("1. Resources")
        print("2. Self-Assessment Tools")
        print("3. Support Chatbot")
        print("4. Community Forum")
        print("0. Exit")
        print("=====================================")

    def run(self):
        '''Runs user input'''
        print("Welcome again to MindConnect the Mental Health Awareness App!")
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
        '''Presents resources'''
        print("\n==== Resources ====")
        for index, resource in enumerate(self.resources, start=1):
            print(f"{index}. {resource}")
        input("Press Enter to go back to the main menu.")

    def show_self_assessment_tools(self):
        '''presents self assessment tools'''
        print("\n==== Self-Assessment Tools ====")
        for index, tool in enumerate(self.self_assessment_tools, start=1):
            print(f"{index}. {tool}")
        input("Press Enter to go back to the main menu.")

    def start_chatbot(self):
        '''presents chatbot'''
        print("\n==== Support Chatbot ====")
        print("Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break
            else:
                print("Bot:", random.choice(self.chatbot_responses))

    def show_community_forum(self):
        '''Presents community forum'''
        print("\n==== Community Forum ====")
        if not self.community_forum_posts:
            print("No posts yet. Be the first to start a conversation!")
        else:
            for post in self.community_forum_posts:
                print(f"- {post}")
        new_post = input("Write your post (or 'exit' to go back to the main menu): ")
        if new_post.lower() != "exit":
            self.community_forum_posts.append(new_post)


if __name__ == "__main__":
    '''run it on terminal'''
    app = MentalHealthApp()
    app.run()

