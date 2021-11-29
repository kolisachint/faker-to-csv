FROM ubuntu:20.04

COPY . /app

# Ensure apt is in non-interactive to avoid prompts
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update  \
  && apt-get -y install --no-install-recommends python3.9-minimal python3-pip git ssh \
  && apt-get autoremove -y && apt-get clean -y  \
  && rm -rf /var/lib/apt/lists/*  \
        /tmp/* \
        /var/tmp/* \
        /usr/share/man \
        /usr/share/doc \
        /usr/share/doc-base \
  && chmod -R 755 /app \
  && pip3 --disable-pip-version-check --no-cache-dir \
      install -r /app/requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]

EXPOSE 5000 8080 80 443


