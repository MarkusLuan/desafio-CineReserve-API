from flask import Flask

from .error_handler import ErrorHandler

app = Flask("CineReserve")
ErrorHandler(app)

def main():
    app.run(
        host="0.0.0.0",
        port=82,
        debug=True
    )

if __name__ == "__main__":
    main()