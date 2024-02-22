<div align="center">
  <img src="https://grow.empress.eco/uploads/default/original/2X/1/1f1e1044d3864269d2a613577edb9763890422ab.png" alt="Attachments on Nextcloud Logo" />
  <h1 align="center">Simplify and Secure Your Data Backup with Nextcloud</h1>
  <p align="center">
    This custom app for Nextcloud automates your data backup processes, enhancing data security and organization.
    <br />
    <a href="https://empress.eco/">Project Website</a>
    ·
    <a href="https://github.com/empress-eco/nextcloud_attachments/issues">Report Bug</a>
    ·
    <a href="https://github.com/empress-eco/nextcloud_attachments/issues/new">Request Feature</a>
  </p>
</div>

## About The Project

Attachments on Nextcloud is a custom app that enables you to backup your database, config, and files to your Nextcloud instance seamlessly. With options for daily or weekly backups, you can customize a backup schedule that best suits your workflow, ensuring your data is always secure and accessible.

### Key Features

- Automated backups to your Nextcloud instance
- Customizable backup frequency (daily or weekly)
- Backup notifications via email
- Backup of public and private files along with the database

## Technical Stack and Setup Instructions

Attachments on Nextcloud is built on Framework. 

### Installation

Get started by cloning the repository and installing the app on your site:

```sh
bench get-app https://github.com/empress-eco/nextcloud_attachments.git
bench --site {site_name} install-app attachments_on_nextcloud
```

### Configuration

After successful installation, navigate to **Nextcloud Settings** in the **Awesome Bar**. Here, you can input your account details and configure your backup preferences. 

Once your configuration is saved, click on the **Backup Now** button to initiate a backup. The process duration can range from a few minutes to half an hour, depending on your backup size.

## Usage

Attachments on Nextcloud is designed to simplify your backup process. After installation and configuration, the app will automatically backup your data at the frequency you've chosen. You will receive email notifications for each backup, keeping you updated on your data security.

## Contribution Guidelines

We welcome and appreciate contributions! Here's how you can contribute:

- Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## License and Acknowledgements

This project is licensed under the MIT License. Your contributions are also licensed under the same.

Special thanks to the Empress Community for their foundational contributions to this project. Their innovative tools and dedicated support have been instrumental in making this project possible. We are profoundly grateful for their pioneering work and ongoing support. 

Also, our gratitude extends to the [Empress](https://empress.eco/) team for their continuous support and contributions.