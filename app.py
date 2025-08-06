from flask import Flask, render_template, url_for, jsonify
#image ko load karne ke liye templates se url_for ko import karna padega
# Create a Flask web application instance ya variable jisme flask application load hogi ye deployment ke vakt gunicorn app:app :- app.py:name of variable
app = Flask(__name__)

# data kisi aur jagah hota database mei hamne yha par dynamically data ko render kiya hai
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Delhi, India',
    'salary': 'Rs 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Remote',
    'salary': 'Rs 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Delhi, India',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Banglore',
    'salary': 'R$ 120,000'
}]


# Define a route for the route URL ("/")
@app.route("/")
def hello_world():
    # return render_template(Home.html)
    return render_template("Home.html", jobs=JOBS, company_name='Jovian')

    # some website allows access to dynamic data using API
    # Json is simply JavaScript objects


@app.route("/api/jobs")  # is function ko register karna padega at route(Second route or URL) & JOBs information ko lenge aur convert karenge into JSON String :- jsonify(helper function) ko import(or call) karna isko
def list_jobs():
    return jsonify(JOBS)  #jsonify takes any object and converts into a json object


# when people say rest API or Json API or API endpoint this is what they mean that your server is returning some information not just as HTML(HTML version of that information) but the same information is also accessible in the form of Json in the form where it's just the data and then u can do whatever u want with the data
print("Hello flask")
# Run the application if this script is executed directly
# programatically extraction data of thousand user then u can simply invoke this Json endpoint or Json route and get all data structured in the form of Json and maybe create a CSV out of it and Analyze it
# information database se bhi aa saki yha par JOBS se aa rha hai
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    print("I am inside if")
print(__name__)

# requirement.txt file mei ham jo library isme import karenge vo dalaenge kyunki render.com ko pata nahi hai ki isko install karne ki jarurat hai
# gunicorn ek production server hai for python when python says its for devlopment server not for production use isko use karke ham flask application ko production mei laate hai
# pip ek package manager hai for python it is used to install liberaries in Python & u are just telling pip look into the requirements.txt file in each line there will be name of the liberary and plz install that liberary for me
