import os, string, sys
# Import SQLite
from sqlite3 import dbapi2 as sqlite3
# Import AcoustID
import acoustid



# GLOBALS
DATA_PATH = ""
DATABASE = "fingerprints.sqlite"


# DB functions
def connect_db():
	# Connects to the database.
	rv = sqlite3.connect(DATABASE)
	rv.row_factory = sqlite3.Row
	return rv

def init_db():
	# Initializes the database.
	db = connect_db()
	f = open('schema.sql')
	for line in f:
		db.cursor().executescript(line)
	db.commit()

def query_db(query, args=(), one=False):
	db = connect_db()
	dbval = db.execute(query, args)
	rv = dbval.fetchall()
	db.close()
	return (rv[0] if rv else None) if one else rv

def write_db(query, args=()):
	db = connect_db()
	db.execute(query, args)
	db.commit()


# Internal functions
def writeEntry(fn, fp, chroma):
	write_db('insert into audiofingerprints (filename, full_path, fingerprint) values (?, ?, ?)', [fn, fp, chroma])

def exists_in_DB(fp):
	#tmpval = query_db('select id from audiofingerprints order by id asc')
	tmpval = query_db('select id from audiofingerprints where full_path=?', [fp])
	#print(tmpval)
	return len(tmpval)


# Main function
def mainFunc():
	print("")
	print("simpleMusicMatcher v0.1")
	
	# Do scan
	print("")
	print("Beginning library scan...")
	for root, dirs, files in os.walk(DATA_PATH, topdown=False):
		for fname in files:
			name, ext = os.path.splitext(fname)
			ext = ext.lower()
			
			print("")
			
			if ext == ".mp3":	# We only check for mp3s. Could work for anything supported by AcoustID.
				fpath = os.path.join(root,fname)
				#print(fpath)
				
				#Check if it already exists in the DB
				if exists_in_DB(fpath):
					print("File already scanned. Skipping...")
				else:
					print("Found " + fpath)
					duration, chroma = acoustid.fingerprint_file(fpath)
					writeEntry(fname, fpath, chroma)
	
	# Cross-reference all fingerprints
	print("")
	print("Beginnning fingerprint cross-reference...")
	
	all_items = query_db('select id, fingerprint from audiofingerprints order by id asc')
	item_count = len(all_items)
	
	for i in range(item_count):
		for j in range(i + 1, item_count):
			#print(all_items[i])
			#print(all_items[i]['fingerprint'])
			if(all_items[i]['fingerprint'] == all_items[j]['fingerprint']):
				print("")
				print("MATCH!")
				
				tmpval1 = query_db('select full_path from audiofingerprints where id=?', [all_items[i]['id']])[0]
				tmpval2 = query_db('select full_path from audiofingerprints where id=?', [all_items[j]['id']])[0]
				
				print(tmpval1['full_path'])
				print(tmpval2['full_path'])


# Technically *actually* main function
if __name__ == "__main__":
	print("")
	print("Starting...")
	
	# Check for path argument and exit if it doesn't exist
	if len(sys.argv) > 1:
		print("Music library path: " + sys.argv[1])
		DATA_PATH = sys.argv[1]
	else:
		print("You must supply a path argument.")
		print("Exiting...")
		sys.exit(1)
	
	# Check for database or create it
	if os.path.exists(DATABASE):
		print("Found database!")
	else:
		print("Database doesn't exist!")
		print("Initializing...")
		init_db()
	
	mainFunc()
