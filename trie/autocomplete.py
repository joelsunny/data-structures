from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import jsonify
from flask_cors import CORS, cross_origin

app = FlaskAPI(__name__)
CORS(app)

import trie

@app.route('/autocomplete/<string:prefix>')
def autocomplete(prefix):
    if prefix == '':
        return {}
    list_words = t.find_prefix(prefix)
    dict_ = {}
    dict_["list"] = list_words
    return jsonify(dict_)

if __name__ == "__main__":
    t = trie.Trie()
    t.add_string("sea")
    t.add_string("string")
    t.add_string("store")
    t.add_string("stream")
    app.run(debug=False)