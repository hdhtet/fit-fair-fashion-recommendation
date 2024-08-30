from flask import Flask, request, render_template
import image_embedding as ie

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    """ index page """
    return render_template("home.html")


@app.route("/body-type-guide")
def information():
    """ display body type guide information page """
    return render_template("information.html")


@app.route("/choose-body-type", methods=['GET', 'POST'])
def choose_body_type():
    """ choose body type - get text input """
    if request.method == 'POST':
        bodytype = request.form.get('bodytype')
        return render_template("decision.html", bodytype=bodytype)
    else:
        return render_template("choosebody.html")


@app.route("/formal-clothes", methods=['GET', 'POST'])
def formal_clothes():
    """ display formal clothes based on body shape """
    if request.method == 'POST':
        bodyshape = request.form.get('bodytype')
        style = request.form.get('style')
        input_text = bodyshape + " " + style
        print(input_text)
        model = ie.model
        processor = ie.processor
        retrieved_images = ie.retrieve_images_for_query_random(
            model, processor, input_text, top_k=10, top_limit=4, bottom_limit=4, temperature=1.0)
        return render_template("formal.html", clothes=retrieved_images, bodyshape=bodyshape)


@app.route("/casual-clothes", methods=['GET', 'POST'])
def casual_clothes():
    """ display causal clothes based on body shape """
    if request.method == 'POST':
        bodyshape = request.form.get('bodytype')
        style = request.form.get('style')
        input_text = bodyshape + " " + style
        print(input_text)
        model = ie.model
        processor = ie.processor
        retrieved_images = ie.retrieve_images_for_query_random(
            model, processor, input_text, top_k=10, top_limit=4, bottom_limit=4, temperature=1.0)
        return render_template("casual.html", clothes=retrieved_images, bodyshape=bodyshape)
    else:
        return render_template("casual.html")


@app.route("/login")
def login():
    """ login page, not implemented yet """
    return render_template("login.html")


@app.route("/register")
def register():
    """ register page, not implemented yet """
    return render_template("register.html")


@app.route("/analyze-with-ai")
def ai_analysis():
    """ to analyze body shape with AI by uploading body image """
    return render_template("ai-analysis.html")


if __name__ == "__main__":
    app.run(debug=True)
