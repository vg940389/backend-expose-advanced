"""Example of flask main file."""
from flask import Flask
app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('whitelabel.html', error_code=404, message="Page Not Found"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('whitelabel.html', error_code=500, message="Internal Server Error"), 500

@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


if __name__ == '__main__':
    app.run()
