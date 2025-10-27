from app.routes.user import app

if __name__ == '__main__':
    app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
    app.run()
