#!/usr/bin/python3
username = input("Enter your username to sign in: ")
print("Welcome to MindConnect, {}!".format(username))

disclaimer = """
Disclaimer: 

The MindConnect App and its integrated support chatbot provide information and tools to promote mental health wellbeing. However, they are not a substitute for professional medical advice or treatment. Users should consult qualified healthcare professionals for personalized guidance. Users interact with the app and chatbot at their own risk and are responsible for their decisions. In case of an emergency, please seek immediate assistance from a medical professional or call your local emergency number.
"""

print(disclaimer)


while True:
 answer =input("Do you wish to continue? ")
