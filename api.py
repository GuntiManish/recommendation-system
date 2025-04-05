# api.py
from flask import Flask, request, jsonify
from recommender import recommend_assessments

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    query = data.get("query", "")
    if not query:
        return jsonify({"error": "Query is required."}), 400

    try:
        recommendations = recommend_assessments(query)
        return jsonify(recommendations), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
    