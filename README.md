# Unfollowgram
Python script that automates the Instagram unfollow process

**Requirements**

- Python 3.8+ - https://www.python.org/downloads/
- Selenium - https://www.selenium.dev/downloads/
- ChromeDriver or the selenium driver for your preferred browser - https://www.selenium.dev/documentation/en/webdriver/driver_requirements/
- Read the code and customize it with you credentials (everything in capital letters)

**How it works?**

Unfollowgram is a simple but effective python script that controls your browser with selenium. Once you have added your credentials to the correct fields, it will:

1. Load Instagram and accept cookies in case there are some. 
2. Log in with the username and password provided
3. Decline notifications in case there are some.
4. Load your following list
5. Unfollow users one by one, waiting 10 seconds before each new unfollow.
6. When the entire list is empty or doesn't load anymore users, the script will wait for 2 minutes before reloading your list.
7. Repeat the process, until you have unfollowed a maximum of 150 accounts 



**Notes**
- The script is written to find the buttons in the Instagram webpage in English. If by default your browser opens in any other language, you'd have to edit the script simply adding the correct words in your language.
- The total waiting time between actions and maximum number of unfollows is set to replicate the human behaviour, in order to avoid getting banned. Feel free to fork the project with your own seetings
- It's recommended to use this script in conjunction with [Instamatic](https://github.com/davidgarrote/Instamatic), which automates the process of finding posts of interest, liking them, leaving a comment and following the user: 
