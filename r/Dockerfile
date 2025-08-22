FROM rocker/r-ver:4.3.1
RUN R -e "install.packages(c('plumber','jsonlite'), repos='https://cloud.r-project.org')"
WORKDIR /app
COPY plumber.R /app/plumber.R
EXPOSE 8000
CMD ["R", "-e", "pr <- plumber::pr('/app/plumber.R'); plumber::pr_run(pr, host='0.0.0.0', port=8000)"]
