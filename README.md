# dtbs.py
Simplifies SQLITE3 to handle the commands in python form, might not be fully complete though

## Example code
```py

dtbs.toggle_warnings(True) # set to true on default, if you just want to toggle dont include any args

dtbs.create_table("USERS", {
  "id": "TEXT",
  "name": "TEXT,
  "balance": "INTEGER"
})

dtbs.add_row("USERS", {
  "id": "1234d",
  "name": "mmph",
  "balance": 100
})

user = dtbs.get_row("USERS", "id", "1234d")
print(f"Users balance is {user["balance"]}")
                        # set to        # which row with identifier
dbts.set_value("USERS", "balance", 200, "id", "1234d")

print(f"Does user with id 20103 exist? {dbts.value_exists("USERS", "id", "20103")}")
```
