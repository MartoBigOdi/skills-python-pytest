# Proyecto, Framework de Pytest-Selenium 🐍 🚀🛸

<img src="img_readme/pytest -selenium-python.png"/>

> #### Requiriments.txt ‍💻
>
> -  Instalar con pip
> 

## IDE Pycharm 
<img height="50" src="img_readme/pycharm.png" width="50"/>

> #### Comandos 👨 🏻 ‍💻
>
> - pytest nombreArchivo.py
> - pytest --collect-only ----> Para correr los archivos que empiecen con "test_" dentro del proyecto.
> - pytest -k 'test_first_url' --collect-only ----> Corremos solo el mark para esa funcion.
> - pytest -k asdict or defaults' --collect-only ----> Ejecuta solamente lo que le enviamos por parametro para elegir las funciones de test
> - pytest -v -m ejecutar ----> ejecutamos test por tags, si no son tags de pytest y son propias de nuestro sistema, personalizadas guardar en el pytest.ini
> 
<img src="img_readme/marcas_propias_archivo_ini.JPG"/>
<img src="img_readme/marca sobre la funcion de test.JPG"/>
<img src="img_readme/error como se ve, solo se tiene que modificar el expected.JPG"/>

## Reporte
> ```
> Generamos reportes con el siguiente comando, por el momento solo generamos de los test que encuentra en el archivo que le indicamos 💾
> pytest test_webElements.py --html=ReporteTests.html ----> En este archivo solo existe un test de front 
> ```

<img src="img_readme/reporte html pytest.JPG"/>

> #### Archivos 💾
>
> - Para que ejecute los test y asi mismo pytest pueda identificar el tag/mark el archivo debe tener un nombre valido.
> - ejemplo test_elementofront.py; test_frontventa.py; test_backventa.py.
> 