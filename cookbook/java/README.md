# Java Cursor Setup

Quick setup for Java development in Cursor.

## Prerequisites

1. Install JDK 17 or later:
   - Windows: Download from [Oracle](https://www.oracle.com/java/technologies/downloads/) or use `winget install Microsoft.OpenJDK.17`
   - Mac: `brew install openjdk@17`
   - Linux: `sudo apt install openjdk-17-jdk`

2. Install Build Tools:
   - Maven:
     - Windows: Download from [Maven](https://maven.apache.org/download.cgi) or use `winget install Apache.Maven`
     - Mac: `brew install maven`
     - Linux: `sudo apt install maven`
   - Gradle:
     - Windows: Download from [Gradle](https://gradle.org/install/) or use `winget install Gradle.Gradle`
     - Mac: `brew install gradle`
     - Linux: `sudo apt install gradle`

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

## Project Structure
- Maven example: `./maven/`
- Gradle example: `./gradle/`

## Project Setup

### Maven Project
1. Ensure Maven is installed: `mvn --version`
2. Navigate to the Maven project: `cd maven`
3. Generate Maven wrapper: `mvn -N wrapper:wrapper`
4. Make wrapper executable: `chmod +x mvnw`
5. Clean and test project: `./mvnw clean test`

### Gradle Project
1. Ensure Gradle is installed: `gradle --version`
2. Navigate to the Gradle project: `cd gradle`
3. Generate Gradle wrapper: `gradle wrapper`
4. Make wrapper executable: `chmod +x gradlew`
5. Clean and test project: `./gradlew clean test`

## Running Tests

### Maven Tests
1. Command Line:
   - `./mvnw test` - Runs tests
   - `./mvnw clean test` - Cleans and runs tests

2. Cursor Tasks (Cmd/Ctrl + Shift + P):
   - `Run Test Task` - Runs Maven tests
   - `Maven Test` - Runs only tests
   - `Maven Clean Test` - Cleans and runs tests

### Gradle Tests
1. Command Line:
   - `./gradlew test` - Runs tests
   - `./gradlew clean test` - Cleans and runs tests

2. Cursor Tasks (Cmd/Ctrl + Shift + P):
   - `Run Test Task` - Runs Gradle tests
   - `Gradle Test` - Runs only tests
   - `Gradle Clean Test` - Cleans and runs tests

### Test Explorer
Both Maven and Gradle projects can use the Test Explorer view to:
- Run individual tests
- Debug tests
- View test results
- Generate test coverage reports

## Running the Application

### Maven
```bash
./mvnw spring-boot:run
```

### Gradle
```bash
./gradlew bootRun
```

Both projects include:
- Basic REST endpoint at `http://localhost:8080/hello`
- Integration tests with MockMvc
- Debug configurations

## Integration Tests
Both projects include comprehensive integration tests that verify:
1. Basic endpoint functionality
2. Content type headers
3. Error handling (404 cases)
4. Response validation

You can find the test files at:
- Maven: `maven/src/test/java/com/example/demo/HelloControllerTest.java`
- Gradle: `gradle/src/test/java/com/example/demo/HelloControllerTest.java`