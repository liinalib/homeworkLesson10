from flask import Flask
import utils

app = Flask(__name__)

@app.route("/")
def index():
    result = '<br>'
    candidates = utils.get_candidates_all()

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'

@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)

    if candidate == 'Not Found':
        return candidate

    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'

    print(candidate['picture'])

    return f"""
        <img src = "{candidate['picture']}">
        <pre> {result} </pre>
    """

@app.route("/candidate/<skill>")
def get_candidate_by_skill(skill):
    result = '<br>'
    candidates = utils.get_candidates_by_skill(skill)

    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'

    return f'<pre> {result} </pre>'

app.run(debug = True)