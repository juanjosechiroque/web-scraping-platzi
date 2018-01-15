# Web Scraper de Platzi

Es una aplicación de consola, hecha en python, que extrae algunos datos publicos que se encuentra en la web de Platzi

* El listado de las carreras
* El listado de los cursos
* Las imagenes de los cursos

## Cómo funciona:

El listado de las carreras y de los cursos, se almacenarán en 2 archivos de texto: careers.txt y courses.txt. 
Por otro lado, las imagenes de los cursos se descargarán en una carpeta llamada *img*

La información extraida se encuentra en https://platzi.com/cursos/


## Librerias utilizadas:
* [Request](http://docs.python-requests.org/en/master/) - Para realizar las llamadas HTTP
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Para manipular los resultados de las llamadas HTTP

Además, para ejecutar la aplicación se utilizó un entorno virtual. Para ello, se instaló:
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) - Para crear el entorno virtual de desarrollo 
* [PIP](https://pip.pypa.io/en/stable/installing/) - Como manejador de paquetes

## Ejecución

Abrir una consola en la carpeta del proyecto y ejecutar los siguiente comandos:

1. Inicializar el entorno virtual venv 
```
source venv/bin/activate
```

2. Ejecutar el web scraper
```
python main.py
```

**Nota**: El proceso puede tomar un par de minutos porque se descargarán en promedio más de 120 imágenes


## Autor

**Juan José Chiroque** - [LinkedIn](https://www.linkedin.com/in/jjchiroque)
