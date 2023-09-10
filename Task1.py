
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, jsonify
#import datetime

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_info():

    #name = request.args.get('Matthias_Iyogun')
    #track = request.args.get('back_end')
    #offset = request.args.get('offset', type=int, default=0)

    #current_time = datetime.datetime.utcnow()
    #if abs(offset) > 2:
        #return jsonify({"error": "Offset must be between -2 and 2"}), 400

    #adjusted_time = current_time + datetime.timedelta(hours=offset)
    #current_day = adjusted_time.strftime('%A')
    response = {
        "slack_name": "Matthias_Iyogun",
        "current_day": "Sunday",
        "utc_time": "2023-09-10T16:01:05Z",
        "track": "backend",
        "github_file_url": ,
        "github_repo_url": ,
        "status_code": 200
    }
    return jsonify(response)
# if __name__ == '__main__':
    # app.run(debug=False)

