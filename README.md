Ansible Role: Raspberry Pi LCD
==============================

[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/fedejaure/ansible-role-rpi-lcd?logo=github)](https://github.com/fedejaure/ansible-role-rpi-lcd/releases)
[![Ansible Role](https://img.shields.io/ansible/role/50495)](https://galaxy.ansible.com/fedejaure/rpi_lcd)
[![Ansible Role](https://img.shields.io/ansible/role/d/50495)](https://galaxy.ansible.com/fedejaure/rpi_lcd)
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50495)](https://galaxy.ansible.com/fedejaure/rpi_lcd)
[![tests](https://github.com/fedejaure/ansible-role-rpi-lcd/actions/workflows/tests.yml/badge.svg)](https://github.com/fedejaure/ansible-role-rpi-lcd/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Configures the LCD driver of Raspberry Pi.

This role was built for learning purposes on ansible (use by your on risk).

Supported LCD's type, so far:

  * 3.5inch RPi Display (MPI3501)

Requirements
------------

None.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    lcd_type: MPI3501

Select the LCD type to be configured.

    lcd_rotate: 90

Set the LCD screen rotation. It depends on LCD type:

  * 3.5inch RPi Display (MPI3501):
    - 0
    - 90
    - 180
    - 270

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: pi

      vars:
        lcd_type: MPI3501
        lcd_rotate: 90

      roles:
         - fedejaure.rpi_lcd

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2020 by [Federico Jaureguialzo][fedejaure].

Credits
-------

For a detail configuring information see [LCD-show][LCD-show].


[fedejaure]: https://github.com/fedejaure
[LCD-show]: https://github.com/goodtft/LCD-show
