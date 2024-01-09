import pathlib
from flask import Flask
from google_auth_oauthlib.flow import Flow
import os
from dotenv import load_dotenv

load_dotenv()
# Create a Flask application instance
app = Flask(__name__,static_url_path='/app/static')

app.config.update(
    OAUTH2_CLIENT_ID= os.environ.get('OAUTH2_CLIENT_ID'),
    OAUTH2_CLIENT_SECRET=os.environ.get('OAUTH2_CLIENT_SECRET'),
    OAUTH2_META_URL="https://accounts.google.com/.well-known/openid-configuration",
    FLASK_SECRET= "RandomString",
    FLASK_PORT= 8000
)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

client_secrets_file = os.path.join(pathlib.Path(__file__).parent,"client_secret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/user.birthday.read","https://www.googleapis.com/auth/userinfo.profile"],
    redirect_uri="https://se335finalapp.azurewebsites.net/.auth/login/google/callback")


# Import routes module to register the routes with the app
from app import routes