## **About**
- Fetch phone specification from https://www.hallogsm.com/ and output it into json format

## **Clone or Download this Repository**
If you have `git` installed in your machine :
`gh repo clone bintangginanjar/GSM-Scraper`

Clone the repo without git :
- Download the repo : [Download zip](https://github.com/bintangginanjar/GSM-Scraper/archive/refs/heads/main.zip)
- Extract the zip on destination folder

## **Install Python using Anaconda**
- Download Anaconda from following URL: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
- Follow the installation steps, and make sure python 3 is successfully installed in your machine by type following command : 

`python --version`

## **Install Python IDE**
You can use your favorite IDE :
- [PyCharm](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu)
- [Visual Code](https://code.visualstudio.com/Download)
- [Spyder](https://docs.spyder-ide.org/current/installation.html)
- [Sublime Text](https://www.sublimetext.com/3)

## **Install Scrapy**
Since we've already install Anaconda, we can install Scrapy using following command

`conda install -c conda-forge scrapy`

Alternatively we can use pip command

`pip install Scrapy`

## **Running Scrapy**
- Enter extracted directory
- Simply put following commands into your shell if you want to fetch phone specification from https://www.hallogsm.com/

`scrapy crawl hallogsm`
