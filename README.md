# UrbanFireRobot
RBECapstone

## Overview

This repository contains the code and resources for the UrbanFireRobot project, developed as part of the RBECapstone. The project utilizes ROS 2 Jammy for robotic control and simulation.

## Setup Instructions

### Using Docker

To set up the ROS 2 Jammy environment using Docker, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/UrbanFireRobot.git
    cd UrbanFireRobot
    ```

2. **Build and run the Docker container**:
    ```sh
    docker-compose up --build
    ```

This will build the Docker image and start a container with the ROS 2 Jammy environment. The `ros2_ws` folder in the repository will be mounted into the container at `/root/ros2_ws`.

### Native Linux Setup

To set up the ROS 2 Jammy environment natively on a Linux machine, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/UrbanFireRobot.git
    cd UrbanFireRobot
    ```

2. **Run the setup script**:
    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

This script will install ROS 2 Jammy and set up the workspace in `~/ros2_ws`.

## Workspace Structure

- `ros2_ws`: The ROS 2 workspace where all packages and code for the project are located.

## Contributing

Please follow the standard GitHub flow for contributing:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.