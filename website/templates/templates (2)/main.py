"""
Run to start website
"""

from website import create_app

app = create_app()

if __name__ == '__main__':  # If we run this file only
    app.run(debug=True)  # Make false if to be released publically
