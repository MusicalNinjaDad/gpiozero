ARG DEBIAN=debian
FROM mcr.microsoft.com/devcontainers/base:${DEBIAN}
ARG PYVERSION=3

# ---
# Add testing repo to get latest versions of tools
COPY <<EOF /etc/apt/sources.list.d/testing.list
deb http://deb.debian.org/debian testing main
EOF

# ---
# Install Python
RUN apt update \
&& apt install -y --no-install-recommends \
    python$PYVERSION \
    python$PYVERSION-distutils \
    python$PYVERSION-venv \
    python3-pip \
&& rm -rf /var/lib/apt/lists/* \
&& rm /etc/apt/sources.list.d/testing.list \
&& ln -s /usr/bin/python$PYVERSION /usr/bin/py

# ---
# Install tools needed for building docs
RUN apt update \
&& apt install -y --no-install-recommends \
    graphviz \
    inkscape \
    latexmk \
    texlive-fonts-recommended \
    texlive-latex-recommended \
    texlive-latex-extra \
    texlive-xetex \
    xindy \
&& rm -rf /var/lib/apt/lists/*