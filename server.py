from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyse = request.args.get("textToAnalyze")

    if text_to_analyse is None or text_to_analyse.strip() == "":
        return "Invalid input! Try again."

    result = emotion_detector(text_to_analyse)

    if result is None or result["dominant_emotion"] is None:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)