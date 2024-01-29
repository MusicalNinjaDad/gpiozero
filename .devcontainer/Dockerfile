FROM mcr.microsoft.com/devcontainers/base:debian

# ---
# Add testing repo to get latest versions of tools
COPY <<EOF /etc/apt/sources.list.d/testing.list
deb http://deb.debian.org/debian testing main
EOF

# # ---
# # Prefer stable versions
# COPY <<EOF /etc/apt/preferences
# Package: *
# Pin: release a=stable
# Pin-Priority: 700

# Package: *
# Pin: release a=testing
# Pin-Priority: 650
# EOF

# ---
# Install Python 3.12
RUN apt update \
&& apt install -y --no-install-recommends python3.12-full python3-pip \
&& rm -rf /var/lib/apt/lists/*

# ---
# Install tools needed for building docs
RUN apt update \
&& apt install -y --no-install-recommends \
    graphviz \
    inkscape \
&& rm -rf /var/lib/apt/lists/*