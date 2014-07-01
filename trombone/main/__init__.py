from flask import request, flash, redirect, render_template

def root():
    return render_template('soon.html')
