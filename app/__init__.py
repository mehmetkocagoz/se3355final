from flask import Flask
from authlib.integrations.flask_client import OAuth

# Create a Flask application instance
app = Flask(__name__,static_url_path='/app/static')

app.config.update(
    OAUTH2_CLIENT_ID= "947748259257-m3m4rbtd91aa14pqlsheo61qihrq2nm4.apps.googleusercontent.com",
    OAUTH2_CLIENT_SECRET="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",
    OAUTH2_META_URL="https://accounts.google.com/.well-known/openid-configuration",
    FLASK_SECRET= "RandomString",
    FLASK_PORT= 8000
)


oauth = OAuth(app)

oauth.register(name="myApp",
               client_id = app.config.get('OAUTH2_CLIENT_ID'),
               client_secret = app.config.get('OAUTH2_CLIENT_SECRET'),
               server_metadata_url = app.config.get('OAUTH2_META_URL'),
               client_kwargs = {
                   "scope": "https://www.googleapis.com/auth/user.emails.read"
               })

# Import routes module to register the routes with the app
from app import routes