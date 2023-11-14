The web application developed in Django, BaseWatch, provides a platform for registering and managing information about projects, types of projects, and their associated costs. In the application, superusers have the ability to create an account, log in, and add information about each project, including its ID, the type of project carried out in the municipality or region, the date it was implemented on-site, and the total associated cost, among other relevant details. Users can also view a complete list of all the projects they have worked on. Additionally, the application allows comprehensive project management, including the registration of new projects, the display of statistics, and the generation of charts to analyze their costs. The application uses various tools and libraries, such as pandas and django-import_export, for processing and handling data from SQLite. It is expected that in the near future, the matplotlib library will be included to facilitate graphical visualization of the data.

## Homepage Preview
Homepage contains information about what takes place in the application.
![image](https://user-images.githubusercontent.com/72874155/228393182-0e742a66-0f88-4b69-9097-fdc7d89eb075.png)

The Options view is expanded, allowing us to see information based on the type of project.
![image](https://user-images.githubusercontent.com/72874155/228394764-20865288-baac-4e32-9118-119f654466dd.png)


The following view displays some of the functionalities available in the dashboard. These functionalities have been incorporated as applications in a web environment and have been designed to be user-friendly and intuitive. For example:

- A section has been added to manually add a project if desired.
- A section has been added to upload multiple projects in *.csv format.
- A dual-functionality section has been incorporated, allowing for the editing of specific project sections and the complete deletion of the project in case of an error.
- A paginator has been added to review the data and avoid overloading the page with the entire listing.

Note: The initial numbers corresponding to the project's associated ID have been removed for copyright reasons.

![image](https://user-images.githubusercontent.com/72874155/228393934-28d8c516-08a4-4e2a-8b60-e8bd7883d0c9.png)

View to add a project, displaying the fields that need to be completed to upload a project.
![image](https://user-images.githubusercontent.com/72874155/228401121-5b75aa9e-9b64-464d-9401-6559ef21a208.png)

"Upload Projects" view where a *.CSV file containing multiple projects will be loaded, and our application will be able to detect all fields and automatically fill them in.
![image](https://user-images.githubusercontent.com/72874155/228401348-57d843cd-9dcd-48dd-9c1f-5eaec1cee4e4.png)


