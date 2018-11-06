from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.API.Logger as log

@app.before_request
def before_request():
    g.logger = log.MyLogger.__call__().get_logger()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('PageNotFound.html'), 404