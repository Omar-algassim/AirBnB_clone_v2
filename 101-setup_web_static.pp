# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create necessary directories if they don't exist
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html><body>Hello World!.</body></html>',
}

# Create symbolic link (if it exists, remove it first)
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test/',
  require => File['/data/web_static/releases/test/index.html'],
  before  => Service['nginx'],
}

# Set ownership of /data/ folder recursively to ubuntu user and group
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration to serve content from /data/web_static/current/ to hbnb_static
file_line { 'add_location_to_nginx_config':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => '        location /hbnb_static { alias /data/web_static/current/; }',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
