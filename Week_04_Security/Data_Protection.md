# Data Protection Using AWS KMS Encryption

A hands-on lab demonstrating data encryption and decryption using AWS Key Management Service (KMS) and the AWS Encryption CLI.

## Overview

This project demonstrates the fundamental concepts of cryptography and data protection using AWS services. The lab covers creating encryption keys, encrypting plaintext data, and decrypting ciphertext using AWS KMS with symmetric encryption.

## Technologies Used

- **AWS KMS** - Key Management Service for creating and managing cryptographic keys
- **AWS EC2** - Elastic Compute Cloud instance (File Server)
- **AWS Systems Manager** - Session Manager for secure instance access
- **AWS Encryption CLI** - Command-line tool for encryption operations
- **Python 3** - Runtime for AWS Encryption SDK

## Lab Objectives

- ✅ Create an AWS KMS symmetric encryption key
- ✅ Configure AWS credentials on EC2 instance
- ✅ Install and configure AWS Encryption CLI
- ✅ Encrypt plaintext files using KMS keys
- ✅ Decrypt ciphertext back to readable format

## Architecture

The lab uses a pre-configured EC2 instance (File Server) with an attached IAM role that allows:
- Connection via AWS Systems Manager Session Manager
- Access to AWS KMS for encryption/decryption operations
- Secure credential management

## Key Concepts

### Symmetric Encryption
- Uses the same key for both encryption and decryption
- Fast and efficient for data protection
- Ideal for encrypting data at rest

### Cryptography Functions
- **Authentication** - Verify identity
- **Data Integrity** - Ensure data hasn't been tampered with
- **Nonrepudiation** - Prove the origin of data
- **Confidentiality** - Keep information private

## Setup & Configuration

### 1. Create KMS Key

```bash
# Key specifications:
# - Type: Symmetric
# - Alias: MyKMSKey
# - Description: Key used to encrypt and decrypt data files
```

### 2. Configure AWS Credentials

```bash
cd ~
aws configure

# Update credentials file
vi ~/.aws/credentials

# Paste AWS credentials from AWS Details
# File should contain:
# - aws_access_key_id
# - aws_secret_access_key
# - aws_session_token
```

### 3. Install AWS Encryption CLI

```bash
pip3 install aws-encryption-sdk-cli
export PATH=$PATH:/home/ssm-user/.local/bin
```

## Usage Examples

### Encrypting Data

```bash
# Create test files
touch secret1.txt secret2.txt secret3.txt
echo 'TOP SECRET 1!!!' > secret1.txt

# Create output directory
mkdir output

# Set KMS key ARN variable
keyArn=arn:aws:kms:REGION:ACCOUNT:key/KEY-ID

# Encrypt file
aws-encryption-cli --encrypt \
                     --input secret1.txt \
                     --wrapping-keys key=$keyArn \
                     --metadata-output ~/metadata \
                     --encryption-context purpose=test \
                     --commitment-policy require-encrypt-require-decrypt \
                     --output ~/output/.

# Verify encryption success
echo $?  # Should return 0
```

### Decrypting Data

```bash
cd output

# Decrypt encrypted file
aws-encryption-cli --decrypt \
                     --input secret1.txt.encrypted \
                     --wrapping-keys key=$keyArn \
                     --commitment-policy require-encrypt-require-decrypt \
                     --encryption-context purpose=test \
                     --metadata-output ~/metadata \
                     --max-encrypted-data-keys 1 \
                     --buffer \
                     --output .

# View decrypted contents
cat secret1.txt.encrypted.decrypted
```

## Encryption Process Flow

![Lab Dashboard Screenshot](/screenshots/Symmetric_Key_Encryption.png)
![Lab Dashboard Screenshot](/screenshots/Symmetric_Key_Decryption.png)

## Security Best Practices

- ✅ Use encryption context for additional security
- ✅ Enable key commitment policy for encrypt/decrypt operations
- ✅ Limit encrypted data keys (`--max-encrypted-data-keys`)
- ✅ Store KMS keys securely with proper IAM permissions
- ✅ Use AWS KMS hardware security modules (HSMs) validated under FIPS 140-2

## Command Parameters Explained

| Parameter | Description |
|-----------|-------------|
| `--encrypt` / `--decrypt` | Specifies the operation type |
| `--input` | File to encrypt or decrypt |
| `--wrapping-keys` | AWS KMS key ARN for cryptographic operations |
| `--metadata-output` | File to store encryption/decryption metadata |
| `--encryption-context` | Additional authenticated data (AAD) |
| `--commitment-policy` | Key commitment security feature setting |
| `--output` | Destination directory for output files |

## Learning Outcomes

Through this lab, I gained hands-on experience with:
- Creating and managing AWS KMS keys
- Configuring AWS CLI credentials securely
- Understanding symmetric vs asymmetric encryption
- Implementing encryption/decryption workflows
- Using AWS Encryption CLI for data protection
- Best practices for key management and data security

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of cryptography concepts
- Familiarity with Linux command line
- AWS IAM role with KMS permissions

## Duration

Approximately 45 minutes

## References

- [AWS Key Management Service Documentation](https://docs.aws.amazon.com/kms/)
- [AWS Encryption CLI Documentation](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/crypto-cli.html)
- [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/)

## License

This is an educational lab project for learning AWS encryption services.

---

**Note**: This lab was completed as part of AWS training. Credentials and resources shown are for demonstration purposes in a controlled lab environment.