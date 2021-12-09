import re
from flask import Flask, send_from_directory, Response
from livereload import Server, shell
from ua_server import Config, mimeutils
import os
import json

config = Config()

#app = Flask(__name__,static_url_path="/",static_folder=config.getStaticWebDir())
app = Flask(__name__)

@app.route('/', defaults={'filename': 'index.html'})
@app.route("/<path:filename>")
def serve_static(filename: str):
    return send_from_directory(config.getStaticWebDir(),filename)


@app.route("/api/files")
def list_files():
    fileMap = config.getDataFiles()
    paths = []
    for path in fileMap.keys():
        paths.append(f"/api/files{path}")
    result = json.dumps(paths)
    return Response(result, mimetype="application/json")

@app.route("/api/files/<path:filename>")
def get_file(filename :str):
    adjustedPath = os.path.join(os.path.sep, filename)
    mimetype = mimeutils.mime_type_for_file(adjustedPath)
    fileMap = config.getDataFiles()
    fullPath = fileMap.get(adjustedPath);
    if fullPath != None:
        def stream():
            with open(fullPath) as file:
                chunk = file.read(4096)
                while chunk:
                    yield chunk
                    chunk = file.read(4096)
        return app.response_class(stream(), mimetype=mimetype)
    else:
        return app.response_class("unable to read file", status=500)


if __name__ == '__main__':
    # Run our web server
    app.debug = True
    server = Server(app.wsgi_app)
    npm_watch_dir = config.get("ClientSource", "basedir")
    web_dir = config.get("Paths", "web_dir")
    npm_watch_dir = os.path.join(npm_watch_dir,"**/*")
    print(f"npm watch dir: {npm_watch_dir}")
    server.watch(npm_watch_dir, shell('npm run build', cwd=web_dir))
    server.serve(port=5000, restart_delay=2, debug=True)
