# YouTube Downloader
## Summary
This application is developed using the _streamlit_ Python package.
It enables the downloading of YouTube videos. The videos can be downloaded as audio
only in the .mp3 format or as the full video in .mp4 format. Below is an image
of the application while running:

![Screenshot of Application](resources/img_1.png)

## Deployment details
- Application is deployed to a private Linode server
- Deployment is handled by a GitHub Actions CI/CD pipeline
- The CI/CD workflow can be seen [here](.github/workflows/pipeline.yml)

## Starting development environment
1. Navigate to the project directory in the terminal
2. Run `streamlit run src/main.py --server.port 8502`
3. The application should now be visible at `http://localhost:8502`

## Building and running Docker image
1. Navigate to the project directory in the terminal
2. Run `docker build -t youtube-downloader .`
3. Once the image is built, run `docker run -d -p 8502:8502 youtube-downloader`
4. The application should be visible at `http://localhost:8502` once the Docker container spins up