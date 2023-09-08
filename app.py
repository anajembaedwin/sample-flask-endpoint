from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/api')
def api():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.utcnow().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = 'https://github.com/anajembaedwin/sample-flask-endpoint/blob/main/app.py'
    github_repo_url = 'https://github.com/anajembaedwin/sample-flask-endpoint'
    status_code = 200
    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': status_code
    }
    return jsonify(response)
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
