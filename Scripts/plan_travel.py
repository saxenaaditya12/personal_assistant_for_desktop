import webbrowser


def travel():
    try:
        webbrowser.open_new_tab('https://www.makemytrip.com/')  # Open a tab of your search
    except Exception as e:
        print(e)
        print("* Error in opening new tab *")
