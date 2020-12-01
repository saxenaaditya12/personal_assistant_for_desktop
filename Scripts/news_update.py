import webbrowser


def news():
    try:
        webbrowser.open_new_tab(
            'https://news.google.com/foryou?hl=en-IN&gl=IN&ceid=IN%3Aen')  # Open a tab of your search
    except Exception as e:
        print(e)
        print("* Error in opening new tab *")
