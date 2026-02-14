"""
Git Learning File - Beginner's Guide
=====================================
This file contains simple examples to help you learn Git!

Basic Git Commands to Try:
- git status: Check what changes you've made
- git add Git.py: Stage this file for commit
- git commit -m "Your message": Save your changes
- git log: See history of commits
- git diff: See what changed
"""

# Example 1: A simple greeting function
def greet_git_learner(name):
    """
    A simple function to greet Git learners.
    Try modifying this and committing the changes!
    """
    print(f"Hello, {name}! Welcome to learning Git!")
    print("Git helps you track changes in your code.")
    return f"Welcome, {name}!"


# Example 2: Git workflow simulator
def explain_git_workflow():
    """
    This function explains the basic Git workflow.
    """
    workflow_steps = [
        "1. Make changes to your files",
        "2. Use 'git status' to see what changed",
        "3. Use 'git add <filename>' to stage changes",
        "4. Use 'git commit -m 'message'' to save changes",
        "5. Use 'git push' to upload to remote repository"
    ]

    print("Basic Git Workflow:")
    for step in workflow_steps:
        print(step)

    return workflow_steps


# Example 3: Simple counter (good for practicing commits)
class GitPracticeCounter:
    """
    A simple counter class to practice making commits.
    Try incrementing the counter and committing each change!
    """

    def __init__(self):
        self.count = 0

    def increment(self):
        """Add 1 to the counter"""
        self.count += 1
        print(f"Counter is now: {self.count}")

    def decrement(self):
        """Subtract 1 from the counter"""
        self.count -= 1
        print(f"Counter is now: {self.count}")

    def reset(self):
        """Reset counter to 0"""
        self.count = 0
        print("Counter reset to 0")

    def get_count(self):
        """Get current count"""
        return self.count


# Example 4: A list of Git terms to learn
git_terms = {
    "repository": "A folder that Git tracks (your project)",
    "commit": "A snapshot of your code at a point in time",
    "branch": "A separate version of your code to work on",
    "merge": "Combining changes from different branches",
    "clone": "Copying a repository to your computer",
    "pull": "Getting latest changes from remote repository",
    "push": "Sending your changes to remote repository",
    "staging": "Preparing files to be committed"
}


def print_git_terms():
    """Print out Git terminology for learning"""
    print("\n=== Git Terms for Beginners ===")
    for term, definition in git_terms.items():
        print(f"\n{term.upper()}:")
        print(f"  {definition}")


# Example 5: Main function to run examples
def main():
    """
    Run this to see all examples!
    Command: python Git.py
    """
    print("=" * 50)
    print("Welcome to Git Learning with Python!")
    print("=" * 50)

    # Run greeting
    greet_git_learner("Beginner")

    print("\n")

    # Show workflow
    explain_git_workflow()

    print("\n")

    # Demo counter
    counter = GitPracticeCounter()
    print("Testing the counter:")
    counter.increment()
    counter.increment()
    counter.increment()

    print("\n")

    # Show terms
    print_git_terms()

    print("\n" + "=" * 50)
    print("Now try making changes and committing them!")
    print("=" * 50)


# Run the main function if this file is executed
if __name__ == "__main__":
    main()


"""
PRACTICE EXERCISES:
===================
1. Run this file: python Git.py
2. Change the greeting message in greet_git_learner()
3. Use 'git status' to see your changes
4. Use 'git add Git.py' to stage your changes
5. Use 'git commit -m "Updated greeting message"' to commit
6. Use 'git log' to see your commit history

Try this: Make small changes, commit often, and use descriptive messages!
"""