from flask import request, flash, redirect, render_template

def root():
    return render_template('soon.html')

def main():
    return render_template('root.html')

def answers():
    return render_template('answers.html')
