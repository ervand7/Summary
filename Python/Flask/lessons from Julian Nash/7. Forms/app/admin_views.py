from . import app
from flask import render_template


@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/dashboard.j2')


@app.route('/admin/profile')
def admin_profile():
    return "Admin profile"
