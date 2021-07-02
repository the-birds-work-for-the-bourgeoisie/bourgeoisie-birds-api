from flask import Flask, request, jsonify, abort
from validators import validate_data_keys, validate_initials, validate_score

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
@app.route('/wake-up', methods=['GET'])
def wake_up():
    return "Awake"

@app.route('/high-score', methods=['PUT'])
def high_score():
    data = request.form.to_dict(flat=False)
    if validate_data_keys(data, ["initials", "score"]):
        initials = validate_initials(data["initials"][0])
        score = validate_score(data["score"][0])
        if initials is not None and score is not None:
            return jsonify(initials)
    abort(400)

if __name__ == '__main__':
    app.run(debug=True)