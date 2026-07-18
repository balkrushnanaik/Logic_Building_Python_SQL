"""
Simple Sticky Notes CLI

Usage:
  - add: create a new note
  - list: show all notes
  - view <id>: view a note
  - delete <id>: delete a note
  - clear: delete all notes
  - exit: quit

Notes are saved to stickynotes.json in the same folder.
"""

import json
import os
import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "stickynotes.json")


def load_notes():
	if not os.path.exists(DATA_FILE):
		return []
	try:
		with open(DATA_FILE, "r", encoding="utf-8") as f:
			return json.load(f)
	except Exception:
		return []


def save_notes(notes):
	with open(DATA_FILE, "w", encoding="utf-8") as f:
		json.dump(notes, f, ensure_ascii=False, indent=2)


def add_note():
	title = input("Title: ").strip()
	print("Enter note (end with a blank line):")
	lines = []
	while True:
		line = input()
		if line == "":
			break
		lines.append(line)
	content = "\n".join(lines).strip()
	note = {
		"id": int(datetime.datetime.now().timestamp() * 1000),
		"title": title or "(no title)",
		"content": content,
		"created": datetime.datetime.now().isoformat(),
	}
	notes = load_notes()
	notes.append(note)
	save_notes(notes)
	print("Saved.")


def list_notes():
	notes = load_notes()
	if not notes:
		print("No notes.")
		return
	for n in notes:
		print(f"{n['id']}: {n['title']} ({n.get('created','')})")


def view_note(cmd_parts):
	if len(cmd_parts) < 2:
		print("Usage: view <id>")
		return
	nid = int(cmd_parts[1])
	notes = load_notes()
	for n in notes:
		if n["id"] == nid:
			print("Title:", n["title"])
			print("Created:", n.get("created", ""))
			print("\n" + n.get("content", ""))
			return
	print("Note not found.")


def delete_note(cmd_parts):
	if len(cmd_parts) < 2:
		print("Usage: delete <id>")
		return
	nid = int(cmd_parts[1])
	notes = load_notes()
	new = [n for n in notes if n["id"] != nid]
	if len(new) == len(notes):
		print("Note not found.")
		return
	save_notes(new)
	print("Deleted.")


def clear_notes():
	confirm = input("Delete ALL notes? (y/N): ")
	if confirm.lower() == "y":
		save_notes([])
		print("All notes deleted.")


def main():
	print("Sticky Notes — simple CLI")
	while True:
		cmd = input("> ").strip()
		if not cmd:
			continue
		parts = cmd.split()
		c = parts[0].lower()
		if c == "add":
			add_note()
		elif c == "list":
			list_notes()
		elif c == "view":
			view_note(parts)
		elif c == "delete":
			delete_note(parts)
		elif c == "clear":
			clear_notes()
		elif c in ("exit", "quit"): 
			break
		else:
			print("Commands: add, list, view <id>, delete <id>, clear, exit")


if __name__ == "__main__":
	main()
