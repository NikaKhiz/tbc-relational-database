# Books Generator

<p>Tbc books generator creates authors and books tables and populates them with fake data in sqlite db.
</p>
<p>When we run script, already existed tables are being droped, recreated and repopulated then after.</p>

<p>Then database collector fetches information from db and show us following results:</p>

<ul>
    <li>books that have most of the pages.</li>
    <li>the average num of pages that books have.</li>
    <li>youngest authors</li>
    <li>authors which doesnt have books</li>
    <li>authors with more then five books</li>
</ul>

### Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)

#

### Prerequisites

- <img src="readme/assets/python.png" width="25" style="position: relative; top: 8px" /> _Python @3.X and up_

- Faker - Python package that generates fake data.

- Starting from version 4.0.0, Faker dropped support for Python 2 and from version 5.0.0 only supports Python 3.7 and above. If you still need Python 2 compatibility, visit faker's official documentation: https://faker.readthedocs.io/en/stable/

- other libraries such as random, datetime, sqlite3 and json generally comes with python when you install it.

#

### Getting Started

1\. First of all you need to clone tbc-reltional-database repository from github:

```sh
git clone https://github.com/NikaKhiz/tbc-relational-database.git
```

2\. Then after you will need to install all of the dependencies included in requirements.txt file:

<p>
for that run the following commands in a root directory from your terminal:
</p>

```sh
pip install -r requirements.txt
```

3\. your operating system may be using different versions of python interpreter , so first check the version:

```sh
python --version
```

or

```sh
python3 --version
```

4\. After that in the root directory, you can run command from the terminal:

```sh
python main.py
```

or

```sh
python main.py
```

### this command runs the script, populates db, and display the results!

### Project Structure

```bash
├─── readme
│   ├─── assets
- .gitignore
- books.db
- database_collector.py
- database_generator.py
- main.py
- readme.md
- requirements.txt
- utils.py
```
