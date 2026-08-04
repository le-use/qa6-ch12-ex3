import requests

for i in range(1, 11):
    url = f"https://jsonplaceholder.typicode.com/users/{i}"
    response = requests.get(url)

    print(response.status_code)
    print("=========")

    if response.status_code == 200:

        data = response.json()
        print(data['name'])
        print(data['email'])
