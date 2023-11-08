# Project: 0x0F. Load balancer

<h2>Learning Objectives</h2>

<p>Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h3>General</h3>

<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass Shellcheck (version 0.3.7) without any error</li>
<li>The first line of all your Bash scripts should be exactly #!/usr/bin/env bash</li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>Tasks</h2>

| Task                               | File                                                             |
| ---------------------------------- | ---------------------------------------------------------------- |
| 0. Double the number of webservers | [0-custom_http_response_header](./0-custom_http_response_header) |
| 1. Install your load balancer      | [1-install_load_balancer](./1-install_load_balancer)             |
