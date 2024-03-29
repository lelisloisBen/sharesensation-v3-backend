import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '57e19ea558d4967a552d03deece34a70'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE2_URL')
    
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')
    
    # Social Auth
    OAUTH_CREDENTIALS = {
        'google': {
            'id': os.environ.get('GOOGLE_CLIENT_ID'),
            'secret': os.environ.get('GOOGLE_CLIENT_SECRET'),
        },
        'facebook': {
            'id' : os.environ.get('FACEBOOK_CLIENT_ID'),
            'secret': os.environ.get('FACEBOOK_CLIENT_SECRET'),
        },
        'twitter': {
            'id': os.environ.get('TWITTER_API_ID'),
            'secret': os.environ.get('TWITTER_API_SECRET'),
        }
    }

    S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
    S3_KEY = os.environ.get("AWS_ACCESS_KEY")
    S3_SECRET = os.environ.get("AWS_ACCESS_SECRET")
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

class ProductionConfig(Config):
    DEBUG = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FRONTEND_URL = 'https://sharesensation.herokuapp.com'
    BACKEND_URL = 'https://sharesensation-backend.herokuapp.com'
    STRIPE_PRIVATE_KEY = os.environ.get('STRIPE_PRIVATE_KEY')

class DevelopmentConfig(Config):
    ENV="development"
    DEVELOPMENT=True
    DEBUG=True
    MAIL_SERVER = '127.0.0.1'
    MAIL_PORT = 1025
    FRONTEND_URL = 'http://localhost:3000'
    BACKEND_URL = 'http://localhost:5000'
    STRIPE_PRIVATE_KEY = 'sk_test_51LoqOoLLg3TVYJvXgwBcfOqs0jdvtbOApWJJpq1CcAJYABcQNhrrYkdcZbXFvNssKON9uNF3ebyVVMZoaTWSUhpm00f4YkrsOl'
    