from halo import Halo
from waitress import serve
from flask import Flask, request, jsonify


def server(on_result):
    app = Flask(__name__)

    spinner = Halo(text='Waiting for browser authorization', spinner='dots')
    spinner.start()
    @app.route('/set-remote', methods=['POST'])
    def set_remote():
        spinner.stop()
        on_result(request.json.remote)
        return jsonify({'status': 'ok'})

    serve(app, host="0.0.0.0", port=54321)