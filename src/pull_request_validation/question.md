> Challenge Background

You have just joined a DevOps team and have been asked to write a script that validates pull requests.

A pull request is an event that takes place when a developer is ready to begin merging new code changes within the main project repository.

> Input Description

The pull request is provided as an array of strings with each element of the array being a code commit.

For example: [Commit_1,Commit _2,...]

Each commit has 4 parts delimited by commas as follows, all values are input as strings so perform $type conversions as necessary:

SequenceNumber,CommitMsg,FileValue,HashValue

`SequenceNumber`: A hexadecimal value provided as a string indicating the sequence of the commits. An example value is `0x21a`

`CommitMsg`: The message written by the developer indicating what changes were made in the commit in the following format: ticket number-commit $type-change description

`FileValue`: An integer value value representing the files in the commit

`HashValue`: An integer value used to verify the file integrity

> Output Description

Your output must be a boolean value (true/false) indicating if the pull request is valid

> Instructions

Your task is to validate the Merge Request by validating each commit within it and return a boolean value True if the commit message is valid and False if it is invalid.

In order to do this you must validate the following.

- Ensure that the hexadecimal sequence in SequenceNumber is correct. Each commit must have a sequence number that is incremented by one from the previous commit
- Ensure that each commit message contains the following:
  - It must be in the format of ticket number-commit $type-change description delimited by hyphens. (Assume that the order of the items such as ticket number within the commit message wont change in the test cases and that the string will always contain two - characters)
  - The ticket number must be a 4 digit integer value
  - The commit $type must be one of the following: [fix,feat,chore,refactor]
  - The code must contain a change description this can be any non-empty string
  - Finally, ensure that the hash value in each commit is correct. The hash value can be calculated by finding the remainder of dividing the FileValue by 151 and reversing the digits.
