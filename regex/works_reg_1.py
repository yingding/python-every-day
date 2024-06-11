import re 

sql = "SELECT * FROM table"

allowed_key_words = ["PIP"]
# allowed_key_words = ["SELECT", "select"]

# regex to match sql string beginning with select 
if not any(re.match(rf'^\s*{word}', sql) for word in allowed_key_words):
    print("Invalid SQL, it does not start with {allowed_key_words}")
else:
    print("Valid SQL")