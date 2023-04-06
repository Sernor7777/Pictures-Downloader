import requests

count = 0
txt = input("What is the name of your txt file (without .txt and make sure to put the file in the same directory as the script and make sure you have a folder called pictures in the same directory.)\n")

with open(rf'{txt}.txt', 'r') as f:
    content = f.readlines()
    lines = len(content)
    while count < lines:
        url = content[count].replace("\n", "")
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(f"pictures/picture{count}.jpg", 'wb') as f:
                f.write(res.content)
        count += 1
        
