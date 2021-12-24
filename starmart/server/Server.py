from waitress import serve
from flask import Flask, request, jsonify


def server(on_result):
    app = Flask(__name__)

    @app.route('/set-remote', methods=['POST'])
    def set_remote():
        on_result(request.json.remote)
        return jsonify({'status': 'ok'})

    serve(app, host="0.0.0.0", port=54321)
