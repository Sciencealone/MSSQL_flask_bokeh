# -*- coding:utf-8 -*-

from flask import Flask, render_template
import pandas as pd
import pymssql
import re
from bs4 import BeautifulSoup

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
    html = df.head(rows_limit).to_html(classes = 'display example', border = 0, index = False)
    
    # Fix some formatting issues
    html = re.sub(' example', '" id = "example', html)
    html = re.sub(' style="text-align: right;"', '', html)
    
    # Prepare a fake footer for the select boxes
    soup = BeautifulSoup(html, "lxml")
    thead = str(soup.find('thead').findChildren()[0])
    html = re.sub(r'</thead>', r'</thead><tfoot>' + thead + '</tfoot>', html)
    
    return render_template('index.html', table = html)

if __name__ == "__main__":
    
    # Retreive MS SQL data
    conn = pymssql.connect(server, user, password, base)
    df = pd.read_sql("select * from Camera", con = conn)
    conn.close()
    
    # Run the app with enabled debug
    app.run(debug = True)