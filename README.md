Python Tutorial for Cookiecutter and Sacred
==============================
You can find more details here: https://docs.google.com/presentation/d/18KcMNFgHG4l0dX--r6YQowwdL2zLod5xj4lTHPr6pVY/edit?usp=sharing

## Part 1: Coockiecutter
1. Install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/readme.html?highlight=data%20science) in your system/user python profile (not a virtual environment).

    ```bash
    $ pip install --user cookiecutter
    ```

2. Surf the file system until your code folder (e.g. `path/to/repos_folder`). This is the parent folder of your code.
**NB: cookiecutter will create a new folder `project_name` with everything inside. Your actual code will be in a subfolder, i.e. `path/to/repos_folder/project_name/src/`**
Then run `cookiecutter` with the link to the  [data-science-template](https://github.com/drivendata/cookiecutter-data-science) and prompt the question it will ask you:

    ```bash
    $ cd Documents/xxx/xxx/Code/
    $ cookiecutter https://github.com/drivendata/cookiecutter-data-science
    # fill the question using project name: project_name
    # then it will ask you about the author's name, the license, the python interpreter, a brief description of the project.
    # once it is finished, cd the forder project_name
    $ cd project_name
    ```
    **From now on, our current directory will be `path/to/project_name/`** unless specified
    
    
 Project Organization
 ------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


 --------


### Virtual Environment pt1
3. set up a virtual environment, named `venv`, specifying the python version.
   This code will create a folder named `venv` containing lot of things and a **local copy of all the packages** you will pip-install from now on.

    ```bash
    $ virtualenv venv -p python3
    ```

4. edit the `.gitignore`  by adding the virtualenv's folder with you favorite text editor or just run the following command

    ```bash
    $ echo venv >> .gitignore
    ```
5. if you use conda:
   ```bash
   $ conda create -n venv python=3 
   ```

### GIT
5. set up git and link it to a new github reporitory:
    1. On [github.com](https://github.com/) create an **empty** reporitory online (it means no README and no license. If you do so it will display usefull command).
    2. Start git locally and synch it with the following commands:

    ```bash
    $ git init
    # check we are not 'saving' wried files
    $ git status
    # if so, commit
    $ git add .
    $ git commit -m "first commit"

    # If github
    $ git remote add origin https://github.com/USER/project_name.git

    $ git push -u origin master
    # avoid writing login and password for the future time
    $ git config credential.helper store
    ```
    3. If you have Windows use GitHub Desktop
    
### Virtual Environment pt2
6. Activate the virtualenv

    ```bash
    [user@localhost] project_name/ $ source venv/bin/activate
    # check that it is activated. You should have (venv) at the beginnig of your command line
    (venv) [user@localhost] project_name/ $
    ```
    if you use conda you don't have to care to be in the right folder:
    ```bash
    $ conda activate venv
    (venv) $
    ```

 7. Install the basic dependencies of cookiecutter (if you want). Notice that doing so also you will install the src 
     package by default. Then install your everyday-coding-favorite-life packages: numpy, matplotlib, jupyter

    ```bash
    (venv) $ pip install -r requirements.txt
    (venv) $ pip install numpy matplotlib jupyter
    ```
    You can also inatall the src package as editable

    ```bash
    $ pip install -e .
    ```

8. Freeze the requirements ('>' overwrite, '>>' append)

    ```bash
    (venv) $ pip freeze >> requirements.txt
    ```

9. Install the package for a toy example

    ```bash
    (venv) $ pip install sklearn
    ```

10. in `src/` create the `main.py` file and paste the following code:

    ```python
    from numpy.random import permutation
    from sklearn import svm, datasets

    C = 1.0
    gamma = 0.7
    iris = datasets.load_iris()
    perm = permutation(iris.target.size)
    iris.data = iris.data[perm]
    iris.target = iris.target[perm]
    model = svm.SVC(C, 'rbf', gamma=gamma)
    model.fit(iris.data[:90],
            iris.target[:90])
    print(model.score(iris.data[90:],
                    iris.target[90:]))
    ```

11. commit the changes

    ```bash
    $ git add .
    $ git commit -m 'toy svm'
    ```

12. edit the `models/train_model.py` and `models/predict_model.py` files. I
In both of the files (actually python modules) create new function respectively
    In `./src/models/train_model.py`:
    ```python
    from sklearn import svm
    def train(data, target, C, gamma):
        clf = svm.SVC(C, 'rbf', gamma=gamma)
        clf.fit(data[:90],
                target[:90])
        return clf
    ```
    In `./src/models/predict_model.py`:
    ```python
    def predict(clf, data, target):
        return clf.score(data, target)
    ```

13. Update the main file in order to import with the following imports
    In `src/main.py` add:
    ```python
    from models.predict_model import predict
    from models.train_model import train
    ```

    Now The main code should looks like:

    ```python
    # std imports
    from numpy.random import permutation
    from sklearn import datasets
    # my imports
    from models.predict_model import predict
    from models.train_model import train

    C = 1.0
    gamma = 0.7
    iris = datasets.load_iris()
    per = permutation(iris.target.size)
    iris.data = iris.data[per]
    iris.target = iris.target[per]
    model = train(iris.data[:90], iris.target[:90], C, gamma)
    score = predict(model, iris.data[90:], iris.target[90:])
    print(score)
    ```

14. Run and debug

    ```bash
    (venv) $ python src/main.py
    ```

### Sacred
15. PIP-install [Sacred](https://github.com/IDSIA/sacred) for tracking experiments

    ```bash
    (venv) $ pip install sacred pymongo
    ```

16. create a new function for the parameters C and gamma and add the colorators for Sacred

    ```python
    #...add here the new nice imports and add the followings
    from sacred import Experiment
    ex = Experiment('iris_svm') # id of the experiments

    @ex.config
    def cfg():
        C = 1.0
        gamma = 0.7

    @ex.automain
    def run(C, gamma):
        # ...
        # ... paste here the main
        #...
        return score
    ```

17. run it from the project's root directory

    ```bash
    (venv) $ python src/main.py
    ```

### MongoDB and Omniboard

18. install mongodb in your system. In a new terminal

    ```bash
    $ sudo dnf install mongodb mongodb-server mongoose
    # start service
    $ sudo service mongod start
    # verify it is woring
    $ mongo  # it will start the mongo-db-shell
    ```

19. Run and re-run as many time as you want the code with the database flag:

    ```bash
    (venv) $ python src/main.py -m MY_IRIS_EXP
    ```
    notice how the ID value increase at each run.
    Now we have also an "observer" to our sacred experiment. 

21. In a mongo shell (just run mongo in the command line) check if the MY_IRIS_EXP database exists

    ```bash
    $ mongo
    # after in the mongo shell
    > show dbs
    # look for MY_IRIS_EXP entry
    ```

22. download and install [Ominboard](https://github.com/vivekratnavel/omniboard), the sacred+mongo frontends 
    N.B. npm is a Javascript package manager. You will probably need to install it (https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

    ```bash
    # in a new terminal
    $ sudo npm install -g omniboard
    ```

23. In the same shell run the server listener

    ```bash
    $ omniboard -m localhost:27017:MY_IRIS_EXP
    ```

24. go to [http://localhost:9000](http://localhost:9000) to access omniboard frontends:

25. play with it

### Experiment metrics and omniboard visualization

26. add a metric in the main.py file add

    ```python
    @ex.automain
    def run(C, gamma):
        ... # the code before
        ex.log_scalar("val.score", score)
        return score
    ```

27. And what about a typical loss fuction in a for loop?
    for instance add the following line.
    We need to pass the object `_run` at the `main()`

    ```python
    @ex.automain
    def run(_run, C, gamma):
        ... # the code before
        my_loss = 0
        for i in range(20):
            # Explicit step counter (0, 1, 2, 3, ...)
            # incremented with each call for training.accuracy:
            _run.log_scalar("training.loss", my_loss, i)
            my_loss += 1.5*i + np.random.random(1)
        return score
    ```

1. run some experiments

1. play in omniboard
