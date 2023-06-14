import math
from github import Github

# Enter your GitHub personal access token
ACCESS_TOKEN = "your-access-token"

# Enter the repository details
REPO_OWNER = "your-username"
REPO_NAME = "your-repository-name"

def calculate_factorial(number):
    return math.factorial(number)

def upload_to_github(file_content, file_name):
    g = Github(ACCESS_TOKEN)
    repo = g.get_user(REPO_OWNER).get_repo(REPO_NAME)
    contents = repo.get_contents("")
    repo.create_file(f"{file_name}", "Adding factorial script", file_content, branch="main")
    print(f"Uploaded {file_name} to GitHub!")

def main():
    number = int(input("Enter a number: "))
    factorial = calculate_factorial(number)
    file_content = f"The factorial of {number} is {factorial}."
    file_name = f"factorial_{number}.txt"
    upload_to_github(file_content, file_name)

if __name__ == "__main__":
    main()
