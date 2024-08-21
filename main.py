from flask import Flask, render_template, request, jsonify
import os, re
import csv
import time
import pandas as pd 


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def get_route():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')


    










  

@app.route('/getanswer', methods=['POST','GET'])
def post_route():
    if request.method == 'POST':
        que=request.form['question']
        print(que)
        #data=runmain(que)   
        #txt="1. For a Requester, the login page contains only the Accounts page & Requests page.\n2. The Accounts page displays all the available managed accounts & managed devices.\n3. The Requests page displays all the Active, Pending, Cancelled, and Expired requests.\n4. For an Approver (Requester Approver), the login page contains the Accounts page, Requests page, and an Approve page.\n5. The Approve page displays requests that are pending approval by the Approver."
        # txt="""For a Requester:\n1. Accounts - Displays all the available managed accounts & managed devices.\n2. Requests - Displays all the Active, Pending, Cancelled, and Expired requests.\nFor an Approver (Requester Approver):\n1. Accounts - Displays all the available managed accounts & managed devices.\n2. Requests - Displays all the Active, Pending, Cancelled, and Expired requests.\n3. Approve - Displays requests which requesters are pending for approval."""
        txt="""2.1 Enter the Okta URL (https://genpact.okta-emea.com/) in the browser (Edge/Chrome is recommended)\n2.2 Log in with OHR ID & Password in okta\n2.3 After successful login to okta, Add PAM-AWS app from Genpact Apps https://genpact.okta-emea.com/ and click on the tile as shown below.\n2.4 Upon clicking on the PAM-AWS, user will be redirected to enter Passcode or send Push notification.\n2.5 Once the passcode or Push notification authentication is done user will be Redirected to PAM (Beynndtrust) web portal."""
        # txt="This is my tweet check it out http://tinyurl.com/blah"
        return jsonify({'message': txt}) 
    
@app.route('/dislikeresponse', methods=['POST'])
def write_to_first_csv():
    usermassage = request.form['usermassage']
    botresponse = request.form['botresponse']
    TimeStampQuery = ''
    TimeStampResponse=''
    Username=''
    csv_file_path = "thumbs_down_log.csv"
    file_exists = os.path.isfile(csv_file_path)
    with open(csv_file_path, mode='a', newline='') as f:
        fieldnames = ['TimeStampQuery','TimeStampResponse','Question', 'Answer','Username']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
    with open(csv_file_path, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'TimeStampQuery': TimeStampQuery,'TimeStampResponse':TimeStampResponse, 'Question': usermassage, 'Answer': botresponse,'Username':Username})
    return jsonify({'msg':'success'})

@app.route('/likeresponse', methods=['POST'])
def write_to_second_csv():
    usermassage = request.form['usermassage']
    botresponse = request.form['botresponse']
    TimeStampQuery = ''
    TimeStampResponse=''
    Username=''
    csv_file_path = "thumbs_up_log.csv"
    file_exists = os.path.isfile(csv_file_path)
    with open(csv_file_path, mode='a', newline='') as f:
        fieldnames = ['TimeStampQuery','TimeStampResponse','Question', 'Answer','Username']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
    with open(csv_file_path, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'TimeStampQuery': TimeStampQuery,'TimeStampResponse':TimeStampResponse, 'Question': usermassage, 'Answer': botresponse,'Username':Username})
    return jsonify({'msg':'success'})





if __name__ == '__main__':
    app.run(debug=True)
