# AWS Amazon EBS Lab Guide

A comprehensive hands-on lab demonstrating Amazon Elastic Block Store (EBS) operations including volume creation, attachment, snapshot management, and restoration.

## Overview

This lab provides practical experience with Amazon EBS, a scalable, high-performance block-storage service designed for Amazon EC2. You'll learn essential storage management operations that are fundamental to AWS infrastructure management.

![EBS Architecture](https://via.placeholder.com/800x300?text=EC2+Instance+%E2%86%94+EBS+Volume+%E2%86%92+Snapshot)

## Learning Objectives

By completing this lab, you will be able to:

- ✅ Create an EBS volume
- ✅ Attach and mount an EBS volume to an EC2 instance
- ✅ Create a snapshot of an EBS volume
- ✅ Create an EBS volume from a snapshot
- ✅ Perform file system operations on mounted volumes

## Prerequisites

- AWS account with appropriate permissions
- Basic understanding of Linux command line
- Familiarity with EC2 instances
- Approximately 45 minutes to complete

## Lab Architecture

![Lab Dashboard Screenshot](/screenshots/ebs.png)

## Tasks Overview

### Task 1: Creating a New EBS Volume
Create a 1GB General Purpose SSD (gp2) volume in the same Availability Zone as your EC2 instance.

### Task 2: Attaching the Volume
Attach the newly created volume to the Lab EC2 instance using device name `/dev/sdb`.

### Task 3: Connecting to EC2 Instance
Use EC2 Instance Connect to establish a terminal session with your instance.

### Task 4: File System Configuration
Format the volume with ext3 file system and mount it to `/mnt/data-store`.

### Task 5: Creating an EBS Snapshot
Create a point-in-time snapshot of your EBS volume, stored in Amazon S3.

### Task 6: Restoring from Snapshot
Create a new volume from the snapshot and verify data restoration.

## Step-by-Step Instructions

### 1. Create EBS Volume

```bash
# In AWS Console:
# - Navigate to EC2 > Volumes
# - Create volume with:
#   * Type: gp2
#   * Size: 1 GiB
#   * AZ: Same as EC2 instance
#   * Tag: Name = "My Volume"
```

### 2. Attach Volume to Instance

```bash
# In AWS Console:
# - Select "My Volume"
# - Actions > Attach volume
# - Instance: Lab
# - Device: /dev/sdb
```

### 3. Format and Mount Volume

```bash
# View current storage
df -h

# Create ext3 file system
sudo mkfs -t ext3 /dev/sdb

# Create mount point
sudo mkdir /mnt/data-store

# Mount the volume
sudo mount /dev/sdb /mnt/data-store

# Make mount persistent
echo "/dev/sdb   /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab

# Verify mount
df -h
```

### 4. Test Volume

```bash
# Create test file
sudo sh -c "echo some text has been written > /mnt/data-store/file.txt"

# Verify file
cat /mnt/data-store/file.txt
```

### 5. Create Snapshot

```bash
# In AWS Console:
# - Select "My Volume"
# - Actions > Create snapshot
# - Tag: Name = "My Snapshot"
```

### 6. Restore from Snapshot

```bash
# In AWS Console:
# - Navigate to Snapshots
# - Select "My Snapshot"
# - Actions > Create volume from snapshot
# - Tag: Name = "Restored Volume"
# - Attach to Lab instance as /dev/sdc

# Mount restored volume
sudo mkdir /mnt/data-store2
sudo mount /dev/sdc /mnt/data-store2

# Verify data restoration
ls /mnt/data-store2/file.txt
cat /mnt/data-store2/file.txt
```

## Key Concepts

### EBS Volume Types
- **General Purpose SSD (gp2/gp3)**: Balanced price/performance
- **Provisioned IOPS SSD (io1/io2)**: High-performance workloads
- **Throughput Optimized HDD (st1)**: Big data, data warehouses
- **Cold HDD (sc1)**: Infrequent access

### Snapshots
- Incremental backups stored in S3
- Only changed blocks are saved after first snapshot
- Can be used across Availability Zones
- Enable disaster recovery and data migration

### Best Practices
- Always create volumes in the same AZ as the EC2 instance
- Tag resources for better organization
- Regular snapshots for data protection
- Use appropriate volume types for workload requirements
- Configure persistent mounts in `/etc/fstab`

## Troubleshooting

### Volume Not Showing
```bash
# List all block devices
lsblk

# Check kernel messages
dmesg | tail
```

### Mount Issues
```bash
# Check file system
sudo file -s /dev/sdb

# Verify fstab syntax
cat /etc/fstab
```

### EC2 Instance Connect Not Working
- Refresh browser tab
- Reconnect using Connect button
- Check security group allows traffic

## Cleanup

To avoid charges after completing the lab:

1. Unmount volumes:
   ```bash
   sudo umount /mnt/data-store
   sudo umount /mnt/data-store2
   ```

2. Detach volumes from instance (AWS Console)
3. Delete volumes (AWS Console)
4. Delete snapshots (AWS Console)
5. Terminate EC2 instance (if desired)

## Additional Resources

- [Amazon EBS Documentation](https://docs.aws.amazon.com/ebs/)
- [EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
- [EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
- [Linux File Systems](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html)

## License

This lab guide is provided for educational purposes.

## Contributing

Feel free to submit issues or pull requests to improve this guide.

---