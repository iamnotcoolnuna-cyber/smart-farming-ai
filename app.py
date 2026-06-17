from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    chatbot_response = ""

    if request.method == "POST":

        if "predict" in request.form:

            soil = request.form["soil"]
            season = request.form["season"]

            if soil == "Loamy" and season == "Winter":
                prediction = "Wheat"

            elif soil == "Clay" and season == "Rainy":
                prediction = "Rice"

            elif soil == "Black" and season == "Summer":
                prediction = "Cotton"

            else:
                prediction = "Maize"

        elif "chat" in request.form:

            question = request.form["question"].lower()

            if "water" in question:
                chatbot_response = "Water crops early in the morning."

            elif "fertilizer" in question:
                chatbot_response = "Organic compost is recommended."

            elif "disease" in question:
                chatbot_response = "Inspect leaves regularly for pests."

            else:
                chatbot_response = "Please consult a local agriculture expert."

    return render_template(
        "index.html",
        prediction=prediction,
        chatbot_response=chatbot_response
    )

if __name__ == "__main__":
    app.run(debug=True)