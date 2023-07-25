from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=5000)

@app.route("/")
def index():
    redis.incr('hits')
    counter = str(redis.get,'utf-8')
    return "Welcome to LegionDev, We have totall viewrs "+counter+""

if __name__=="__main__":
    app.run(debug=True, host=0.0.0.0)