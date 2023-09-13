#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <div style='text-align:center;margin-top:150px'>
        <h2>Please Enter the Input and it will Produce What you Entered</h2>
   
        <form action="/echo_user_input" method="POST">
            <input name="user_input">
            <input type="submit" value="Submit!">
        </form>
    </div>
 
     '''


@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return f'''
    <div style='text-align:center;margin-top:150px'>
        <h2>You entered: {input_text}</h2>
    </div>

    '''
