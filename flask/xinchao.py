from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def xinchào():
    return 'xin chào mọi người!,nkkbavlnhczbxnbcdccctclsndavhnvl'
 
if __name__ == '__main__':
    app.run()
