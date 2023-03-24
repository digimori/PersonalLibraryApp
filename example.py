import os

os.environ.setdefault("IP", "0.0.0.0")  # Local IP
os.environ.setdefault("PORT", "5000")  # This is the port for Flask
os.environ.setdefault("SECRET_KEY", "Any secret key")
os.environ.setdefault(
    "MONGO_URI",
    "mongodb+srv://root:<password>@<cluster_name>.ixpv5wd.mongodb.net/<database_name>?retryWrites=true&w=majority"
)
os.environ.setdefault("MONGO_DBNAME", "<database_name>")
