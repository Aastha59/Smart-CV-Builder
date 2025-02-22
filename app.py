# from flask import Flask, render_template
# import os
# import datetime
# import subprocess
# import getpass

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("main.py")

# @app.route("/htop")
# def htop():
#     name = "Aastha"  # Replace with your full name
#     try:
#         username = getpass.getuser()  # More reliable in a remote environment
#     except Exception:
#         username = "Unknown (running as a service)"

#     # Get server time in IST
#     ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
#     time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

#     # Get top command output
#     try:
#         top_output = subprocess.getoutput("top -b -n 1 | head -20")
#     except Exception as e:
#         top_output = f"Error fetching top output: {str(e)}"

#     response = f"""
#     <h1>System Info</h1>
#     <p><strong>Name:</strong> {name}</p>
#     <p><strong>Username:</strong> {username}</p>
#     <p><strong>Server Time (IST):</strong> {time_str}</p>
#     <pre>{top_output}</pre>
#     """
#     return response

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000, debug=True)



from flask import Flask, render_template_string
import os
import datetime
import subprocess
import getpass

app = Flask(__name__)

@app.route("/")
def home():
    try:
        output = subprocess.getoutput("python3 main.py")  # Run main.py and get output
    except Exception as e:
        output = f"Error executing main.py: {str(e)}"

    return render_template_string(f"<h1>Main.py Output</h1><pre>{output}</pre>")  # Show output in browser

@app.route("/htop")
def htop():
    name = "Aastha"  # Replace with your full name
    try:
        username = getpass.getuser()  # More reliable in a remote environment
    except Exception:
        username = "Unknown (running as a service)"

    # Get server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    time_str = ist_time.strftime('%Y-%m-%d %H:%M:%S IST')

    # Get top command output
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        top_output = f"Error fetching top output: {str(e)}"

    response = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {time_str}</p>
    <pre>{top_output}</pre>
    """
    return render_template_string(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

