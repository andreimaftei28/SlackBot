def construct_payload(HEADER_BLOCK, DIVIDER_BLOCK, MESSAGE_BLOCK, DIVIDER_BLOCK1):
    """
    construct the message to be posted
    """
    return {
        "channel": "C01QGE69N91", # change this with the channel id where your bot should post 
        "username": "Andrei's Python Bot", 
        "icon_emoji": ":robot_face",
        "text": ":wave: Your daily training Python exercise is here!",
        "blocks": [
            HEADER_BLOCK,
            DIVIDER_BLOCK,
            MESSAGE_BLOCK,
            DIVIDER_BLOCK1
        ],
    }