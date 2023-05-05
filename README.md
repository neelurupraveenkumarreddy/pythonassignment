# pythonassignment

#about questions in my assignment

*********inttorom.py********

 this program converts any interger from 1 to 3999 into roman number.
 Ex: 2045 in roman numbers is MMXLV

*********leapyear.py*********
 this program finds wheather given year is a leap year or not.
 ex: 1900 is not a leap year

*********listnumber.py*********
 this program at first converts a group of list into a programm and add 1 to it 
 again conert it into list
 adding 1 to given number in a list form
  Input: digits = [1,2,3]
  Output: [1,2,4]
  Explanation: The array represents the integer 123.
  Incrementing by one gives 123 + 1 = 124.
  Thus, the result will be [1,2,4].

***********maxvolume.py*********
 this program finds the max area that is max water that two diiferent indexed elements can store
 we are given an integer array height of length n. There are n vertical lines drawn such that the two
 endpoints of the ith line are (i, 0) and (i, height[i]).
 Find two lines that together with the x-axis form a container, such that the container contains the most water.
 Return the maximum amount of water a container can store.
 Notice that you may not slant the container.
 Input: height = [1,8,6,2,5,4,8,3,7]
 Output: 49
 Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
 (blue section) the container can contain is 49.

*************medianoftwosortedarrays************
 this program finds the median of two sorted lists/array of numbers.
 median of two sorted arrays
 Example 1:
 Input: nums1 = [1,3], nums2 = [2]
 Output: 2.00000
 Explanation: merged array = [1,2,3] and median is 2.
 Example 2:
 Input: nums1 = [1,2], nums2 = [3,4]
 Output: 2.50000
 Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

**********palindrome.py*********************
 this program finds wheather given string is a palindrome or not
 palindrome
 Input: x = 121
 Output: true
 Explanation: 121 reads as 121 from left to right and from right to left.

**********palindromess.py*********************
 this program finds the palindromes in the given list 
 and prints palindromes position in given list
 Input: words = ["abcd","dcba","lls","s","sssll"]
 Output: [[0,1],[1,0],[3,2],[2,4]]
 Explanation: The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]

**************phonenumbers.py******************
 this program basically concatenates the charaters present at given numbers in a key pad phone and gives output as list
 inear combination of a phone number
 Example 1:
 Input: digits = "23"
 Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
 Example 2:
 Input: digits = ""
 Output: []
 Example 3:
 Input: digits = "2"
 Output: ["a","b","c"]

*************reversweinteger.py**********
 this program reverse the integer without changing the sign
 reversing an integer
 Input: x = -123
 Output: -321

*************tagetpositions.py***********
 this program adds every elemnt in the program with the other and finds if the key is equal to their sum
 and return the poistion of added numbers to give the value of target
 Input: nums = [2,7,11,15], target = 9
 Output: [0,1]
 Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#################### ABOUT GITHUB ##########################

************** What is github & git ?  *****************

Git is an open-source, Version control tool created in 2005 by developers working on the Linux operating system;
GitHub is a company founded in 2008 that makes tools which integrate with git. You do not need GitHub to use git,
but you cannot use GitHub without using git. 

Before using Git, it is important to know why we need it. Git makes it easy to contribute to open source projects.
Nearly every open-source project uses GitHub to manage their documentation. By using GitHub, you make it easier to
get excellent documentation. Their help section and guides have integration with Git. 

************** who uses the github ? ******************

GitHub is used by software engineers, programmers, developers, instructors, and coding students to build unique code.
Companies and educational institutions use it to make coding tasks easier, faster, and more streamlined. Any team or 
company that works on different projects which require development in the form of files can use this service. For 
example, content and marketing teams can use GitHub to organize their projects.

************** what are repositories ? ****************

In GitHub, a repository is similar to a folder and becomes a folder that is available online on the cloud for people
to download, access, and contribute. It is a centralized location in the distributed Version control platform for 
enabling users to collaborate and adapt the culture of open source projects and emphasize forking code, sharing ideas, and so on.

*************How to create a repository ? ***************

There are various ways of creating a GitHub repository. A GitHub repository is a place where you can store your code,
files, and other project-related items. You can create a repository on your personal account or any organization where 
you have sufficient permissions1.

Some of the ways to create a GitHub repository are:

**Using the web browser: You can create a new repository on the GitHub website by clicking on the New button in the upp
  er-right corner of any page, and filling out the required fields. You can   also choose to initialize the 
  repository with a README file, a .gitignore file, or a license file.
**Using the GitHub CLI: You can create a new repository using the GitHub command-line interface (CLI) by running the 
  command gh repo create and following the prompts. You can also specify various options such as the name, description,
  visibility, and template of the repository.
**Using an existing repository as a template: You can create a new repository with the directory structure and files of
  an existing repository by selecting the Choose a template dropdown menu and clicking on a template repository. You can
  also include all branches from the template repository if you want.

**************How to add project files to github? ***************

There are various ways to add project files to a GitHub repository. A GitHub repository is a place where you can store 
your code, files, and other project-related items. You can add files to a repository on GitHub or by using the command line.

Some of the ways to add project files to a GitHub repository are:

**Using the web browser: You can upload and commit an existing file to a repository on GitHub by clicking on the Add file 
  drop-down and selecting Upload files. You can drag and drop the file or folder you want to upload to your repository. You
  can also add a commit message and choose a branch for your commit.
**Using the command line: You can upload an existing file to a repository on GitHub using the command line by moving the file
  to your local repository directory and running the commands git add, git commit, and git push.
**Using an existing project as a template: You can add your project to a repository that has the same owner as your project 
  by clicking on Projects and selecting Add project. You can search for and select your project from the list of projects that appear.

********** What is a branch & how to create ana merge branches ? ****************

A branch is a parallel version of your repository that allows you to work on different features or tasks without affecting the
main branch. You can create a branch using the git branch command or the GitHub web interface. You can merge a branch into another
branch using the git merge command or by creating a pull request on GitHub.

**********What is a pull request ? *************************

A pull request in GitHub is a way of proposing changes to a repository that you do not have direct access to. A pull request lets 
you fork (copy) a repository, make changes to your fork, and then request that the original repository merges your changes.

A pull request is useful for collaborating with other developers, contributing to open source projects, and getting feedback on 
your code. You can also use a pull request to review and discuss the changes before merging them.

To create a pull request in GitHub, you need to follow these steps:

***    Fork the repository that you want to contribute to.
***    Clone your forked repository to your local machine.
***    Create a new branch for your changes and switch to it.
***    Make and commit your changes to your branch.
***    Push your branch to your forked repository on GitHub.
***    Go to the original repository on GitHub and click on the Pull requests tab.
***    Click on the New pull request button and select your branch as the compare branch.
***    Add a title and a description for your pull request and click on Create pull request.
***    After creating a pull request, you can wait for the repository owners or collaborators to review your changes, comment on
       them, suggest modifications, or approve them. You can also update your pull request by pushing more commits to your branch.
       Once your pull request is ready to be merged, you or someone else can click on the Merge pull request button.
