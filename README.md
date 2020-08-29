Ansible Role: RPi LCD
=====================

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

Set the LCD screen rotation.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: pi
      vars_files:
        - vars/main.yml
      roles:
         - { role: fedejaure.rpi_lcd }

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2020 by [Federico Jaureguialzo][fedejaure].

Credits
-------

For a detail configuring information see [LCD-show][LCD-show].


[fedejaure]: https://github.com/fedejaurefedejaure
[LCD-show]: https://github.com/goodtft/LCD-show
