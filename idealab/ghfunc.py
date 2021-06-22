import requests
import json
import os
from dotenv import load_dotenv
# Notice for this we require a URL to the github repo. This function should
# Parse the returned JSON and give proper about info. Review the return info in the
# git hub documentation
# We require a token to get unlimited requests. (Else you would be restricted to 60 per hour)
# TODO REMOVE THE TOKEN AFTER USE
load_dotenv()
token = os.getenv('API_TOKEN')
headers = {'Authorization': 'token %s' % token,
           'Accept': 'application/vnd.github.v3+json'}


def parseDescription():
    r = requests.get('https://api.github.com/orgs/makeopensource/repos',
                     headers=headers)
    if r.status_code != 200:
        print("Error calling rest:")
        print(r.json())
    else:
        retDict = {}
        for repos in r.json():
            name = repos.get("name")
            description = repos.get("description")
            if description == None:
                description = ""
            retDict[name] = description
        return retDict

# Creates a repo with the following name and description. #change private to False or True when necessary

def createRepo(name, description):
        data = {'name': name,
                'description': description,
                "private": False
                }
        r = requests.post('https://api.github.com/orgs/makeopensource/repos',
                            headers=headers,
                            data=json.dumps(data)) 
        return (r.json().get("html_url"), r.json().get('name'))

# viewCollaborators gets a list of collaborators (and their data) for a specific repo.
def viewCollaborators(repo):
    r = requests.get('https://api.github.com/repos/makeopensource/' + repo + '/collaborators',
                     headers=headers)
    for user in r.json():
        print(user)
        return r.json()


# permissionUserToRepo.
# user and repo are username of the user we want to give permission to and the repo is the repo name respectfully
# permissions is a string value of either push, pull, admin, maintain, triage.
# NOTE: There is an inconsistency with the read and write permissions in the REST API
# for clarity: read = pull , write = push
# View the permissions here: https://docs.github.com/en/rest/reference/repos#add-a-repository-collaborator
def permissionUserToRepo(user, repo, permission='pull'):
    permissions = json.dumps({'permission': permission})
    print("user", user)
    print("repo", repo)
    r = requests.put('https://api.github.com/repos/makeopensource/' + repo + '/collaborators/' + user,
                     headers=headers,
                     data=permissions)
    print(r.status_code)


