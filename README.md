# Steps
Create a `.env` file
```
AZURE_OPENAI_API_KEY=<>
AZURE_OPENAI_ENDPOINT=<>
AZURE_OPENAI_DEPLOYMENT=<>
AZURE_OPENAI_API_VERSION=<>
```

# Popular commands

```
bash .codeenv/setup.sh
bash main.sh
pip freeze > requirements.txt
pip uninstall -y -r requirements.txt
pip list
pip install -r requirements.txt
docker system prune -a
docker stop <container-id>
docker rm <container-id>
docker ps --all
docker images prune
docker rmi <image-name>
```

```
echo "# python-openai-prompts" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:senglin/python-openai-prompts.git
git push -u origin main
```

```
git config --global user.name "YOUR_NAME"
git config --global user.email "YOUR_EMAIL"
ssh-keygen -t ed25519 -C "your_email@example.com"
```

~/.ssh/config
```
Host github.com
  User git
  IdentityFile ~/.ssh/id_ed25519
```

```
git status
