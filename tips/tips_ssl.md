# SSL / TLS technologies

### Querying for SSL / TLS Protocols
```text
openssl s_client -connect www.incspot.com:443 -tls1
openssl s_client -connect www.incspot.com:443 -tls1_1
openssl s_client -connect www.incspot.com:443 -tls1_2
openssl s_client -connect www.incspot.com:443 -ssl3

# Using nmap
nmap --script ssl-enum-ciphers -p 443 www.ibm.com
``` 
### Generating SSL Certs
#### [Lets Encryt](https://letsencrypt.org/getting-started/)
#### [Certbot](https://certbot.eff.org/lets-encrypt/ubuntuxenial-apache)
#### To install using Certbot
```commandline
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python-certbot-apache
sudo apt-get install certbot python3-certbot-dns-rfc2136
```

#### Create a certificate
```commandline
sudo certbot --apache certonly
```

#### [Local CA](https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/)

### Compile OpenSSL source code
 - Download [here](https://www.openssl.org/source/openssl-1.1.1d.tar.gz)
 - Compile directives
    - openssldir used for storing OpenSSL Configuration files, certs and keystore
    - prefix --> installation directory. Preference is to keep the version so
    multiple versions can be supported.
```text
tar xfz ../Downloads/openssl-1.1.1d.tar.gz
./config --prefix=/usr/local/openssl-1.1.1d --openssldir=/usr/local/ssl
```