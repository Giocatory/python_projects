from urllib.request import urlopen
from xml.etree.ElementTree import parse


# Скачивание и парсинг RSS-фида
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# Извлечение и вывод нужных тегов
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()


# CodersLegacy: How to read Excel files with Multiple Sheets in Python Pandas
# Sat, 24 Jun 2023 19:21:22 +0000
# https://coderslegacy.com/python-pandas-read-excel-files/

# Abhijeet Pal: How to Read a Text File in Python with Examples
# Sat, 24 Jun 2023 14:02:31 +0000
# http://djangocentral.com/how-to-read-a-text-file-in-python/

# Abhijeet Pal: How to Add ads.txt to Your Django Project: Boost Ad Revenue with Simple Implementation
# Sat, 24 Jun 2023 04:43:37 +0000
# http://djangocentral.com/how-to-add-adstxt-to-your-django-project-boost-ad-revenue-with-simple-implementation/

# Brett Cannon: State of WASI support for CPython: June 2023
# Fri, 23 Jun 2023 23:41:01 +0000
# https://snarky.ca/wasi-support-for-cpython-june-2023/

# PyCon: PyCon US 2023 Recap and Recording Release
# Fri, 23 Jun 2023 15:36:28 +0000
# https://pycon.blogspot.com/2023/06/pycon-us-2023-recap-and-recording.html

# Fabio Zadrozny: robocorp.log: a library to answer what happened in a Python run.
# Fri, 23 Jun 2023 12:39:55 +0000
# http://pydev.blogspot.com/2023/06/robocorplog-library-to-answer-what.html

# Stack Abuse: Efficient Data Manipulation with Apply() Function in Pandas
# Fri, 23 Jun 2023 12:34:24 +0000
# https://stackabuse.com/efficient-data-manipulation-with-apply-function-in-pandas/

# Real Python: The Real Python Podcast – Episode #161: Resources and Advice for Building CircuitPython Projects
# Fri, 23 Jun 2023 12:00:00 +0000
# https://realpython.com/podcasts/rpp/161/

# PyBites: 11 Planning and Productivity tips for Python developers
# Fri, 23 Jun 2023 10:39:56 +0000
# https://pybit.es/articles/11-planning-and-productivity-tips-for-python-developers/

# Abhijeet Pal: Flask vs Django: Selecting the Perfect Python Web Framework
# Thu, 22 Jun 2023 15:22:22 +0000
# http://djangocentral.com/flask-vs-django-selecting-the-perfect-python-web-framework/

# PyCharm: PyCharm 2023.1.3 Is Out!
# Thu, 22 Jun 2023 12:15:29 +0000
# https://blog.jetbrains.com/pycharm/2023/06/2023-1-3/

# Python Software Foundation: Announcing Our New Security Developer in Residence!
# Thu, 22 Jun 2023 09:50:11 +0000
# https://pyfound.blogspot.com/2023/06/announcing-our-new-security-developer.html

# ListenData: 14 Free and Open Source Alternatives to ChatGPT
# Thu, 22 Jun 2023 07:19:54 +0000
# https://www.listendata.com/2023/03/open-source-chatgpt-models-step-by-step.html

# Matt Layman: First Major Model - Building SaaS with Python and Django #163
# Thu, 22 Jun 2023 00:00:00 +0000
# https://www.mattlayman.com/blog/2023/first-major-model-building-saas-with-python-and-django-163/

# Paolo Melchiorre: 2023 Python Software Foundation Board Nomination
# Wed, 21 Jun 2023 17:06:34 +0000
# https://www.paulox.net/2023/06/21/2023-python-software-foundation-board-nomination/

# The Python Coding Blog: Breaking the Rules — My Thoughts on Narrative Technical Writing
# Wed, 21 Jun 2023 16:19:24 +0000
# https://thepythoncodingbook.com/2023/06/21/breaking-the-rules-my-thoughts-on-narrative-technical-writing/

# Real Python: Python's Self Type: How to Annotate Methods That Return self
# Wed, 21 Jun 2023 14:00:00 +0000
# https://realpython.com/python-type-self/

# Stack Abuse: Step-by-Step Guide to File Upload with Flask
# Wed, 21 Jun 2023 12:42:00 +0000
# https://stackabuse.com/step-by-step-guide-to-file-upload-with-flask/

# Python Software Foundation: The 2023 PSF Board Election is Open!
# Wed, 21 Jun 2023 11:39:15 +0000
# https://pyfound.blogspot.com/2023/06/the-2023-psf-board-election-is-open.html

# CodersLegacy: Python JIT Compilers – Just in time compilation
# Wed, 21 Jun 2023 10:48:34 +0000
# https://coderslegacy.com/python-jit-compilers/

# CodersLegacy: Python APScheduler: Exploring the Power of AsyncIOScheduler
# Tue, 20 Jun 2023 19:42:43 +0000
# https://coderslegacy.com/python-apscheduler-asyncioscheduler/

# PyCoder’s Weekly: Issue #582 (June 20, 2023)
# Tue, 20 Jun 2023 19:30:00 +0000
# https://pycoders.com/issues/582

# Python Insider: Python 3.12.0 beta 3 released
# Tue, 20 Jun 2023 14:52:23 +0000
# https://pythoninsider.blogspot.com/2023/06/python-3120-beta-3-released.html

# Real Python: Recursion in Python
# Tue, 20 Jun 2023 14:00:00 +0000
# https://realpython.com/courses/python-recursion/

# Python Bytes: #341 Shhh - For Secrets and Shells
# Tue, 20 Jun 2023 08:00:00 +0000
# https://pythonbytes.fm/episodes/show/341/shhh-for-secrets-and-shells