import os

a = 2
print("coucou", a)

token = os.environ.get("SECRET_API_TOKEN")
print("Le secret recupere est :", token)
