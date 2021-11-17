### COVID-19 Virus Spread Web App

### Getting started

1. Creating a virtual environment

- To create a virtual environment inorder to install packages using `pip` we are going to open the `cwd` with a command line and run the following command in sequence.

- create a virtual environment folder and navigate to it

```shell
mkdir venv && cd venv
```

- run the following command to initialize the virtual environment

```shell
virtualenv .
```

- activate the virtual environment using the following command and navigate to the project folder

```shell
.\Scripts\activate && cd ..
```

### Package installations

We are going to install all the packages that we are going to use in this project.

1. flask

```shell
pip install flask
```

2. folium

```shell
pip install folium
```

3. pandas

```shell
pip install pandas
```

4. request

```shell
pip install requests
```

5. beautifulsoup

```shell
pip install beautifulsoup4
```

### Requirements

Packages that are required for this project was extracted using the following command:

```shell
pip freeze > requirements.txt
```

### Installing packages in the `requirements.txt` file

```shell
pip install -r requirements.txt
```

### Data visualization

For data visualization in the DOM using the flask templates, we are going to use the [chart.js](https://www.chartjs.org/) which is an open source javascript library for displaying charts on canvases.

We are going to add the following CDN in the `base.html` file.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js"></script>
```
