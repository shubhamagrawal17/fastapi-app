Perfect—here’s your **clean, end-to-end, copy-paste demo** with **ALL commands in single line** (including the missing cert-manager step that caused your error).

Follow exactly in order 👇

---

# 🚀 What You’ll Build

* GitHub Actions job runs on **self-hosted runner**
* Runner runs as a **pod inside AKS**
* Full CI runs **inside your cluster**

---

# 🧱 Architecture

![Image](https://images.openai.com/static-rsc-4/JadWUF6Gan_evWU4Z-3v-P75dsCWOYDpFEjpVXDjG7cm_vrwdcfGpcXJZqiMR2Qg12j8sZ882jGIg4RJdJWAY4XuLjjOEQah3L9kuUAhnhZ-tti0d4kjj2tPeGihkGiwLUxaeUCvkjkJUzQ6GsMOXWje9MWGgVCdzqLhVjQv8EliL3YVErKBduCMYSQ1N5PQ?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/UKvsn8YLw6EjsBV6jg0UoPVXXZMnXFV5eXh_iU520NZNTl01WWTPtflSd_3MKo4ycbkdMtr4hXFfAh6aKM7ehm3L2PlpWTBGDZq5fi6DGgHXGq52d-fpfpdheRauF-mrPZ2yH-pm2dqxIbaBfKXQwQMTNRQDhewGSqtl7UsUC32ceMe7CMd7VDpS5kYXwQpd?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/ujkOcSnD2RrNjbXWsk_1yDIC7cNw8SNHLUDjdn96hWHsmR45e7z8lG9CGK-KaRQHs_Go9rDrk2FC9KwTRkEQbwTLRNipGTfV05wCVG9m4RabFa66cQZCWeysmRFKfH1tIc6HPqTqeKl4wn_yKAuFRxLBR4jTgIaRnQCKn6tiZsfRBegC5bcDuSgJpuvm6KJv?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/-InLZ_KpslQprHAFvzKcafK2JdDcCxAAJUbCkS_H0h1xfnl6jLApotBF9o5sYFlf7OGld2jZzyXX-bB9VUmHDwCQKgVCJpJaPx6oKMIVCUVgXsMRgt8rGHSMXUpUHI5p4Bo_fnTti8iyvvfzjWDvXjXwEyn72XhoMqle6OccNAwknBJfZK681qEIl7NTM9Pl?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Mu7rSdVF_OcOjznGKerACbyhkRG5p6GcDL6BhoaNDDugPQzc9MpTZ5y-ELdMbMSfcZYtuAZ7Co1ROm6whz9w2nEl9Slhcy9mwRX4QGsClzYSPIb976JkYwJu2k5mF77PorNikAs0lgwUeOn7UXFtbpA1vIdKCVyquOZp7aziSSZGF6d9thiwn8plTuCjVupS?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/zimPec20AYA0avxRDDJIOoLoffX3X8dH8ZzUCt8TQ_eP8BhjUE3mfTDBaPw26z_rSo5OBRq6BRxwgP6EmM6VKF5fNpkrKTa2XTKmD43fkV8QbtHeyrMZDfREeFLmDqqjxMu87rjmi1Pabo0xk5DwSxX5lA5ZKtOh5oH7_E1e_0nRDSbFnj7l47sEB_fZnboO?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/RyyNe_oLlt8nbbwXqCfsFB3NK2vN4nR6i1ND7bykcDpY6mA1RAGT9myhksKCRgTnVsoRRI3D7aCxVlcMCxGa6kioszxN7g2R0w6KXkh3U4aeaJYcKRErFjrvxYTYLwIUMSQgNr39U6d_Litv67VHscoCRcXLmUECQq4TohBIuWHRMgAYNeU0amtVsZozjWpK?purpose=fullsize)

---

# ⚙️ STEP 1 — Create AKS Cluster

```bash
az login
```

```bash
az group create --name aks-rg --location eastus
```

```bash
az aks create --resource-group aks-rg --name myAKSCluster --location eastus --node-count 1 --node-vm-size Standard_D2s_v3 --enable-managed-identity --generate-ssh-keys
```

---

# ⚙️ STEP 2 — Connect to Cluster

```bash
az aks get-credentials --resource-group aks-rg --name myAKSCluster
```

```bash
kubectl get nodes
```

---

# ⚠️ STEP 3 — Install cert-manager (MANDATORY FIX)

👉 This fixes your error

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.crds.yaml
```

```bash
helm repo add jetstack https://charts.jetstack.io
```

```bash
helm repo update
```

```bash
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace
```

```bash
kubectl get pods -n cert-manager
```

👉 Wait until all pods are **Running**

---

# ⚙️ STEP 4 — Install ARC

Using Actions Runner Controller

```bash
helm repo add actions-runner-controller https://actions-runner-controller.github.io/actions-runner-controller
```

```bash
helm repo update
```

```bash
helm install arc actions-runner-controller/actions-runner-controller --namespace actions-runner-system --create-namespace
```

```bash
kubectl get pods -n actions-runner-system
```

---

# 🔐 STEP 5 — Create GitHub PAT

Go to GitHub:

👉 Settings → Developer Settings → **Tokens (classic)**

Permissions:

* repo
* workflow

---

# 🔐 STEP 6 — Create Kubernetes Secret

```bash
kubectl create secret generic controller-manager --namespace actions-runner-system --from-literal=github_token=YOUR_PAT_HERE
```

---

# 🏃 STEP 7 — Create Runner Deployment

Create file: `runner.yaml`

```yaml
apiVersion: actions.summerwind.dev/v1alpha1
kind: RunnerDeployment
metadata:
  name: aks-runner
  namespace: actions-runner-system
spec:
  replicas: 1
  template:
    spec:
      repository: YOUR_USERNAME/YOUR_REPO
```

Apply:

```bash
kubectl apply -f runner.yaml
```

```bash
kubectl get pods -n actions-runner-system
```

---

# ⚙️ STEP 8 — Add GitHub Workflow

Create:

```
.github/workflows/ci.yml
```

```yaml
name: AKS Self Hosted CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: self-hosted

    steps:
      - uses: actions/checkout@v4
      - run: echo "Running inside AKS 🚀"
```

---

# 🚀 STEP 9 — Trigger Pipeline

```bash
git add .
```

```bash
git commit -m "test aks runner"
```

```bash
git push
```

👉 Go to GitHub → Actions tab
👉 You’ll see job running on **self-hosted runner**

---

# 🔍 STEP 10 — Verify Inside AKS

```bash
kubectl get pods -n actions-runner-system
```

```bash
kubectl logs -n actions-runner-system <runner-pod-name>
```

---

# 🧹 STEP 11 — CLEANUP (IMPORTANT 💸)

```bash
az group delete --name aks-rg --yes --no-wait
```


Just tell me 👍
