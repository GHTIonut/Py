import requests

response = requests.get("https://jsonplaceholder.typicode.com/comments")
if response.status_code == 200:
    posts = response.json()

    search = int(input('Insert ID that u are looking for: '))
    
    for post in posts: 
        if search == post['id']:
            print(f'You are looking for this post: \n- ID: {post['id']} \n- Text: {post['body']}')