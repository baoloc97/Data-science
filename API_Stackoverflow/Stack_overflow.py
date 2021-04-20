import requests
import bs4
def top_question(N, lable):
    condition_input = {"site": "stackoverflow", "pagesize": N, "tagged": lable, "order": "desc", "sort": "votes"}
    r = requests.get("https://api.stackexchange.com/2.2/questions", params = condition_input)
    data = r.json()
    print(data['items'][0])
    print('Top 10 cau hoi')
    i = 0
    for item in data['items']:
        print('Cau ', i + 1)
        print(item['title'])
        print("link cau tra loi ")
        print(item['link'])
        i += 1
print(top_question(10,"python"))    
