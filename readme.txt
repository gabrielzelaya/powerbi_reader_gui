Power BI Dashboard Reader
Descripción
Power BI Dashboard Reader es una aplicación de Python que permite a los usuarios autenticar y leer dashboards de Power BI. Utiliza la API REST de Power BI para obtener información de los dashboards y tiles, y presenta estos datos en una interfaz gráfica de usuario creada con Tkinter.

Requisitos
Cuenta de Power BI: Debes tener una cuenta de Power BI con acceso a los dashboards que deseas leer.
Registro de Aplicación en Azure AD: Necesitarás registrar tu aplicación en Azure Active Directory para obtener las credenciales necesarias para la autenticación.
Python 3.x: Asegúrate de tener Python 3 instalado.
Bibliotecas de Python: Instala las siguientes bibliotecas necesarias:
requests: Para realizar solicitudes HTTP.
msal: Microsoft Authentication Library para Python.
tkinter: Para la interfaz gráfica de usuario (generalmente incluido en Python).
Instalación de Bibliotecas
Instala las bibliotecas necesarias utilizando pip:


pip install requests msal

Registro de Aplicación en Azure AD
Ve a Azure Portal.
Navega a "Azure Active Directory" > "Registros de aplicaciones" > "Nuevo registro".
Completa el formulario con los detalles de tu aplicación y toma nota del Application (client) ID y el Directory (tenant) ID.
En "Certificates & secrets", crea un nuevo secreto y guarda el valor.