## Serverless Python FastApi    

Aplicacion Base desarrollada con serverless, python y fastapi.


Para el desarrollo de las funciones serverless estaremos utilizando serverless framework por lo que para ello debemos tener los siguientes programas instalados:

 

- Node JS: https://nodejs.dev/
- Serverless: https://www.serverless.com/framework/docs/getting-started#via-npm
- Python: https://www.python.org/downloads/
- AWS-CLI: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html



tambien utilizaremos python como lenguaje principal, las funciones pueden ser probadas de forma local pero se recomienda hacer pruebas en ambiente de desarrollo AWS para verificar que las librerías python requeridas se instalen correctamente durante el despliegue gestionado por serverless.

 
## Preparación de ambiente local:

Serverless framework (en adelante sls) ofrece herramientas de administración y monitoreo a funciones serverless. 

En caso de se quiera tener acceso al dashboard de sls, se debe iniciar sesión a través del siguiente comando:


```
sls login
```


Para que sls tenga acceso a las herramientas de amazon se debe iniciar sesión en amazon a través de la línea de comandos de AWS-CLI


```
aws configure
```
 
---
**Dato:**

Para mayor detalle de como configurar la sesión de aws revisar la siguiente documentación: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

---
 

 
## Deploy en AWS:

Para hacer deploy en AWS con Serverless se debe ejecutar el siguiente comando:

Activar el entorno local de python e instalar las librerias:

```
virtualenv venv --python=python3     
. venv/bin/activate     
```

Ejecucion de deploy:

```
sls deploy    
```

---
**Dato:**
En caso de querer activar el dashboard de serverless, se deben actualizar las dos primeras lineas de serverless.yml con los datos de la organizacion y la app que corresponde

```
org: setterlee
app: serverless-python-fastapi
```

O en caso de querer usar el dashboard de serverless, se deben remover las lineas. 

---


## Ejecución local:

El proyecto se puede correr de forma local ejecutando los siguientes comandos:

Activar el entorno local de python e instalar las librerias:

```
virtualenv venv --python=python3     
. venv/bin/activate     
```

Instalacion de libreria uvicorn
```
pip install uvicorn
```

Ejeucion de la aplicacion:
```
uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
```