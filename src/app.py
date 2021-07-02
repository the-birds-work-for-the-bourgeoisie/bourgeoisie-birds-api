from flask import Flask, request, jsonify, abort
from database_access import get_highest_scores, insert_high_score
from validators import validate_data_keys, validate_initials, validate_score

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
@app.route('/wake-up', methods=['GET'])
def wake_up():
    """ Used to warm up the heroku server so the game's request will be faster later
    """
    return "Awake"

@app.route('/high-score', methods=['GET'])
def get_high_score():
    """ Returns an array of the highest high score data for displaying the score board
    """
    return jsonify(get_highest_scores())

@app.route('/high-score', methods=['PUT'])
def put_high_score():
    """ Inserts a score into the database and returns if there was an error
    """
    data = request.form.to_dict(flat=False)
    
    if not validate_data_keys(data, ["initials", "score"]):
        return jsonify({'errors': 'Invalid request body'}), 400
    
    initials = validate_initials(data["initials"][0])
    score = validate_score(data["score"][0])
    if initials is None or score is None:
        return jsonify({'errors': 'Invalid values for initials or score'}), 400
    
    if insert_high_score(score, initials):
        return jsonify({'message': 'inserted'})
    else:
        return jsonify({'message': 'not inserted'})

if __name__ == '__main__':
    app.run(debug=True)