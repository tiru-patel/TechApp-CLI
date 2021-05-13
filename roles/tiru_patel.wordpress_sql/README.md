wpSQL
=========

A brief description of the role goes here.


Role Variables
--------------

- db_pod_name is the name of mysql pod. 
- wp_pod_name is the name of wordpress pod. 
Optional: You can add all the environment variables as variable like root password, user name etc while launching mysql pod. 


Example Playbook
----------------

    - hosts: ["tag_Name_k8s_Master"]
      roles: 
        - name: configure wordpress and mysql database and expose wordpress 
          role: /root/k8s_wp_sql_play/wpSQL/ 



