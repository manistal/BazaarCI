
from . import create_app

if __name__ == "__main__":
    app = create_app(config="Production/LocalRun/etc")
    app.run()


