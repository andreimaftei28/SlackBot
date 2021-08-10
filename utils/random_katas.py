import random
import json
from scrapping_tool.main import get_katas

path_to_posted = "path/to/posted.json"
with open(path_to_posted, "r") as json_file:
    posted_katas = json.load(json_file)

def random_katas_generator():
    """
    select an exercises to be posted with 2 conditions :
        1. difficulty level must be different from the last posted exercise
        2. always choose an exercise that haven't been posted before
    :return: a 'random' exercise to be posted
    """
    get_katas("https://www.codewars.com/kata/search/python?q=&r[]=-8&r[]=-7&r[]=-6&beta=false")
    path = "path/to/katas.json"
    posted_titles = [x["title"] for x in posted_katas]
    with open(path, "r") as file:
        katas_dict = json.load(file)
    while True:
        kata = random.choice(katas_dict)
        if kata["title"] not in posted_titles and kata["diff"] != posted_katas[-1]["diff"]:
            posted_katas.append({"title": kata["title"], "diff": kata["diff"]})
            with open(path_to_posted, "w") as file:
                json.dump(posted_katas, file)
            return kata

#print(random_katas_generator())