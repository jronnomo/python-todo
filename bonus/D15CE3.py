import webbrowser

user_term = input("What would you like to search?: ").strip().replace(' ', '+')

webbrowser.open("https://google.com/search?q=" + user_term)
