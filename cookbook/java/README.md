# Java Cursor Setup

Quick setup for Java development in Cursor.

## Prerequisites

1. Install JDK 17 or later:
   - Windows: Download from [Oracle](https://www.oracle.com/java/technologies/downloads/) or use `winget install Microsoft.OpenJDK.17`
   - Mac: `brew install openjdk@17`
   - Linux: `sudo apt install openjdk-17-jdk`

2. Install Maven:
   - Windows: Download from [Maven](https://maven.apache.org/download.cgi) or use `winget install Apache.Maven`
   - Mac: `brew install maven`
   - Linux: `sudo apt install maven`

3. Configure Java 17:
   - Mac/Linux: Create symlink and add to PATH:
     ```bash
     sudo ln -sfn /usr/local/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
     export PATH="/usr/local/opt/openjdk@17/bin:$PATH"
     ```

4. Install Required Extensions:
   Cursor will automatically suggest installing the recommended extensions when you open the project. You can also install them manually:

   Required Extension Packs:
   - Java Extension Pack (`vscjava.vscode-java-pack`) - Includes Language Support for Java™ by Red Hat and other essential Java extensions
   - Spring Boot Extension Pack (`vmware.vscode-spring-boot-pack`) - Includes Spring Boot tools and extensions

   IntelliSense Enhancement:
   - Visual Studio IntelliCode (`VisualStudioExptTeam.vscodeintellicode`) - AI-assisted IntelliSense with context-aware code completions

## Project Structure
- Maven example: `./maven/`
- Gradle example: `./gradle/`

## Maven Project Setup
1. Ensure Maven is installed: `mvn --version`
2. Navigate to the Maven project: `cd maven`
3. Generate Maven wrapper: `mvn -N wrapper:wrapper`
4. Make wrapper executable: `chmod +x mvnw`
5. Clean and test project: `./mvnw clean test`

## Running Tests
You can run tests in several ways:

1. Cursor Tasks (Cmd/Ctrl + Shift + P):
   - `Run Test Task` - Runs Maven tests
   - `Maven Test` - Runs only tests
   - `Maven Clean Test` - Cleans and runs tests

2. Command Line:
   - `./mvnw test` - Runs tests
   - `./mvnw clean test` - Cleans and runs tests

3. Test Explorer:
   - Use the Test Explorer view to run individual tests

## Quick Start
1. Open either project folder
2. Wait for dependencies to download
3. Run `Main.java`
4. Run tests with Test Explorer

Both projects include:
- Basic REST endpoint at `http://localhost:8080/hello`
- Unit tests
- Debug configurations