from flask import Flask

app = Flask("CineReserve")

def main():
    app.run(
        host="0.0.0.0",
        port=82,
        debug=True
    )

if __name__ == "__main__":
    main()