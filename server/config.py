import os

BASE_URL = ''

FOLLOWERS_THRESHOLD = 10000

NODE2VEC_MODEL_PATTERN = './data/interaction_node2vec_{}.model'
NODE2VEC_MODEL_PATH = NODE2VEC_MODEL_PATTERN.format(FOLLOWERS_THRESHOLD)

USER_NAME2DATA_PATTERN = './data/interaction_{}_user_name2data.json'
USER_NAME2DATA_PATH = USER_NAME2DATA_PATTERN.format(FOLLOWERS_THRESHOLD)
USER_ID2DATA_PATTERN = './data/interaction_{}_user_id2data.json'
USER_ID2DATA_PATH = USER_ID2DATA_PATTERN.format(FOLLOWERS_THRESHOLD)

VIEW_FOLDER = os.path.abspath('./view')

RESULT_NODES_NO = 20
