# 🚀 FastAPI Project – Push to GitHub (Step-by-Step Guide)

This guide explains how to push a local FastAPI project to GitHub from scratch.

---

## 📁 Prerequisites

Make sure you have:

* Git installed → [https://git-scm.com/](https://git-scm.com/)
* GitHub account → GitHub
* Your project folder ready (e.g., `fastapi_project`)

---

## 📂 Step 1: Navigate to Project Folder

Open terminal / PowerShell:

```bash
cd path/to/your-project
```

Example:

```bash
cd fastapi_project
```

---

## 🔧 Step 2: Initialize Git Repository

```bash
git init
```

---

## 📦 Step 3: Add Files to Git

```bash
git add .
```

---

## 📝 Step 4: Commit Your Code

```bash
git commit -m "Initial commit"
```

---

## 🌐 Step 5: Create Repository on GitHub

1. Go to GitHub
2. Click **New Repository**
3. Enter repository name (e.g., `fastapi-app`)
4. Click **Create Repository**

⚠️ Important:

* Do **NOT** select "Initialize with README"

---

## 🔗 Step 6: Add Remote Repository

Copy your GitHub repo URL and run:

```bash
git remote add origin https://github.com/<username>/<repo-name>.git
```

Example:

```bash
git remote add origin https://github.com/shubhamagrawal17/fastapi-app.git
```

---

## 🔄 Step 7: Rename Branch to Main

```bash
git branch -M main
```

---

## 🚀 Step 8: Push Code to GitHub

```bash
git push -u origin main
```

---

## ✅ Step 9: Verify

* Open your repository on GitHub
* You should see your project files uploaded 🎉

---

## ⚠️ Common Errors & Fixes

### ❌ Error: `src refspec main does not match any`

✔️ Fix:

```bash
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---
