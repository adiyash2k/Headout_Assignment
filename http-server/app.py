from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name:
        file_path = f'/tmp/data/{file_name}.txt'

        if os.path.exists(file_path):
            if line_number:
                try:
                    with open(file_path, 'r') as file:
                        lines = file.readlines()
                        line_number = int(line_number)
                        if 1 <= line_number <= len(lines):
                            return jsonify({'content': lines[line_number - 1].strip()})
                        else:
                            return jsonify({'error': 'Invalid line number'})
                except ValueError:
                    return jsonify({'error': 'Invalid line number'})
            else:
                with open(file_path, 'r') as file:
                    content = file.read()
                    return jsonify({'content': content})
        else:
            return jsonify({'error': 'File not found'})
    else:
        return jsonify({'error': 'File name not provided'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
