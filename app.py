# -*- coding:utf-8 -*-

from flask import Flask, render_template
import pandas as pd
import pymssql
import re

# Visible rows limit
rows_limit = 5000

# MS SQL server configuration
server = "localhost\FOSS_FI"
user = ""
password = ""
base = "test_base"

app = Flask(__name__)

@app.route("/")
def show_index():
    # Prepare html code for the table
    html = df.head(rows_limit).to_html(classes = 'example', border = 0, index = False)
    html = re.sub(' example', '" id = "example', html)
    return render_template('index.html', table = html)

if __name__ == "__main__":
    
    # Retreive MS SQL data
    conn = pymssql.connect(server, user, password, base)
    df = pd.read_sql("select * from consumer_complaints", con = conn)
    conn.close()
    
    # Remove empty or equal filled columns
    df.drop('consumer_complaint_narrative', axis = 1, inplace = True)
    df.drop('company_public_response', axis = 1, inplace = True)
    df.drop('consumer_consent_provided', axis = 1, inplace = True)
    
    # Run the app with enabled debug
    app.run(debug = True)