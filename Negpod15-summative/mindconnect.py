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


'''Define a class MentalHealthApp'''
class MentalHealthApp:
     '''presend a  menu of the app'''
	def __init__(self):
		self.resources = ["Resource 1", "Resource 2", "Resource 3"]
		self.self_assessment_tools = [
			"Assessment Tool 1",
			"Assessment Tool 2",
			"Assessment Tool 3",
		]
