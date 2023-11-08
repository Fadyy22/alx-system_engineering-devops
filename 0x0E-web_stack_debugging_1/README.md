# Project: 0x0E. Web stack debugging #1

<h2>Learning Objectives</h2>

<p>
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements:

    - Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
    - Write a Bash script that configures a server to the above requirements

</p>
<h3>General</h3>

<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted on Ubuntu 20.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file at the root of the folder of the project is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash scripts must pass Shellcheck without any error</li>
<li>Your Bash scripts must run without error</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
<li>You are not allowed to use wget</li>
</ul>

<h2>Tasks</h2>

| Task                   | File                                             |
| ---------------------- | ------------------------------------------------ |
| 0. Nginx likes port 80 | [0-nginx_likes_port_80](./0-nginx_likes_port_80) |
