from server.gll_node2vec import load_model
from server.gll_node2vec import load_user_data
from server.gll_node2vec import get_similar_node
from server.gll_node2vec import get_likely_be_mentioned
from server.gll_node2vec import get_likely_mention
from server.config import VIEW_FOLDER, BASE_URL
from server.config import USER_ID2DATA_PATH, USER_NAME2DATA_PATH
from flask import Flask, jsonify, redirect
import os


model = load_model()
user_name2data = load_user_data(USER_NAME2DATA_PATH)
user_id2data = load_user_data(USER_ID2DATA_PATH)

app = Flask(__name__, static_folder=os.path.abspath(VIEW_FOLDER))


@app.route(BASE_URL + '/')
def index():
    return redirect(BASE_URL + '/file/main.html')


@app.route(BASE_URL + '/file/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


@app.route(BASE_URL + '/get_nodes/<nodes_type>/<node_name>')
def query_nodes(nodes_type, node_name):
    node_id = str(user_name2data[node_name.lower()]['id'])

    if nodes_type == 'similarity':
        nodes = get_similar_node(model, node_id)
    elif nodes_type == 'mention':
        nodes = get_likely_mention(model, node_id)
    elif nodes_type == 'mentioned':
        nodes = get_likely_be_mentioned(model, node_id)
    else:
        nodes = get_similar_node(model, node_id)

    nodes_data = []
    for n in nodes:
        nodes_data.append(user_id2data[n[0]])

    print(nodes_type, node_name)
    res = {'nodes_type': nodes_type,
           'node_name': node_name,
           'data': nodes_data}
    return jsonify(res)


app.run(port=8009, host='0.0.0.0')
