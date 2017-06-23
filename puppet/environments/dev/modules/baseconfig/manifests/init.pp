class baseconfig {
  host { 'hostmachine':
    ip => '192.168.0.1';
  }

  exec { 'yum clean':
    command => '/usr/bin/yum -y clean all';
  }

  package { 'postgresql-devel':
    ensure => 'latest',
  }

  package { 'postgresql-server':
    ensure => 'latest',
  }

  package { 'postgresql-contrib':
    ensure => 'latest',
  }

  file {
    '/vagrant/database_shim.sh':
      owner => 'vagrant',
      group => 'vagrant',
      mode  => '0777',
      source => 'puppet:///modules/baseconfig/database_shim.sh',
      notify => Exec['database_shim'];
  }

  exec { 'database_shim':
    command => "/usr/bin/sudo /bin/bash -c '/vagrant/database_shim.sh'",
  }

  file {
    '/home/vagrant/.bashrc':
      owner => 'vagrant',
      group => 'vagrant',
      mode  => '0644',
      source => 'puppet:///modules/baseconfig/bashrc';
  }

  # Configure postgres:
  file {
    '/var/lib/pgsql/data/pg_hba.conf':
      owner => 'postgres',
      group => 'postgres',
      mode  => '0640',
      source => 'puppet:///modules/baseconfig/pg_hba.conf'
  }

  # Create fizzbuzz database and fizzbuzzuser user:
  exec { 'Setup Database':
    command => '/usr/bin/sudo su postgres /vagrant/vagrant/conf/setup_psql.sh'
  }

  exec { 'Install Django via pip':
    command => '/usr/bin/sudo /usr/bin/pip install Django'
  }

  exec { 'Install restframework via pip':
    command => '/usr/bin/sudo /usr/bin/pip install djangorestframework'
  }

  exec { 'Install psycopg2 via pip':
    command => '/usr/bin/sudo /usr/bin/pip install psycopg2==2.5.4'
  }

  exec { 'Install markdown via pip':
    command => '/usr/bin/sudo /usr/bin/pip install markdown'
  }

  # set up directory for app to be installed to
  file { "/opt/fizzbuzz":
    ensure => "directory",
    owner  => "root",
    group  => "root",
    mode   => "0744",
  }

  # Configure apache
 # file {
 #   '/etc/apache2/sites-available/default':
 #     owner => 'root',
 #     group => 'root',
 #     mode  => '0644',
 #     source => 'puppet:///modules/baseconfig/apache_site';
 # }

  # make sure apache is started
  #service { "apache2":
  #  ensure => "running"
  #}
}
