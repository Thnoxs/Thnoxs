import os
import requests

def update_readme():
    token = os.environ['GITHUB_TOKEN']
    username = "Thnoxs"
    headers = {"Authorization": f"token {token}"}
    
    # Repos fetch karna
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    repos = response.json()
    
    featured_repos = []
    for repo in repos:
        # Check if 'push-on-main' tag exists in topics
        topics = repo.get('topics', [])
        if 'push-on-main' in topics:
            name = repo['name']
            desc = repo['description'] or "No description"
            url = repo['html_url']
            featured_repos.append(f"| **{name}** | {desc} | [Demo→]({url}) |")

    # Table content taiyar karna
    new_content = "| Project | Overview | Links |\n| :--- | :--- | :--- |\n" + "\n".join(featured_repos)
    
    # README file update karna
    with open("README.md", "r") as f:
        content = f.read()

    import re
    pattern = r".*?"
    replacement = f"\n{new_content}\n"
    updated_readme = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    update_readme()