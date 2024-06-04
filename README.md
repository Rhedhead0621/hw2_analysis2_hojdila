# Project hw2_analysis2_hojdila notes

 
Required Homework Files
-----------------------

HW2_Analysis2_hojdila.ipynb - main homework notebook

HW2_Analysis2_hojdila_InputVersion.ipynb - pared down version with an input() feature for three-letter file name descriptor

    Running the input version will generate data/log_copies/FCM/ - this will contain the files generated by using the input FCM - I deleted these files so you can run and not create errors or double-headers

# Data sources

data/log_copies/ = copies of originals for manipulation

data/log_copies/BCM_v1.xlsx = combined all the individual csv into one worksheet, with headers

data/log_copies/BCM_sorted.xlsx = sorted each sheet in the worksheet

data/log_copies/BCM.xlsx = final version, with headers and formulas

data/logs/ = original csv log files - added copies of 4 of the files and changed the three-letter designation to 'FCM' to run the input version

data/raw/ = not used

/downloads_python_excel/ = for reference only



















Information on using this cookiecutter

Development workflows
=======================

Create new project
----------------------

You've already done this if you are reading this file. You ran:

```bash
cookiecutter gh:Rhedhead0621/cookiecutter-datascience-simple
```

Put project under version control
---------------------------------

Let's get version control set up. You don't absolutely have to do this, but you should. For the local repository, do;

```bash
git init
git add .
git commit -m "Initial commit"
```

For the remote repository, make a github repository named hw2_analysis2_hojdila, then do;

```bash
git remote add origin git@github.com:Rhedhead0621/hw2_analysis2_hojdila.git
git branch -M main
git push -u origin main
```

Great. Using version control is good.


Folder structure
-----------------

Here's the folder structure that gets created by `cookiecutter-datascience-simple`:

	├── hw2_analysis2_hojdila	<- Your notebooks and scripts will live in the main project folder
		│   .gitignore					<- Common file types for git to ignore
		│   README.md					<- The top-level README for developers (you) using this project
		│   template-nb.ipynb			<- A Jupyter notebook template
		│
		├───data						<- Final and intermediate data
		│   └───raw						<- The original, immutable data dump
		│
		├───docs
		│       notes.md				<- Simple markdown template for project notes
		│
		└───output
				readme.md				<- Guidance for using this folder


Documentation
--------------

In this very simple project structure template, we've just included a markdown file with some typical
section headings to use for project notes. Expand as desired. Later in the semester we will learn how to
use Sphinx with restructuredText to write and generate documentation.