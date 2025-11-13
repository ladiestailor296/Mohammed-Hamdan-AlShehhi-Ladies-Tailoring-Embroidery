import tkinter as tk from tkinter import messagebox, simpledialog, ttk import subprocess import os

=========================

Configuration

=========================

REPO_PATH = "."  # Current directory BRANCH = "main"

=========================

Helper Functions

=========================

def run_command(cmd): """Run a shell command and return output and success flag.""" result = subprocess.run(cmd, shell=True, capture_output=True, text=True) if result.returncode != 0: return f"❌ Error: {result.stderr.strip()}", False return f"✅ {result.stdout.strip()}", True

def ensure_branch(branch): result = subprocess.run(f"git rev-parse --verify {branch}", shell=True, capture_output=True, text=True) if result.returncode != 0: run_command(f"git checkout -b {branch}") else: run_command(f"git checkout {branch}")

def get_all_files(): files = [] for root, dirs, filenames in os.walk(REPO_PATH): for f in filenames: if not f.endswith('.py') and not f.startswith('.'): files.append(os.path.relpath(os.path.join(root, f), REPO_PATH)) return files

def commit_selected_files(selected_files, commit_message, progress_bar=None): logs = [] total = len(selected_files) + 2  # stage + commit + push step = 0 for file in selected_files: log, _ = run_command(f"git add '{file}'") logs.append(log) step += 1 if progress_bar: progress_bar['value'] = int((step/total)*100) step += 1 log, success = run_command(f'git commit -m "{commit_message}"') logs.append(log) if not success: messagebox.showerror("Commit Error", log) return logs step += 1 if progress_bar: progress_bar['value'] = int((step/total)*100) log, success = run_command(f"git push origin {BRANCH}") logs.append(log) if not success: messagebox.showerror("Push Error", log) if progress_bar: progress_bar['value'] = 100 return logs

=========================

GUI Application

=========================

class GitCommitGUI: def init(self, master): self.master = master master.title("Professional Git Commit & Push Tool") master.geometry("750x650")

tk.Label(master, text="Select files to commit:", font=("Arial", 14, "bold")).pack(pady=10)

    # Frame for scrollable file list
    self.frame = tk.Frame(master)
    self.frame.pack(fill=tk.BOTH, expand=True)
    self.canvas = tk.Canvas(self.frame)
    self.scrollbar = tk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
    self.scrollable_frame = tk.Frame(self.canvas)

    self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
    self.canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    self.canvas.pack(side="left", fill="both", expand=True)
    self.scrollbar.pack(side="right", fill="y")

    self.file_vars = []
    self.checkbuttons = []

    # Buttons
    btn_frame = tk.Frame(master)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="Select All", command=self.select_all, bg="#2196f3", fg="white").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Deselect All", command=self.deselect_all, bg="#f44336", fg="white").pack(side="left", padx=5)
    tk.Button(btn_frame, text="Refresh Files", command=self.refresh_files, bg="#9c27b0", fg="white").pack(side="left", padx=5)

    # Commit button
    tk.Button(master, text="Commit & Push Selected Files", command=self.commit_files, bg="#4caf50", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    # Progress bar
    self.progress = ttk.Progressbar(master, orient="horizontal", length=700, mode="determinate")
    self.progress.pack(pady=5)

    # Logs
    self.log_text = tk.Text(master, height=15, width=90)
    self.log_text.pack(pady=10)

    self.refresh_files()

def select_all(self):
    for var in self.file_vars:
        var.set(True)

def deselect_all(self):
    for var in self.file_vars:
        var.set(False)

def refresh_files(self):
    # Clear existing
    for chk in self.checkbuttons:
        chk.destroy()
    self.file_vars.clear()
    self.checkbuttons.clear()

    # Add files
    files = get_all_files()
    for f in files:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(self.scrollable_frame, text=f, variable=var)
        chk.pack(anchor="w", padx=10, pady=2)
        self.file_vars.append(var)
        self.checkbuttons.append(chk)

def commit_files(self):
    selected_files = [f for var, f in zip(self.file_vars, get_all_files()) if var.get()]
    if not selected_files:
        messagebox.showwarning("No files selected", "Please select at least one file to commit.")
        return
    default_msg = f"Auto-update: {', '.join(selected_files[:5])}" + (f", and {len(selected_files)-5} more files" if len(selected_files) > 5 else "")
    commit_message = simpledialog.askstring("Commit Message", f"Enter commit message or press OK to use default:\n{default_msg}")
    commit_message = commit_message if commit_message else default_msg

    ensure_branch(BRANCH)
    logs = commit_selected_files(selected_files, commit_message, self.progress)
    self.log_text.delete(1.0, tk.END)
    for log in logs:
        self.log_text.insert(tk.END, log + "\n")
    messagebox.showinfo("Done", "Selected files committed and pushed successfully!")

=========================

Run GUI

=========================

if name == "main": root = tk.Tk() app = GitCommitGUI(root) root.mainloop()
