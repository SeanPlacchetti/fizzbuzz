#!/bin/bash
/usr/bin/sudo systemctl enable postgresql
/usr/bin/sudo postgresql-setup initdb
/usr/bin/sudo systemctl start postgresql