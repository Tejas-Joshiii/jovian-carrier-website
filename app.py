from flask import Flask, render_template, url_for, jsonify
        #image ko load karne ke liye templates se url_for ko import karna padega 
        # Create a Flask web application instance
app = Flask(__name__)

    # data kisi aur jagah hota database mei hamne yha par dynamically data ko render kiya hai  
JOBS = [
        {
            'id':1,
            'title':'Data Analyst',
            'location':'Delhi, India',
            'salary':'Rs 10,00,000'
        },
        {
            'id':2,
            'title':'Data Scientist',
            'location':'Remote',
            'salary':'Rs 15,00,000'
        },
        {
            'id':3,
            'title':'Frontend Engineer',
            'location':'Delhi, India',
        },
        {
            'id':4,
            'title':'Backend Engineer',
            'location':'Banglore',
            'salary':'R$ 120,000'
        }
    ]
        # Define a route for the route URL ("/")
@app.route("/")
def hello_world():
        # return render_template(Home.html)
    return render_template("Home.html",jobs=JOBS,company_name='Jovian')

        # some website allows access to dynamic data using API 
        # Json is simply JavaScript objects

@app.route("/jobs") # is function ko register karna padega at route(Second route or URL) & JOBs information ko lenge aur convert karenge into JSON String :- jsonify(helper function) ko import(or call) karna isko 
def list_jobs():
    return jsonify(JOBS)

print("Hello flask")
        # Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    print("I am inside if") 
print(__name__)    