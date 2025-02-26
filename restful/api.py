from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据库
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

# 获取所有用户
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# 获取单个用户
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 创建新用户
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = {"id": len(users) + 1, "name": data["name"]}
    users.append(new_user)
    return jsonify(new_user), 201

# 运行服务器
if __name__ == '__main__':
    app.run(debug=True)
