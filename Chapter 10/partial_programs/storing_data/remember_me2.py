# from pathlib import Path
# import json

# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")

# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}")



from pathlib import Path
import json

fillagring = Path('användarnamn.json')
if fillagring.exists():
    innehåll = fillagring.read_text()
    användarnamn = json.loads(innehåll)
    print(f"Välkommen tillbaka, {användarnamn}")

else:
    användarnamn = input("Vad är ditt namn/användarnamn? ")
    innehåll = json.dumps(användarnamn)
    fillagring.write_text(innehåll)
    print(f"Vi sparar och kommer ihåg dig till nästa gång du är tillbaka {användarnamn}")