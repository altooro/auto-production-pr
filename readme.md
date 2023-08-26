# Auto Open Production Pull Request

This Python script automates the process of version bumping and updating changelogs for a GitHub repository. It utilizes the GitHub API to achieve this automation. The script is designed to be used in a Continuous Integration (CI) environment, such as GitHub Actions, to streamline the release process.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

1. **GitHub Token**: You need to set up a GitHub personal access token with appropriate permissions. This token should be stored in the environment variable `GITHUB_TOKEN`.

2. **Repository Name**: The name of the target GitHub repository should be stored in the environment variable `REPO_NAME`.

3. **Head Branch**: The name of the branch from which the pull requests will be merged should be stored in the environment variable `HEAD_BRANCH`.

## Usage

1. Ensure that the script has the necessary execution permissions.

2. Set up the required environment variables (`GITHUB_TOKEN`, `REPO_NAME`, `HEAD_BRANCH`) either in your CI environment or by exporting them in your shell.

3. Run the script as part of your CI workflow.
