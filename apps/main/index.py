from blueprints import main
from flask import redirect, render_template,request, session, json,jsonify, url_for
from datetime import datetime as dt, timezone,timedelta
import traceback

try:
    @main.route('/home')
    def home():
        return render_template("/base.html")
except Exception as e:
    raise e
    