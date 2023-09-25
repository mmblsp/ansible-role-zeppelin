Zeppelin server
=========

[Apache Zeppelin Doc](https://zeppelin.apache.org/docs/latest/quickstart/install.html#starting-apache-zeppelin)

Requirements
------------

- Availability of Internet access

Role Variables
--------------

- zeppelin_binary_package_url: https://zeppelin.apache.org/docs/latest/quickstart/install.html#downloading-binary-package
- zeppelin_user: zeppelin
- zeppelin_home: /opt/zeppelin
- zeppelin_listen_all: false

Dependencies
------------

- [role java](https://github.com/mmblsp/ansible-role-java.git)

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: zeppelin }

License
-------

Apache 2.0

Author Information
------------------

[VK](https://vk.com/mmblspace)
