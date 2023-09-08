from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api')
def api():
    slack_name = request.args.get('isommie')
    track = request.args.get('backend')
    current_day = datetime.utcnow().strftime('%A')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = 'https://github.com/username/repo/blob/main/app.py'
    github_repo_url = 'https://github.com/username/repo'
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
    app.run()
