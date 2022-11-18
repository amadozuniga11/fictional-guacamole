from flask import Flask, render_template
app = Flask(__name__)

# Function to read in details for page
def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]



@app.route('/')
def homePage():
    name = "Amado Zuniga"
    details = readDetails('static/details.txt')
    return render_template("base.html", name = name, aboutMe = details)

@app.route('/profile')
def profile(): 
    profile_details = readDetails('static/profileDetails.txt')
    return render_template('profile.html',aboutMe=profile_details)
if __name__ == '__main__': 
    app.run(debug=True)
