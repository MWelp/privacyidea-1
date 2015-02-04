import os
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = "/".join(basedir.split("/")[:-1]) + "/"

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQL_ALCHEMY_DATABASE_URI = "mysql://privacyidea:XmbSrlqy5d4IS08zjz"
    # "GG5HTt40Cpf5@localhost/privacyidea"
    PI_ENCFILE = os.path.join(basedir, "tests/testdata/enckey")
    PI_HSM = "default"
    PI_AUDIT_MODULE = "privacyidea.lib.auditmodules.sqlaudit"
    PI_AUDIT_KEY_PRIVATE = os.path.join(basedir, "tests/testdata/private.pem")
    PI_AUDIT_KEY_PUBLIC = os.path.join(basedir, "tests/testdata/public.pem")
    # PI_AUDIT_SQL_URI = sqlite://


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    # This is used to encrypt the auth token
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    # This is used to encrypt the admin passwords
    PI_PEPPER = ""
    # This is only for testing encrypted files
    PI_ENCFILE_ENC = "tests/testdata/enckey.enc"


class ProductionConfig(Config):
    config_path = basedir
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(config_path, 'data.sqlite')
    #SQLALCHEMY_DATABASE_URI = "mysql://pi2:pi2@localhost/pi2"
    # This is used to encrypt the auth_token
    SECRET_KEY = os.environ.get('SECRET_KEY') or 't0p s3cr3t'
    # This is used to encrypt the admin passwords
    PI_PEPPER = "Never know..."
    # This is used to encrypt the token data and token passwords
    PI_ENCFILE = os.path.join(config_path, "enckey")
    # This is used to sign the audit log
    PI_AUDIT_KEY_PRIVATE = os.path.join(config_path, "private.pem")
    PI_AUDIT_KEY_PUBLIC = os.path.join(config_path, "public.pem")


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
