

def test_login(app):
    app.session.login("administrator", "root")
    print(app.session.is_logged_in_as("administrator"))
