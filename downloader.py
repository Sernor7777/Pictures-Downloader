from bs4 import BeautifulSoup
import urllib.request as urllib2
import os
import subprocess


images = []


def geturl(word, pages_amount):
    page = 0
    percentage = 0
    try:
        while page <= pages_amount:
            url = urllib2.urlopen(
                f'https://www.istockphoto.com/search/2/image?phrase={word}&page={page}')
            page += 1
            percentage += 100 / (pages_amount + 1)
            print(f'Loading {percentage}%...')
            soup = BeautifulSoup(url, 'html.parser')
            for img in soup.findAll('img'):
                images.append(img.get('src'))

    except:
        print("Too Many Requests")
        exit()


def imgs_to_txt(txt_name):
    output = ""

    with open(f'{txt_name}.txt', 'a') as f:
        for image in images:
            f.write("%s\n" % image)

    with open(f'{txt_name}.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.endswith("="):
                output += line + "\n"

    f = open(f'{txt_name}.txt', 'w')
    f.write(output)


def open_file_location(txt_name):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, f'{txt_name}.txt')
    subprocess.Popen(f'explorer /select,"{file_path}"')


word = input("What photos do you want?\n")
images_amount = int(input(
    "How many pictures of that do you want?(max = 6000, Can be devided by 60)\n"))
if images_amount <= 6000:
    if images_amount % 60 == 0:
        pages_amount = (images_amount // 60) - 1
    else:
        pages_amount = (images_amount // 60)
else:
    exit()
txt_name = input("What do you want to name your .txt file?\n")


geturl(word, pages_amount)
imgs_to_txt(txt_name)
open_file_location(txt_name)
