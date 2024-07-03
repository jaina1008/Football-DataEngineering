def get_wikipedia_page(url):
    import requests

    print('Getting wikipedia page...', url)

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # check if request was successful

        return response.text 
    except requests.RequestException as e:
        print(f"An error has occured: {e}")
