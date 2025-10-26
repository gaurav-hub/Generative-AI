"""
HugAI Connect SmartSheet Integration

This module provides a Flask application for OAuth authentication with SmartSheet, enabling integration with SmartSheet APIs for reading and writing sheets.

Functions:
    index(): Displays the home page with a login link.
    login(): Initiates the OAuth login flow with SmartSheet.
    callback(): Handles the OAuth callback and retrieves the access token.

Usage:
    Run this script to start the Flask server for SmartSheet integration.
"""

import os
import uuid
import requests
from flask import Flask, redirect, request, session, jsonify, abort

app = Flask(__name__)
# Use a fixed secret key for testing purposes
app.secret_key = 'vu1cpu1qnqacitdmgl1'

# Replace these with your actual SmartSheet app credentials
CLIENT_ID = "c38gwi13siuehnini40"
CLIENT_SECRET = "h3mehk68z1w0wudysev"
REDIRECT_URI = "https://ascendgenai-eu.deloitte.com"

SCOPE = "READ_SHEETS WRITE_SHEETS"

AUTHORIZATION_URL = "https://app.smartsheet.eu/b/authorize"
TOKEN_URL = "https://api.smartsheet.eu/2.0/token"

@app.route('/')
def index():
    return """
    <h2>Welcome to the SmartSheet & AIP Integration!</h2>
    <p><a href="/login">Click here to login with SmartSheet</a></p>
    """

@app.route('/login')
def login():
    # Generate a random state string for CSRF protection
    state = str(uuid.uuid4())
    session['oauth_state'] = state

    # Log for debugging:
    app.logger.info("Generated state: %s", state)

    # Build the authorization URL using the required parameters including scope
    params = {
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'state': state,
        'scope': SCOPE
    }
    request_url = requests.Request('GET', AUTHORIZATION_URL, params=params).prepare().url
    return redirect(request_url)

@app.route('/callback')
def callback():
    error = request.args.get('error')
    if error:
        return f"Error during authorization: {error}", 400

    code = request.args.get('code')
    state = request.args.get('state')

    # Log for debugging:
    app.logger.info("Returned state: %s", state)
    app.logger.info("Stored state in session: %s", session.get('oauth_state'))

    #if state != session.get('oauth_state'):
    #    return "Error: State parameter does not match", 400

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    token_response = requests.post(TOKEN_URL, data=data, headers=headers)
    if token_response.ok:
        token_data = token_response.json()
        return jsonify(token_data)
    else:
        return f"Failed to retrieve access token: {token_response.text}", 400

if __name__ == '__main__':
    app.run(debug=True)