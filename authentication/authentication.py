from flask import Flask, redirect, session, url_for, make_response

from authlib.integrations.flask_client import OAuth
import os
import psutil

from prometheus_client import generate_latest, Counter, Gauge

# AUTH0_CLIENT_ID="oyp940gN2eaffEZjgdHvFKSCfprngFmY"
# AUTH0_CLIENT_SECRET="_bb5JwYk_enfIaVrWt9kKqLDcwWSKAt--zLDHJAZOULdrnMwmrgtjD3FJhITSRAz"
# AUTH0_DOMAIN="dev-yq8vieybb3gnrzif.eu.auth0.com"
APP_SECRET_KEY = os.getenv("APP_SECRET_KEY")

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")

app = Flask(__name__)
app.secret_key = APP_SECRET_KEY
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{AUTH0_DOMAIN}/.well-known/openid-configuration'
)

# metrics
request_counter = Counter("requests_counter_authentication", "Total number of requests of authentication")
cpu_usage = Gauge('cpu_usage_percent_authentication', 'CPU Usage Percentage of authentication')
memory_usage = Gauge('memory_usage_percent_authentication', 'Memory Usage Percentage of authentication')


@app.route("/api/authentication/see_id")
def see_token():
    request_counter.inc(1)
    response = make_response()
    response.set_cookie("user_id", session["user"]["userinfo"]["sub"])
    return response


@app.route("/api/authentication/login")
def login():
    request_counter.inc(1)
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    request_counter.inc(1)
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/api/authentication/see_id")


@app.route("/api/authentication/liveness-check", methods=['GET'])
def liveness_check():
    return "ok", 200


@app.route("/metrics", methods=['GET'])
def prometheus_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)
    return generate_latest()
