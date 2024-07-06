from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Jinja, Uganda',
    'salary': 'UGX. 1,500,000',
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Nairobi, Kenya',
    'salary': 'KSH. 500,000',
}, {
    'id': 3,
    'title': 'Front-End Engineer',
    'location': 'Dareslam, Tanzania',
    'salary': 'TSH. 250,000',
}, {
    'id': 4,
    'title': 'Back-End Engineer',
    'location': 'Kampala, Uganda',
    'salary': 'UGX. 2,500,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Logic-Labs')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
