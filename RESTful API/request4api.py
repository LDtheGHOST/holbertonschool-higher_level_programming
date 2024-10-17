from flask import Flask, jsonify, request
    """on utisilise flask pour creer un api ou on va ensuite faire une importation et des requete"""

app = Flask(__name__)
    """le code qui cree l'api"""

users = {}
    """on cree un dictionnaire vide pour stocker les donnee des utilisateurs"""

@app.route("/")
def home():
    return "Welcome to the Flask API!"
        """ on une route, qui va retouner le message"""

@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))
        """on cree un aute chemin qui jusqu'a la data ou j'ai la liste des clé et nom des utilisateurs"""

@app.route("/status")
def status():
    return "OK"
        """pareil que les autres"""

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
        """ pareil puis on demande des information pour trouver les utilisateur dans """
    
    if user:
        return jsonify(user)
            """si on trouve l'utilisateur on retoune"""
    
    else:
        return jsonify({"error": "User not found"}), 404
            """sinon retoune erreur"""
        
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201
        """la meme chose que l'autre a l'inverse"""
    
if __name__ == "__main__":
    app.run()
        """on lance l'api"""