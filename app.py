from flask import Flask, jsonify
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    for _ in range(10): # Generates 10 users
        users.append({
            "id": fake.uuid4(),
            "name": fake.name(),
            "email": fake.email(),
            "city": fake.city()
        })
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
