#!/usr/bin/env bash

#basic settings
GH_USERNAME=jbukala
GH_REPO=jbukala.github.io

#advanced settings
BRANCH=master
GITHUB_OUTPUT_FOLDER=built_website
WEBSITE_OUTPUT_FOLDER=output
SHOW_CHANGES=true
TARGET_REPO=${GH_USERNAME}/${GH_REPO}.git

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to GitHub Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "jorisbukala@gmail.com"
        git config --global user.name "Deploy Bot"
    fi
    # Pull hash and commit message of the most recent commit
    commitHash=$(git rev-parse HEAD)
    commitMessage=$(git log -1 --pretty=%B)
    #get the current output in a separate directory
    git clone --quiet --branch=$BRANCH https://${GH_PAGES}@github.com/$TARGET_REPO $GITHUB_OUTPUT_FOLDER > /dev/null
    #copy the new output
    cd $GITHUB_OUTPUT_FOLDER
    rsync -rv --exclude=.git  ../$WEBSITE_OUTPUT_FOLDER/* . --delete
    #add, commit and push files
    git add -A .
    if [ "$SHOW_CHANGES" == "true" ]; then
      echo -e "Changes:"
      git status -s
      echo -e "\n"
    fi
    detailedMessage="Commit $commitHash pushed to GitHub Pages by Travis build $TRAVIS_BUILD_NUMBER"
    
    git commit -m "$commitMessage" -m "$detailedMessage"
    git push -fq origin $BRANCH > /dev/null || exit $?
    echo -e "Deploy completed\n"
fi
