from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/oauth/callback')
def oauth_callback():
    code = request.args.get("code")
    if code:
        print("✅ Authorization Code:", code)
        return render_template_string("""
            <h2 style="color: green;">✅ Authorization Code Received</h2>
            <p><b>Code:</b> {{ code }}</p>
            <p>You can now close this page and return to the app.</p>
        """, code=code)
    else:
        return render_template_string("""
            <h2 style="color: red;">❌ Authorization Failed</h2>
            <p>No code was returned. Please try again.</p>
        """)
