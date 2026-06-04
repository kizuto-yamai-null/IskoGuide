"""
IskoGuide Application Gateway Entry Point
Executes the local thread server configuration for web service rendering.
"""

from website import create_app

app = create_app()

if __name__ == '__main__':
    # Initialize the web thread environment locally on port 5000
    app.run(debug=True)