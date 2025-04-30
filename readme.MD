
<h1 align="center">Speech Polarity Detector</h2>



Speech Polarity Detector lets you detect sentimental of headlines from online News portals. You Paste your Newspaper link and Boom! You get your sentimental rate the headlines . 



<h2> Project Installation </h2>

<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/detect-speech.git
# After cloning, move into the directory 
# having the project files 
```

#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env

# Use this on Linux and Mac
python3 -m venv env
```

#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate

# Linux and Mac
source env/bin/activate

```

#### Install all the project Requirements

```bash

# Windows
pip install -r requirements.txt

# Linux and Mac
pip3 install -r requirements.txt

```

#### Run the Server


```bash
# RUN the development server

# Windows 
python manage.py runserver

# Linux & Mac 
python3 manage.py runserver

```


The installation guide is Done here. Please follow the Documention Section for API ENDPOINTS .

<h2>Project Tree </h2>

```bash 

    backend_config/  #Root Config folder
        |-- __init__.py
        |-- settings.py # All the settings 
        |-- urls.py (Root URL file)
        |-- wsgi.py
        |-- asgi.py

    speech_detector/
        |-- __init.py
        |-- models # database folder  
        |-- views 
        |-- detect.py # Detector Logic File
        |-- serializers.py 
        |-- urls.py # URL file
        |-- admin.py

    |-- requirements.py # Requirements file for project
    |-- .gitignore
    |-- readme.md
    
```

<h2>Project Documentation</h2>


> The codes of these features are well documented and we can get more info by reading them.

<h3>API ENDPOINT </h3>

To `Detect Sentimental Speech` from newspaper headlines, we need to follow the endpoint Below 
.We can use these `Three` popular news portal for test . <br>
`https://www.prothomalo.com/` <br>
`https://www.kalerkantho.com/` <br>
`https://www.bd-pratidin.com/`

```bash

    # Method : Post
    http://localhost:8000/api/v1/speech-detect/

```

> Payload to see the result 

```bash

    # Copy one of the following 
    {
        "web_url" :"https://www.prothomalo.com/"
    }

    ##

    {
        "web_url" :"https://www.kalerkantho.com/"
    }

    ##

    {
        "web_url" :"https://www.bd-pratidin.com/"
    }

    # Or you can use your own Url to check 

```

> The Result should look like this 

```bash

    {
        "Result": {
            "Headline": "এখনো তৎপর মালয়েশিয়ার সিন্ডিকেট",
            "Detect": "Neutral"
        }
    }


```

<h2> Thanks for your time for reaching this far </h2>
If you have any modification or discussion , you can connect me at once .

mail : nazrulislamyeasin@gmail.com <br>
Thanks
