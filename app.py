from flask import Flask, render_template, request, jsonify
from game import play_round

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    result_data = play_round(user_choice)

    if "error" in result_data:
        return jsonify({"error": result_data["error"]})

    return jsonify({
        "computer_choice": result_data["computer"].lower(),  # Ensure lowercase filenames
        "result": result_data["result"]
    })

if __name__ == '__main__':
    app.run(debug=True)
