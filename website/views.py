import json

from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import *
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note_text = request.form.get("note")
        user_id = current_user.id
        if len(note_text) < 1:
            flash("Add a good note please", category="error")
        else:
            note = Note(note=note_text, user_id=user_id)

            db.session.add(note)
            db.session.commit()
            flash("Note created successfully", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    note_id = note["noteId"]
    note = Note.query.get(note_id)

    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})


@views.route("/edit-note/<int:id>", methods=["GET", "POST"])
@login_required
def edit_note(id):
    note = Note.query.get(id)
    if note:
        if current_user.id == note.user_id:
            pass
        else:
            flash("This note doesn't exist", category="error")
            return redirect(url_for("views.home"))
    else:
        flash("This note doesn't exist", category="error")
        return redirect(url_for("views.home"))

    if request.method == "POST":
        note_text = request.form.get("note")
        if len(note_text) < 1:
            flash("Add a good note please", category="error")
        else:
            note.note = note_text
            db.session.commit()
            flash("Note edited successfully", category="success")
            return redirect(url_for("views.home"))

    return render_template("edit_note.html", user=current_user, note_data=note.note)

