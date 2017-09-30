import json
import twitter


def main():
    cred = json.load(open("credentials.json"))
    api = twitter.Api(consumer_key='OzT9MQFsYck3PCw7rDK9gTeqX',
                      consumer_secret=cred["consumer_secret"],
                      access_token_key=cred["access_token_key"],
                      access_token_secret=cred["access_token_secret"])

    d = json.load(open("speakers.json"))
    for i in d:
        soc = [i["link"] for i in filter(lambda x: x["name"] == "Twitter",
                                         i["socials"])]
        if soc and soc[0] != "TODO":
            username = soc[0].split('/')[-1]
            try:
                # print(username)
                # print(api.GetUser(screen_name=username).description)
                i["shortBio"] = api.GetUser(screen_name=username).description
                # print(i["shortBio"])
            except Exception as e:
                pass
        else:
            print(i["name"] + " MISSING")

    json.dump(d, open("speakers_final.json", "w", encoding="utf-8"),
              ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    main()
