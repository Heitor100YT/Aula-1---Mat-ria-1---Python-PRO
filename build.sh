jobs:
  deploy-and-release:
    name: Deploy and release in BotCity.
    runs-on: ubuntu-latest
    steps:
      # Checking out the project.
      - uses: actions/checkout@v4
      # Implemented executable permission to build.sh
      - name: Get permission to build.
        run: chmod +x build.sh
      # Execute the build script to compile the project
      - name: Execute to build.
        run: ./build.sh
