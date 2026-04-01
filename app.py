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


# from flask import Flask, jsonify, request
# from faker import Faker

# app = Flask(__name__)
# fake = Faker()

# @app.route('/api/users', methods=['GET'])
# def get_users():
#     # Get parameters from URL (default to page 1, 5 users per page)
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 5))
    
#     users = []
#     for _ in range(per_page):
#         users.append({
#             "id": fake.uuid4(),
#             "name": fake.name(),
#             "email": fake.email()
#         })
        
#     return jsonify({
#         "page": page,
#         "per_page": per_page,
#         "data": users,
#         "total": 100 # Example total
#     })
