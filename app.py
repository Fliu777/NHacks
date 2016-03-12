from flask import Flask, render_template #alrighty team here we go
app = Flask(__name__) #creates flask app 

@app.route("/") #ignore this this is flask magic


def main():
    return render_template('index.html') #display the site

if __name__ == "__main__":
    app.run()

