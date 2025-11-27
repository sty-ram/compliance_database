from flask import Flask, request, jsonify
from database.db import init_db, create_user, get_user
from database.db import save_image, fetch_images # Importing new image functions
app = Flask(__name__)
init_db()

@app.route("/db/create_user", methods=["POST"])
def db_create_user():
    data = request.get_json()
    result = create_user(data["username"], data["password"])
    return jsonify(result), 200

@app.route("/db/get_user", methods=["POST"])
def db_get_user():
    data = request.get_json()
    user = get_user(data["username"])
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Not found"}), 404

# Additional routes for image handling to match db.py functions

@app.route("/db/upload_image", methods=["POST"])
def upload_image():
    username = request.form.get("username")
    file = request.files.get("file")

    if not file:
        return jsonify({"error": "No file"}), 400

    data = file.read()
    res = save_image(username, file.filename, data)
    return jsonify(res), 200

@app.route("/db/list_images", methods=["POST"])
def list_images():
    data = request.get_json()
    username = data.get("username")
    imgs = fetch_images(username)
    return jsonify(imgs), 200

@app.route("/db/get_dummy_data", methods=["GET"])

# added route for dummy data retrieval
def get_dummy_data():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT country, entity, product, docs, compliance FROM dummy_mappings")
        rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            "country": row[0],
            "entity": row[1],
            "product": row[2],
            "docs": row[3].split(","),
            "compliance": row[4].split(",")
        })

    return jsonify(result), 200


if __name__ == "__main__":
    app.run(port=6000, debug=True)
