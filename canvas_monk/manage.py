from application import Application
from werkzeug import script

def make_app():
    return Application()

def main():
    action_runserver = script.make_runserver(make_app, use_reloader=True)
    script.run()


if __name__ == "__main__":
    main()
