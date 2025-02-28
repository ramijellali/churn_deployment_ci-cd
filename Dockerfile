# Use the official Jenkins base image
FROM jenkins/jenkins:2.492.1-jdk17

# Switch to root user to install dependencies
USER root

# Install apt utilities
RUN apt-get update && apt-get install -y lsb-release

# Add Docker's official GPG key and repository
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Install Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Switch back to the Jenkins user
USER jenkins

# Install required plugins for Jenkins (Blue Ocean and Docker Workflow)
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
