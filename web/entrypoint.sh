#!/bin/bash

exec gunicorn -b 0.0.0.0:5877 "app:create_app()"
