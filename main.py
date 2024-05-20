from flask import Flask, jsonify, request
import json
from model.post import Post

posts = []
ids = 0
app = Flask(__name__)


class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return {"id": obj.id, "body": obj.body, "author": obj.author}
        else:
            return super().default(obj)

app.json_encoder = MyJSONEncoder

@app.route('/post/', methods=['POST'])              #Создаем пост {"body": "Post2", "author": "Name2"}
def create_post():
    global ids
    ids += 1
    post = {
        "body": request.json["body"],
        "author": request.json["author"],
        "id": int(ids)
    }
    posts.append(post)
    return f"Пост с id {ids} создан"

@app.route('/post/<int:id>', methods=['POST'])      #Создаем пост по id
def create_id_post(id):
    post = {
        "body": request.json["body"],
        "author": request.json["author"],
        "id": int(id)
    }
    posts.append(post)
    return f"Пост с id {id} создан"

@app.route('/post/<int:id>', methods=['DELETE'])    #Удаляем пост по id
def delete_post(id):
    post = list(filter(lambda x: x['id'] == id, posts))
    if len(post) == 0:
        return f"Пост с {id} не найден"
    posts.remove(post[0])
    return f"Пост с id {id} удален"

@app.route('/post/<int:id>', methods=['PUT'])       #Обновляем пост по id
def put_post(id):
    post = list(filter(lambda x: x['id'] == id, posts))
    if len(post) == 0:
        return f"Пост с id {id} не найден"
    else:
        ind = posts.index(post[0])
        posts[ind]["body"] = request.json["body"]
        posts[ind]["author"] = request.json["author"]
        return f"Студент с id {id} обновлен"

@app.route('/post/<int:id>', methods=['GET'])       #Возвращаем пост по id
def get_id_post(id):
    post = list(filter(lambda x: x['id'] == id, posts))
    return jsonify(post[0])

@app.route('/post/', methods=['GET'])               #Возвращаем все посты
def get_post():
    return jsonify(posts)


if __name__ == '__main__':
    app.run(debug=True)