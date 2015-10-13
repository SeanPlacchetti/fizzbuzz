# == Class: baseconfig
#
# Performs initial configuration tasks for fizzbuzz dev box
#
class baseconfig {
  host { 'hostmachine':
    ip => '192.168.0.1';
  }

  exec { 'apt-get update':
    command => '/usr/bin/apt-get -y update';
  }

  file {
    '/home/vagrant/.bashrc':
      owner => 'vagrant',
      group => 'vagrant',
      mode  => '0644',
      source => 'puppet:///modules/baseconfig/bashrc';
  }

  package { [
    "pkg-config",
    "make",
    ]:
      ensure => "latest",
      require => Exec['apt-get update'],
  }

  # Apache web server
  package { [
      "apache2",
      "apache2-utils",
      "libexpat1",
      "ssl-cert",
      "libapache2-mod-wsgi",
      ]:
    ensure => "latest",
    require => Exec['apt-get update'],
  }

  # Postgres
  package { [
      "postgresql",
      ]:
    ensure => "latest",
    require => Exec['apt-get update'],
  }
  # Configure postgres:
  file {
    '/etc/postgresql/9.1/main/pg_hba.conf':
      owner => 'postgres',
      group => 'postgres',
      mode  => '0640',
      source => 'puppet:///modules/baseconfig/pg_hba.conf',
      require => Package["postgresql"];
  }
  # Create fizzbuzz database and fizzbuzzuser user:
  exec { 'Setup Database':
    command => '/usr/bin/sudo su postgres /vagrant/vagrant/conf/setup_psql.sh',
    require => Package["postgresql"];
  }

  package { [
        "python2.7",
        "python-pip",
        "python-psycopg2",
        ]:
      ensure => "latest",
      require => Exec['apt-get update'],
  }

  exec { 'Install Django via pip':
    command => '/usr/bin/pip install Django',
    require => Package["python-pip"]
  }

  exec { 'Install restframework via pip':
    command => '/usr/bin/pip install djangorestframework',
    require => Package["python-pip"]
  }

  exec { 'Install markdown via pip':
    command => '/usr/bin/pip install markdown',
    require => Package["python-pip"]
  }

  # set up directory for app to be installed to
  file { "/opt/fizzbuzz":
    ensure => "directory",
    owner  => "root",
    group  => "root",
    mode   => 744,
  }

  # Configure apache
  file {
    '/etc/apache2/sites-available/default':
      owner => 'root',
      group => 'root',
      mode  => '0644',
      source => 'puppet:///modules/baseconfig/apache_site';
  }

  # make sure apache is started
  service { "apache2":
    ensure => "running",
    require => Package["apache2"],
  }


}
