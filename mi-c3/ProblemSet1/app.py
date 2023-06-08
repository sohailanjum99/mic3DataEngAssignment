from datetime import datetime
from flask import Flask, request, jsonify
import os 

app = Flask(__name__)



@app.route('/calculate_time_diff', methods=['POST'])
def calculate_time_diff():
    try:
        text_data = request.get_data().decode('utf-8')
        if not text_data:
            return jsonify({'error': 'Invalid input'}), 400

        text_data = text_data.replace('\r', '')  # Remove carriage return characters

        timestamps = text_data.strip().split('\n')
        if len(timestamps) % 2 != 0:
            return jsonify({'error': 'Invalid number of timestamps'}), 400

        time_diffs = []

        for i in range(0, len(timestamps), 2):
            time1 = datetime.strptime(timestamps[i], "%a %d %b %Y %H:%M:%S %z")
            time2 = datetime.strptime(timestamps[i + 1], "%a %d %b %Y %H:%M:%S %z")
            diff = int(abs((time1 - time2).total_seconds()))
            time_diffs.append(diff)

        node_id = os.environ.get('HOSTNAME')


        response = {
            'id': node_id,
            'result': time_diffs
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/', methods=['GET'])
def Hello():
    return {   'Hello': 'World'   }


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


