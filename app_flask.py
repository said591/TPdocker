from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
users = db['users']

# Créer un utilisateur
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user = {
        'name': user_data['name'],
        'prenom': user_data['prenom'],
        'age': user_data['age']
    }
    result = users.insert_one(user)
    return {'id': str(result.inserted_id), 'message': 'Utilisateur créé avec succès'}

# Récupérer tous les utilisateurs
@app.route('/users', methods=['GET'])
def get_users():
    user_list = []
    for user in users.find():
        user_list.append({
            'id': str(user['_id']),
            'name': user['name'],
            'prenom': user['prenom'],
            'age': user['age']
        })
    return jsonify({'users': user_list})

# Récupérer un utilisateur par son ID
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.find_one({'_id': ObjectId(user_id)})
    if user:
        return {
            'id': str(user['_id']),
            'name': user['name'],
            'prenom': user['prenom'],
            'age': user['age']
        }
    else:
        return {'message': 'Utilisateur non trouvé'}

# Mettre à jour un utilisateur
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    updated_user = {
        'name': user_data['name'],
        'prenom': user_data['prenom'],
        'age': user_data['age']
    }
    result = users.update_one({'_id': ObjectId(user_id)}, {'$set': updated_user})
    if result.modified_count > 0:
        return {'message': 'Utilisateur mis à jour avec succès'}
    else:
        return {'message': 'Utilisateur non trouvé'}

# Supprimer un utilisateur
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = users.delete_one({'_id': ObjectId(user_id)})
    if result.deleted_count > 0:
        return {'message': 'Utilisateur supprimé avec succès'}
    else:
        return {'message': 'Utilisateur non trouvé'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5016)