#!/usr/bin/env bash
# Function to install Nginx

install_nginx() {
    if ! nginx -v &> /dev/null; then
        sudo apt update
        sudo apt install -y nginx
        
    fi
}

# Function to create a directory if it doesn't exist
create_directory() {
    local dir=$1
    if [ ! -d "$dir" ]; then
        sudo mkdir -p "$dir"
    fi
}

# Function to create a fake HTML file
create_fake_html() {
    local file="$1"
    echo "<!DOCTYPE html>
<html>
<head>
    <title>TEST</title>
</head>
<body>
    <h1>Test</h1>
</body>
</html>" > "$file"
}

# Function to create a symbolic link
create_symbolic_link() {
    local target=$1
    local link=$2
    if [ -L "$link" ]; then
        sudo rm -f "$link"
    fi
    sudo ln -s "$target" "$link"
}

# Function to set ownership
set_ownership() {
    local dir=$1
    sudo chown -R ubuntu:ubuntu "$dir"
}

# Function to update Nginx configuration
update_nginx_configuration() {
    local nginx_conf="/etc/nginx/sites-available/default"
    sudo sed -i '/server_name _;/a location /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n}' "$nginx_conf"
    sudo systemctl restart nginx
}

# Run the functions
install_nginx
create_directory "/data/"
create_directory "/data/web_static/"
create_directory "/data/web_static/releases/"
create_directory "/data/web_static/shared/"
create_directory "/data/web_static/releases/test/"
create_fake_html "/data/web_static/releases/test/index.html"
create_symbolic_link "/data/web_static/releases/test/" "/data/web_static/current"
set_ownership "/data/"
update_nginx_configuration
exit 0
