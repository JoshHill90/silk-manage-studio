

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Silk Manage Studio</h3>

  <p align="center">
    An application for photographers to manage galleries and collaborate with clients.
  </p>
</div>
  <p align="center">
Project Link/Live Demo: <a href='https://portfolio.silkthreaddev.com/projects/silk-manage-studio.html'>Silk Manage Studio</a>
  </p>
<!-- ABOUT THE PROJECT -->
## About Silk Manage Studio

Silk Manage Studio is a web application designed to empower photographers with tools and capabilities for creating galleries from uploaded images and seamlessly sharing them with their clients. The ongoing development of Silk Manage Studio includes features for managing clients, projects, generating invoices using Stripe integration, and incorporating a calendar for event tracking.

### Built With

* Front-end:
  - JavaScript
  - HTML
  - CSS
  - Bootstrap
* Back-end:
  - Python
  - Django
  - MySQL
  - Planet Scale
  - Docker

<!-- GETTING STARTED -->
## Getting Started

1. Install Python 3 and Django:
   ```sh
   # Install Python 3 (if not already installed)
   sudo apt-get update
   sudo apt-get install python3

   # Install pip (Python package manager)
   sudo apt-get install python3-pip

   # Create env 
   sudo python3 -m venv {env_name}

   # Activate env 
   sudo source {env_name}/bin/activate

   # Install Django
   pip3 install Django

   # Install requirements.txt
   pip3 install -r requirements.txt

   # Install Planet scale componets
   cd a_main # the name of the project 
   sudo git clone https://github.com/planetscale/django_psdb_engine.git



Setting up project intergrations:

<br />
To run this project, you'll need to set up connections with Planet Scale. Ensure you have an account and create a database; all other connections are already in place. Match up the empty environment variables with the information from Planet Scale. For uploading images, you'll also need to create a Cloudflare account and sign up for their Image CDN. The API components responsible for batch upload, delete, and update tokens are through Cloudflare. Additionally, Cron tasks are stored within Cloudflare R2 storage, which is an S3-compatible storage system. However, you can substitute any other S3 bucket credentials since this project uses boto3 to connect.

Stripe integration has been added but is only in a testing capacity. You'll need to create a Stripe account and set up access keys for the test account. The application also needs to send emails, so SMTP Host, email, and password are required. Note that PM_EMAIL_PORT='587' is the needed port regardless of SMTP information given by the provider. Please refer to tempEnv.txt, fill in all values with the correct information to start the application.

### Project Setup

Silk Manage Studio is configured across two Django applications: one for user content management and the other serving as a separate API endpoint for external communication with the client-facing site. The project utilizes a unified database using a planet-scale SQL server, allowing users to create, manage, and display galleries seamlessly. Both applications are containerized using Docker Compose and run from a VPS, with a containerized Nginx reverse proxy hosting the sites. This setup facilitates efficient management of the deployment pipeline and ensures consistency.

<!-- CURRENT FEATURES -->
## Current Features

- Upload up to 60 images at a time
- Create and share galleries
- Manage gallery images
- Utilize tags for efficient searching
- Manage gallery display settings

<!-- FEATURES IN TESTING -->
## Features in Testing

- Manage clients and invitations
- Create and manage projects
- Generate and manage invoices (Stripe integration)
- Calendar functionality with event tracking and invites
- Further customization of gallery display settings

<!-- CONTRIBUTING -->
## Contributing

No contributions at this time

<!-- CONTACT -->
## Contact

For any inquiries or assistance, feel free to contact Josh at Josh@silkthreaddev.com


