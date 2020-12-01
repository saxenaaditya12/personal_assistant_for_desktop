import webbrowser


def meaning(x):
    try:
        webbrowser.open_new_tab('https://www.google.com/search?q=%s meaning' % x)  # Open a tab of word meaning
    except Exception as e:
        print(e)
        print("* Error in opening new tab *")
