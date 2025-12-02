import sqlite3

DB_PATH = "app.db"

# def init_db():
#     with sqlite3.connect(DB_PATH) as conn:
#         conn.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT UNIQUE NOT NULL,
#                 password TEXT NOT NULL
#             )
#         ''')
#         conn.commit()
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                filename TEXT NOT NULL,
                data BLOB NOT NULL
            )
        ''')
        conn.commit()
def init_dummy_data_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS dummy_mappings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                country TEXT NOT NULL,
                entity TEXT NOT NULL,
                product TEXT NOT NULL,
                docs TEXT NOT NULL,
                compliance TEXT NOT NULL
            )
        """)
        conn.commit()


def create_user(username, password_hash):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password_hash)
            )
            conn.commit()
        return {"status": "success"}
    except sqlite3.IntegrityError:
        return {"status": "error", "message": "User exists"}

def get_user(username):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT username, password FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        if row:
            return {"username": row[0], "password": row[1]}
        return None
# Image handling functions adding to upload and fetch images
def save_image(username, filename, data):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO images (username, filename, data) VALUES (?, ?, ?)",
            (username, filename, data)
        )
        conn.commit()
        return {"status": "success"}


def fetch_images(username):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, filename FROM images WHERE username = ?",
            (username,)
        )
        return [{"id": row[0], "filename": row[1]} for row in cursor.fetchall()]

# image upload storage end
def init_image_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                doc_type TEXT NOT NULL,
                filename TEXT NOT NULL,
                filedata BLOB NOT NULL,
                uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()



# Initialize dummy data table when the module is imported
def seed_dummy_data():
    init_dummy_data_table() #  check it after running --> 
    data ={

        "India": {
        "Individual": {
            "Fintech":    {"docs": ["IN-IND-FIN-DOC1", "IN-IND-FIN-DOC2"], "compliance": ["IN-IND-FIN-COMP1"]},
            "Insurance":  {"docs": ["IN-IND-INS-DOC1", "IN-IND-INS-DOC2"], "compliance": ["IN-IND-INS-COMP1"]},
            "eSIM":       {"docs": ["IN-IND-ESIM-DOC1", "IN-IND-ESIM-DOC2"], "compliance": ["IN-IND-ESIM-COMP1"]}
        },
        "Business": {
            "Fintech":    {"docs": ["IN-BUS-FIN-DOC1", "IN-BUS-FIN-DOC2"], "compliance": ["IN-BUS-FIN-COMP1"]},
            "Insurance":  {"docs": ["IN-BUS-INS-DOC1", "IN-BUS-INS-DOC2"], "compliance": ["IN-BUS-INS-COMP1"]},
            "eSIM":       {"docs": ["IN-BUS-ESIM-DOC1", "IN-BUS-ESIM-DOC2"], "compliance": ["IN-BUS-ESIM-COMP1"]}
        }
    },

    "USA": {
        "Individual": {
            "Fintech":    {"docs": ["US-IND-FIN-DOC1", "US-IND-FIN-DOC2"], "compliance": ["US-IND-FIN-COMP1"]},
            "Insurance":  {"docs": ["US-IND-INS-DOC1", "US-IND-INS-DOC2"], "compliance": ["US-IND-INS-COMP1"]},
            "eSIM":       {"docs": ["US-IND-ESIM-DOC1", "US-IND-ESIM-DOC2"], "compliance": ["US-IND-ESIM-COMP1"]}
        },
        "Business": {
            "Fintech":    {"docs": ["US-BUS-FIN-DOC1", "US-BUS-FIN-DOC2"], "compliance": ["US-BUS-FIN-COMP1"]},
            "Insurance":  {"docs": ["US-BUS-INS-DOC1", "US-BUS-INS-DOC2"], "compliance": ["US-BUS-INS-COMP1"]},
            "eSIM":       {"docs": ["US-BUS-ESIM-DOC1", "US-BUS-ESIM-DOC2"], "compliance": ["US-BUS-ESIM-COMP1"]}
        }
    },

    "Singapore": {
        "Individual": {
            "Fintech":    {"docs": ["SG-IND-FIN-DOC1", "SG-IND-FIN-DOC2"], "compliance": ["SG-IND-FIN-COMP1"]},
            "Insurance":  {"docs": ["SG-IND-INS-DOC1", "SG-IND-INS-DOC2"], "compliance": ["SG-IND-INS-COMP1"]},
            "eSIM":       {"docs": ["SG-IND-ESIM-DOC1", "SG-IND-ESIM-DOC2"], "compliance": ["SG-IND-ESIM-COMP1"]}
        },
        "Business": {
            "Fintech":    {"docs": ["SG-BUS-FIN-DOC1", "SG-BUS-FIN-DOC2"], "compliance": ["SG-BUS-FIN-COMP1"]},
            "Insurance":  {"docs": ["SG-BUS-INS-DOC1", "SG-BUS-INS-DOC2"], "compliance": ["SG-BUS-INS-COMP1"]},
            "eSIM":       {"docs": ["SG-BUS-ESIM-DOC1", "SG-BUS-ESIM-DOC2"], "compliance": ["SG-BUS-ESIM-COMP1"]}
        }
    },

    "UAE": {
        "Individual": {
            "Fintech":    {"docs": ["UAE-IND-FIN-DOC1", "UAE-IND-FIN-DOC2"], "compliance": ["UAE-IND-FIN-COMP1"]},
            "Insurance":  {"docs": ["UAE-IND-INS-DOC1", "UAE-IND-INS-DOC2"], "compliance": ["UAE-IND-INS-COMP1"]},
            "eSIM":       {"docs": ["UAE-IND-ESIM-DOC1", "UAE-IND-ESIM-DOC2"], "compliance": ["UAE-IND-ESIM-COMP1"]}
        },
        "Business": {
            "Fintech":    {"docs": ["UAE-BUS-FIN-DOC1", "UAE-BUS-FIN-DOC2"], "compliance": ["UAE-BUS-FIN-COMP1"]},
            "Insurance":  {"docs": ["UAE-BUS-INS-DOC1", "UAE-BUS-INS-DOC2"], "compliance": ["UAE-BUS-INS-COMP1"]},
            "eSIM":       {"docs": ["UAE-BUS-ESIM-DOC1", "UAE-BUS-ESIM-DOC2"], "compliance": ["UAE-BUS-ESIM-COMP1"]}
        }
    },

    "Germany": {
        "Individual": {
            "Fintech":    {"docs": ["DE-IND-FIN-DOC1", "DE-IND-FIN-DOC2"], "compliance": ["DE-IND-FIN-COMP1"]},
            "Insurance":  {"docs": ["DE-IND-INS-DOC1", "DE-IND-INS-DOC2"], "compliance": ["DE-IND-INS-COMP1"]},
            "eSIM":       {"docs": ["DE-IND-ESIM-DOC1", "DE-IND-ESIM-DOC2"], "compliance": ["DE-IND-ESIM-COMP1"]}
        },
        "Business": {
            "Fintech":    {"docs": ["DE-BUS-FIN-DOC1", "DE-BUS-FIN-DOC2"], "compliance": ["DE-BUS-FIN-COMP1"]},
            "Insurance":  {"docs": ["DE-BUS-INS-DOC1", "DE-BUS-INS-DOC2"], "compliance": ["DE-BUS-INS-COMP1"]},
            "eSIM":       {"docs": ["DE-BUS-ESIM-DOC1", "DE-BUS-ESIM-DOC2"], "compliance": ["DE-BUS-ESIM-COMP1"]}
        }
    }


    }

    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany("""
            INSERT INTO dummy_mappings (country, entity, product, docs, compliance)
            VALUES (?, ?, ?, ?, ?)
        """, data)
        conn.commit()
