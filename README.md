# IFC19 - India Fights COVID19

**IMPORTANT UPDATE**  

After keeping you updated with Covid-19 information for the last 18 months, **`covid19india.org`** API will be stopping it's operations on **31st October, 2021**.

**IFC19 will be online post 31st October, but with the last available data.**

Read more here [https://blog.covid19india.org/2021/08/07/end/](https://blog.covid19india.org/2021/08/07/end/)

### 👋👋 IFC19 webapp version 2.0 is here! | August 2021 
ICF19 no longer uses the Django framework. <br>
It now runs on Streamlit - an open-source Python library that <br>
makes it easy to create and share beautiful, custom web apps <br> 
for machine learning and data science.

The old website (https://indraneel.pythonanywhere.com/) is now deprecated and allows users to visit the new version. <br> 
The Streamlit hosted app is available at https://share.streamlit.io/ineelhere/ifc19/2.0/ifc19_app.py

#### New features in this release
* More visualizations - interactive and downloadable
* Download all the data in csv format as desired
* COVID19 Vaccination data for India is added
* Truly open-source and reproducible, no secrets!
* Also available inside a container (docker) for easy use/deployment accross different platforms - https://hub.docker.com/repository/docker/ineelhere/ifc19

#### How to run via `docker`-
* Pull the docker using the command `docker pull ineelhere/ifc19`
* Run the same using the command `docker run ineelhere/ifc19`
* If not automatically redirected, open your browser and go to http://172.17.0.2:8501/ (This might be different on your system. However, the port will always be `8501`)
* You might need to use `sudo` or grant relevant permissions before the above commands in case you find the error - `Got permission denied`.

<hr>

### 👉👉 IFC19 webapp version 1.0 | May 2020
With a background in Biotechnology and Bioinformatics, I wanted to expand my knowledge and skillsets in data science programming and web development. While I was self-learning my way out, I was inspired by the several COVID19 dashboards that were coming up from several sources worldwide. So, I thought of creating a similar website myself as a part of the learning process and here is the result!

The data is being pulled from the crowdsourced API provided by the covid19india.org. The relevant data is then cleaned up and processed using python. The results are then presented on the website using Django framework.

So, long story short — I have created a website that displays real-time data and statistics along with other information regarding the COVID19 situation in India. This project is fully a personal endeavor. It has not been done under any sort of external influence or funding or sponsorship. Please visit the website and provide feedback on the same.

Website URL - https://indraneel.pythonanywhere.com/ 
