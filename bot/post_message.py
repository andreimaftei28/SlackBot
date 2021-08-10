import os
import random
from slack import WebClient
from dotenv import load_dotenv
from bot.builder import construct_payload
from utils.random_katas import random_katas_generator

quotes = ["You've got this!", "Take the risk!", "Be the change!", "Never, ever, give up!", "Every exercise matters!",
		  "I can and I will!", "You can do hard things!", "Good things take time!", "Enjoy the journey!"]
# load .env file with login tokens
load_dotenv()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

slack_web_client = WebClient(token=SLACK_BOT_TOKEN)

def post_katas_to_channel():
	"""
	post message to slack using slack module for python 
	"""
	kata = random_katas_generator()
	difficulty = kata["diff"]
	title = kata["title"]
	link = kata["kata_link"]
	message = construct_payload(
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*Your daily <{difficulty.upper()}> Python exercise is here!* :blush: :python:\n*Today's quote: {random.choice(quotes)}* :dancing-hamster: :party_blob:"
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": f"*{title}*\n{link}"
			}
		},
		{
			"type": "divider"
		})
	response = slack_web_client.chat_postMessage(**message)

#post_katas_to_channel()
