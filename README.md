# AWM_2

# AWM2 Project

AWM2 is a web-based application for managing and displaying restaurant data. It allows users to view a list of restaurants, including details like name, address, city, and more. The project is built using **Django** as the backend and **HTML, CSS, JavaScript** for the frontend.

## Features

- Display a list of restaurants fetched from the API
- View detailed information about a restaurant (name, address, city, etc.)
- Built with Django for the backend API
- Fully responsive and user-friendly frontend


## Installation

To run the project locally, follow these steps:

1. **Clone the repository** to your local machine:
    ```bash
    git clone https://github.com/yourusername/AWM2.git
    cd AWM2
    ```

2. **Set up a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations** to set up the database:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Usage

1. Open a web browser and go to `http://127.0.0.1:8000/`.
2. You should see the list of restaurants fetched from the backend API.
3. Click on any restaurant to view more details (if applicable).

## API Endpoints

Here are some key API endpoints for interacting with the restaurant data:

- **GET /api-v1/restaurants/**: Fetch all restaurants.
- **GET /api-v1/restaurants/<id>/**: Fetch a specific restaurant by ID.

## Development

If you would like to contribute to this project or make modifications, follow these steps:

1. **Fork the repository** to your GitHub account.
2. **Clone your fork** to your local machine:
    ```bash
    git clone https://github.com/yourusername/AWM2.git
    ```
3. **Create a new branch**:
    ```bash
    git checkout -b feature-name
    ```
4. **Make changes** and commit them:
    ```bash
    git commit -m "Description of changes"
    ```
5. **Push your changes** to your forked repository:
    ```bash
    git push origin feature-name
    ```
6. **Open a pull request** to the main repository.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used for the backend.
- [Leaflet](https://leafletjs.com/) - A JavaScript library for interactive maps (removed from this version).
- [Bootstrap](https://getbootstrap.com/) - For front-end components (if applicable).
  
