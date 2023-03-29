La aplicación web desarrollada en Django, BaseWatch, ofrece una plataforma para registrar y administrar información sobre proyectos, tipos de proyectos y sus costos asociados.
En la aplicación, los super usuarios tienen la capacidad de crear una cuenta, iniciar sesión y agregar información sobre cada proyecto, incluyendo su ID, el tipo de proyecto llevado a cabo en la comuna o región, la fecha en la que se ejecutó en terreno, y el costo total asociado, entre otros detalles relevantes. Los usuarios también pueden visualizar una lista completa de todos los proyectos en los que se han trabajado.
Además, la aplicación permite la administración integral de cada proyecto, lo que incluye el registro de nuevos proyectos, la visualización de estadísticas y la generación de gráficos para analizar sus costos. La aplicación utiliza diversas herramientas y librerías, como pandas y django-import_export, para el procesamiento y manejo de datos provenientes de SQLite. Se espera que en un futuro cercano se incluya la librería matplotlib para facilitar la visualización gráfica de los mismos.

## Vista previa de BaseWatch
Página de inicio posee información acerca de lo que se lleva a cabo en la aplicación.
![image](https://user-images.githubusercontent.com/72874155/228393182-0e742a66-0f88-4b69-9097-fdc7d89eb075.png)

La siguiente vista muestra algunas de las funcionalidades disponibles en el dashboard. Estas funcionalidades se han incorporado como aplicaciones en un entorno web y se han diseñado para ser amigables e intuitivas. Por ejemplo:

- Se ha añadido una sección para agregar manualmente un proyecto si se desea.
- Se ha agregado una sección para subir múltiples proyectos en formato *.csv.
- Se ha incorporado una sección con doble funcionalidad, que permite editar secciones específicas del proyecto y eliminar el proyecto por completo en caso de haber cometido un error.
- Se ha agregado un paginador para revisar los datos y evitar sobrecargar la página con todo el listado.

Nota: Los primeros números correspondientes al ID asociado al proyecto se han eliminado por motivos de copyright.

![image](https://user-images.githubusercontent.com/72874155/228393934-28d8c516-08a4-4e2a-8b60-e8bd7883d0c9.png)
