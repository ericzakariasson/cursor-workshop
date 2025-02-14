# C#

## Setup

1. Install .NET SDK

### macOS

```bash
brew install dotnet
```

### Windows

Download and install from [.NET download page](https://dotnet.microsoft.com/download)

### Linux

#### Ubuntu/Debian

```bash
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update
sudo apt install dotnet-sdk
```

#### Fedora/RHEL

```bash
sudo dnf install dotnet-sdk
```

## Debugging

> [!IMPORTANT]
> Visual Studio Code officially supports .NET debugging only with its proprietary `vsdbg` tool, which is limited to Visual Studio Code, Visual Studio Code Insiders, and Visual Studio products. This solution explores an alternative approach using Samsung's open-source `netcoredbg` tool.

For debugging with breakpoints in Cursor, we use Samsung's open-source `netcoredbg` tool. This requires building the debugger from source to ensure compatibility with your system architecture.

[Follow the detailed community setup guide](https://github.com/dgokcin/dotnet-cursor-debugging-with-breakpoints) for instructions on:

- Building netcoredbg from source
- Configuring launch.json
- Troubleshooting architecture-specific issues

We understand this is not the best experience, but it's the best we can do for now due to licensing restrictions.

## Tasks

Press `Cmd/Ctrl + Shift + P` and type "Run Task" to access available tasks:

- `restore`: Restore NuGet packages
- `build`: Build the solution
- `run`: Run the application
- `test`: Run unit tests

You can also use keyboard shortcuts:

- Build: `Cmd/Ctrl + Shift + B`
- Test: `Cmd/Ctrl + Shift + P` → "Run Test Task"
