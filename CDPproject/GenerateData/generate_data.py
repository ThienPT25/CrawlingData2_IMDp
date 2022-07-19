import random, json
import pandas as pd

def calculate_score():
    return random.randint(0,10), random.randint(10,20),random.randint(20,30),random.randint(30,40),random.randint(40,50)

df = pd.read_csv("./dim_product.csv", encoding="utf-8")
df["name"] = df["name"].apply(lambda x : str(x).replace("REPLAY", "").replace("\\", "").replace("<p>", "").replace("</p>", "").replace("  ", " ").strip())
df["description"] = df["description"].apply(lambda x : str(x).strip().replace(" ", "-"))
path_link = list(df["description"])
title = list(df["name"])
json_obj_list = []
for i in range(1000):
    tp, fp, tn, fn, ar = calculate_score()
    json_obj_list.append({"channel": "web", "context": {"app": {"build": "1.0.0", 
                                                                "name": "RudderLabs JavaScript SDK", 
                                                                "namespace": "com.rudderlabs.javascript", 
                                                                "version": "1.1.18"}, 
                                                        "traits": {}, 
                                                        "library": {"name": "RudderLabs JavaScript SDK", 
                                                                    "version": "1.1.18"}, 
                                                        "userAgent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27", 
                                                        "locale": "en-US", 
                                                        "os": {"name": "", 
                                                            "version": ""}, 
                                                        "screen": {"density": tp, 
                                                                "width": fp, 
                                                                "height": tn, 
                                                                "innerWidth": fn, 
                                                                "innerHeight": ar}, 
                                                        "campaign": {}, 
                                                        "page": {"path": "/" + path_link[i]+ ".html", 
                                                                "referrer": "https://hoangphuc.vn/", 
                                                                "referring_domain": "vnexress.net", 
                                                                "search": "", 
                                                                "title": title[i], 
                                                                "url": "https://hoangphuc.vn/" + path_link[i] + ".html", 
                                                                "tab_url": "https://hoangphuc.vn/" + path_link[i] + ".html", 
                                                                "initial_referrer": "$direct", "initial_referring_domain": ""}}, 
                        "type": "page", 
                        "messageId": "e424216b-b396-4ebe-98be-00ec362bf894", 
                        "originalTimestamp": "2021-08-06T04:23:43.476Z", 
                        "anonymousId": "611f2fe4-010f-4616-823c-e7f59e85af65", 
                        "userId": "", 
                        "properties": {"path": "/" + path_link[i]+ ".html", 
                                        "referrer": "https://hoangphuc.vn/", 
                                        "referring_domain": "tuoitre.vn", 
                                        "search": "", 
                                        "title": title[i], 
                                        "url": "https://hoangphuc.vn/" + path_link[i] + ".html", 
                                        "tab_url": "https://hoangphuc.vn/" + path_link[i] + ".html", 
                                        "initial_referrer": "$direct", 
                                        "initial_referring_domain": ""}, 
                        "integrations": {"All": "true"}, 
                        "sentAt": "2021-08-06T04:37:08.537877", 
                        "tenant_id": "Customer" + str(i + 1)})


json_dump = json.dumps(json_obj_list, indent="\t")
print(json_dump)

#open text file
text_file = open("data.json", "w")
 
#write string to file
n = text_file.write(json_dump)
 
#close file
text_file.close()