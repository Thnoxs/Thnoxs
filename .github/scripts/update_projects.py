import os
import requests
import re

def update_readme():
    token = os.environ['GITHUB_TOKEN']
    username = "Thnoxs"
    headers = {"Authorization": f"token {token}"}
    
    # Repos fetch karna
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    repos = response.json()
    
    featured_repos = []
    for repo in repos:
        topics = repo.get('topics', [])
        if 'push-on-main' in topics:
            name = repo['name']
            desc = repo['description'] or "No description provided."
            url = repo['html_url']
            featured_repos.append(f"| **{name}** | {desc} | [Demo→]({url}) |")

    # Agar koi repo nahi mili toh update mat karo
    if not featured_repos:
        print("No repos with 'push-on-main' tag found.")
        return

    new_content = "| Project | Overview | Links |\n| :--- | :--- | :--- |\n" + "\n".join(featured_repos)
    
    with open("README.md", "r") as f:
        content = f.read()

    # Sirf markers ke beech ka hissa badalna hai
    pattern = r".*?"
    replacement = f"\n{new_content}\n"
    
    updated_readme = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    update_readme()