import webbrowser


def movies(x):
    try:
        webbrowser.open_new_tab('https://www.google.com/search?q=' + x)  # Open a tab of your search
    except Exception as e:
        print(e)
        print("* Error in opening new tab *")
