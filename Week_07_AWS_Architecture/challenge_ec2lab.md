# 🚀 Amazon EC2 Instances Challenge Lab

This repository documents the steps, configurations, and results of my **AWS re/Start EC2 Challenge Lab**, where I deployed a simple web application on an **Amazon Linux EC2 instance** running an **Apache (httpd)** web server.

---

## 🧭 Lab Overview

In this challenge, I created and configured a virtual network, launched an Amazon EC2 instance, installed a web server, and deployed a simple HTML webpage.

**Objectives**
- Configure a Virtual Private Cloud (VPC)
- Place an Amazon Linux EC2 instance in that VPC
- Install and configure an Apache web server
- Deploy and run a simple web application

---

## 🕐 Duration

Approx. **45 minutes**

---

## 🛠️ Steps Performed

### 1️⃣ Network Configuration
- Created a **VPC** with IPv4 CIDR `10.0.0.0/16`
- Created a **public subnet** `10.0.1.0/24`
- Created and attached an **Internet Gateway** to the VPC
- Created a **Route Table** with a route to `0.0.0.0/0` via the Internet Gateway
- Associated the route table with the public subnet
- Enabled **Auto-assign Public IPv4 address** for the subnet

---

### 2️⃣ Security Group Configuration
- Created a **Security Group** named `reStart-sg`
- Allowed the following inbound traffic:
  - **SSH (TCP 22)** — from my IP address
  - **HTTP (TCP 80)** — from anywhere (`0.0.0.0/0`)
- Allowed all outbound traffic

---

### 3️⃣ Launching the EC2 Instance
- **AMI:** Amazon Linux 2 AMI (HVM)
- **Instance Type:** t3.micro
- **Storage:** 8 GiB General Purpose SSD (gp2)
- **Network:** reStart-VPC and reStart-subnet
- **Public IPv4:** Enabled
- **Security Group:** reStart-sg

**User Data Script used during launch:**
```bash
#!/bin/bash
yum update -y
yum install -y httpd
systemctl enable httpd
systemctl start httpd
chmod 777 /var/www/html
````

---

### 4️⃣ Verifying Installation

After launch, I viewed the **system log** and confirmed that `httpd` was successfully installed and started.

Commands used for verification:

```bash
sudo systemctl status httpd
sudo ss -tlnp | grep :80
curl -I http://localhost
```

The `curl` response confirmed Apache was running:

```
HTTP/1.1 200 OK
Server: Apache/2.4.65 (Amazon Linux)
```

---

### 5️⃣ Deploying the Web Application

I created a simple HTML file named `projects.html` and placed it in the `/var/www/html` directory.

```html
<!DOCTYPE html>
<html>
<body>
<h1>Edwin Muigai's re/Start Project Work</h1>
<p>EC2 Instance Challenge Lab</p>
</body>
</html>
```

Commands:

```bash
cat <<'EOF' > projects.html
<!DOCTYPE html>
<html>
<body>
<h1>Edwin Muigai's re/Start Project Work</h1>
<p>EC2 Instance Challenge Lab</p>
</body>
</html>
EOF

sudo mv projects.html /var/www/html/projects.html
sudo chmod 644 /var/www/html/projects.html
sudo systemctl restart httpd
```

---

### 6️⃣ Testing the Application

Opened the following URL in the browser:

```
http://<PUBLIC_IPV4>/projects.html
```

✅ The web page loaded successfully, displaying my name and the lab project title.

---

## 📸 Screenshots


![EC2 CLI after connecting](./screenshots/cli.png)
![EC2 **System Log** showing httpd successfully installed](./screenshots/system-log.png)
![**Web Page** displayed in browser](./screenshots/web-page.png)


**Folder structure:**

```
ec2-challenge-lab/
│
├── README.md
└── screenshots/
    ├── system-log.png
    ├── web-page.png
    └── instance-details.png
```

---

## ✅ Verification Checklist

* [x] VPC and Subnet created
* [x] Internet Gateway configured
* [x] Route table set for `0.0.0.0/0`
* [x] Security Group allows SSH and HTTP
* [x] EC2 instance launched using Amazon Linux 2
* [x] httpd installed and running
* [x] HTML web page deployed and accessible
* [x] Screenshots captured

---

## 📚 Useful Commands

| Purpose               | Command                        |
| --------------------- | ------------------------------ |
| Update instance       | `sudo yum update -y`           |
| Install Apache        | `sudo yum install -y httpd`    |
| Start Apache          | `sudo systemctl start httpd`   |
| Enable Apache at boot | `sudo systemctl enable httpd`  |
| Check Apache status   | `sudo systemctl status httpd`  |
| Restart Apache        | `sudo systemctl restart httpd` |
| Test with curl        | `curl -I http://localhost`     |

---

## 🧩 Troubleshooting Notes

| Issue                     | Solution                                                                                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------- |
| **HTTP 403 Forbidden**    | Ensure correct file permissions (`chmod 755 /var/www/html`, `chmod 644 /var/www/html/projects.html`) |
| **No Public IP**          | Enable Auto-assign public IP in subnet or instance settings                                          |
| **Cannot SSH or connect** | Check Security Group rules for SSH (22) and HTTP (80)                                                |
| **User data didn’t run**  | Check system log via **Actions → Monitor and troubleshoot → Get system log**                         |

---

## 👤 Author

**Edwin Muigai**
AWS re/Start Student | Aspiring Cloud & Backend Developer

🔗 [GitHub Profile](https://github.com/MuigaiEdwin)

---

## 📘 References

* [AWS re/Start Labs – Amazon EC2 Challenge](https://aws.amazon.com/training/restart/)
* [AWS Documentation – Launching Your First EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
* [Apache HTTP Server Guide](https://httpd.apache.org/docs/)

````

---

### 💾 Instructions to Use


