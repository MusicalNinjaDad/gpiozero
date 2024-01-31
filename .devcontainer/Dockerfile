ARG DEBIAN=debian
FROM debian:${DEBIAN}
ARG PYVERSION=3

# ---
# Install Python
RUN apt update \
&& apt install -y --no-install-recommends \
    ca-certificates \
    git \
&& if [ $PYVERSION -eq 3 ] \
    ; then \
        apt install -y --no-install-recommends \
            python$PYVERSION \
            python$PYVERSION-distutils \
            python3-pip \
            python$PYVERSION-venv \
        && rm -rf /var/lib/apt/lists/* \
    ; else \
        echo "Install from Source" \
; fi \
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