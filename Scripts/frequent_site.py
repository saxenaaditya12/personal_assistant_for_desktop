import webbrowser


def site(x):
    try:
        webbrowser.open_new_tab('https://www.%s.com/search?q=' % x)  # Open a specific site
    except Exception as e:
        print(e)
        print("* Error in opening new tab *")
