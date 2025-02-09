import sqlite3

con = sqlite3.connect("dt.bs")
cur = con.cursor()

global send_messages
send_messages = True

def toggle_warnings(set_value: bool = None):
	global send_messages
	if set_value == None:
		send_messages = not send_messages
	else:
		send_messages = set_value

def create_table(name: str, columns: dict):
	cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = ?", (name,))
	table = cur.fetchone()
	if not table:
		_columns = []
		for value in columns:
			_columns.append(f"{value} {columns[value]}")
		cur.execute(f"""CREATE TABLE {name} (
			{", ".join(_columns)}
		)""")
	elif send_messages:
		print(f"[DTBS] \033[33mTable \"{name}\" already exists!\033[0m")

def add_row(name: str, columns: dict):
	column_names = ', '.join(columns.keys())
	placeholders = ', '.join(['?'] * len(columns))
	query = f"INSERT INTO {name} ({column_names}) VALUES ({placeholders})"
	cur.execute(query, tuple(columns.values()))
	con.commit()

def set_value(name: str, column: str, value, condition_column: str, condition_value):
	cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name = ?", (name,))
	table = cur.fetchone()
	if not table and send_messages:
		print(f"[DTBS] \033[31mTable \"{name}\" does not exist!\033[0m")
		return
	query = f"UPDATE {name} SET {column} = ? WHERE {condition_column} = ?"
	
	cur.execute(query, (value, condition_value,))
	con.commit()
def value_exists(table: str, column: str, value):
	query = f"SELECT 1 FROM {table} WHERE {column} = ? LIMIT 1"
	cur.execute(query, (value,))
	result = cur.fetchone()
	if result:
		return True
	elif send_messages:
		print(f"[DTBS] \033[31mValue {value} does not exist in column {column} of table {table}.\033[0m")
		return False
def get_row(table: str, column: str, value):
	query = f"SELECT * FROM {table} WHERE {column} = ? LIMIT 1"
	
	cur.execute(query, (value,))
	
	row = cur.fetchone()
	
	if row:
		column_names = [description[0] for description in cur.description]
		
		row_dict = dict(zip(column_names, row))
		return row_dict
	else:
		print(f"[DTBS] \033[31mNo row with {column} = {value} found in table {table}.\033[0m")
		return None
