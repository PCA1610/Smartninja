from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup


def main():
    url = 'https://scrapebook22.appspot.com/'
    response = urlopen(url).read()

    soup = BeautifulSoup(response)

    for link in soup.findAll('a'):
        if link.string == "See full profile":
            person_url = "https://scrapebook22.appspot.com/" + link["href"]
            person_html = urlopen(person_url).read()
            soup_person = BeautifulSoup(person_html)

            email_list = open("email_list.txt", "w+")  # open the TXT file (or create a new one)

            email_list.write(soup_person.find("span", attrs={"class": "email"}).string + "\n")  # add task into the TXT

            email_list.write("\n")

            email_list.close()  # close the TXT file


if __name__ == "__main__":
    main()
