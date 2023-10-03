# ECE 252 Mock Backend Docker Image

Welcome to the ECE 252 Mock Backend Docker Image repository! This repository contains the code and Dockerfile to build a Docker image that serves as a mock backend for ECE 252 lab 2. This mock backend is designed to simulate the behavior of a real backend system, making it a valuable tool for testing and development.

## Table of Contents

- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

To get started with the ECE 252 Mock Backend Docker Image, follow these steps:

### Prerequisites

Before you begin, ensure you have the following prerequisites:

- Docker installed on your system. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

### Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/RyEggGit/ece-252-mock-backend.git
```

### Build the Docker Image

Navigate to the cloned repository directory and use the following command to build the Docker image:

```bash
docker build -t mock-ece-252 .
```

### Run the Docker Container

After the image is built, you can run a Docker container using the following command:

```bash
docker run -d -p 8080:8080 --name mock-backend mock-ece252
```

The mock backend will now be running inside a Docker container and listening on port 8080.

## Usage

To use the ECE 252 Mock Backend, you can send HTTP requests to it as if it were a real backend service. The mock backend will respond with simulated data or behavior that you can use for testing your frontend or other parts of your ECE 252 project.

You can access the mock backend by sending HTTP requests to `http://localhost:8080`, assuming you are running the Docker container locally. You can also adjust the port mapping as needed when running the container.

## Contributing

We welcome contributions to this repository. If you would like to contribute, please follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch for your contribution: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m "Add your changes"`.
4. Push your changes to your fork: `git push origin feature/your-feature-name`.
5. Create a pull request from your fork to this repository.

Please ensure that your code follows the project's coding standards and includes appropriate documentation for any new features or changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the ECE 252 Mock Backend Docker Image repository. If you have any questions or encounter any issues, please feel free to open an issue or reach out to the project maintainers. Happy coding!
