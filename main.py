from flask import Flask, render_template, request, flash, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return "works"#render_template("homepage.html")



if __name__ == '__main__':
   app.run()