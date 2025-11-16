#!/usr/bin/env python3
"""
github_stats.py - Get GitHub repository statistics
"""

import requests
from datetime import datetime

class GitHubAPI:
    """Simple GitHub API client"""

    def __init__(self):
        self.base_url = "https://api.github.com"
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Python-Learning-Script'
        })
    
    def get_user(self, username):
        """Get user information"""
        url = f"{self.base_url}/users/{username}"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching user data: {e}")
            return None
        
    def get_repos(self, username):
        """Get user repositories"""
        url = f"{self.base_url}/users/{username}/repos"
        
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching repositories: {e}")
            return None
    
    def print_user_stats(self, username):
        """Print comprehensive user statistics"""
        print(f"\n{'='*60}")
        print(f"GITHUB PROFILE: {username}")
        print(f"{'='*60}")
        
        # Get user info
        user = self.get_user(username)
        if not user:
            return
        
        print(f"Name: {user.get('name', 'N/A')}")
        print(f"Bio: {user.get('bio', 'N/A')}")
        print(f"Location: {user.get('location', 'N/A')}")
        print(f"Public Repos: {user['public_repos']}")
        print(f"Followers: {user['followers']}")
        print(f"Following: {user['following']}")
        print(f"Created: {user['created_at'][:10]}")

        # Get repositories
        repos = self.get_repos(username)
        if not repos:
            return
        
        print(f"\nTop Repositories (by stars):")
        
        # Sort by stars
        sorted_repos = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)[:3]
        
        for repo in sorted_repos:
            print(f"\n  📦 {repo['name']}")
            print(f"     ⭐ {repo['stargazers_count']} stars")
            print(f"     🍴 {repo['forks_count']} forks")
            print(f"     📝 {repo.get('description', 'No description')[:120]}")
            if repo['language']:
                print(f"     💻 {repo['language']}")
        
        # Statistics
        total_stars = sum(repo['stargazers_count'] for repo in repos)
        total_forks = sum(repo['forks_count'] for repo in repos)
        languages = set(repo['language'] for repo in repos if repo['language'])
        
        print(f"\n{'='*60}")
        print("OVERALL STATISTICS")
        print(f"{'='*60}")
        print(f"Total Stars: {total_stars}")
        print(f"Total Forks: {total_forks}")
        print(f"Languages Used: {', '.join(sorted(languages))}")
        print(f"{'='*60}")

if __name__ == "__main__":
    api = GitHubAPI()

    # Analyze your own GitHub profile
    api.print_user_stats("schnstep")