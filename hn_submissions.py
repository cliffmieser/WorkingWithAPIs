#hn_submissions.py

from operator import itemgetter
import requests


#Make API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'       #1
r = requests.get(url)
print(f"Status Code: {r.status_code}")

#Process information about the submission
submission_ids = r.json()       #2
submission_dicts = []           #3
for submission_id in submission_ids[:30]:
    #make seperate API call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'      # 4
    r = requests.get(url)
    print(f"id: {submission_id}\tStatus: {r.status_code}")
    response_dict = r.json()

    #Build dictionary for each article
    try:
        submission_dict = {         #5
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],    
        }
    except KeyError:
        print("Key unknown")
    submission_dicts.append(submission_dict)        #6

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse = True)         #7

for submission_dict in submission_dicts:        #8
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")    
