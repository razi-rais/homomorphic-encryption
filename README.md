# Homomorphic Encryption

## Partially Homomorphic Encryption in Python | PHE Python Library
* Source: https://github.com/n1analytics/python-paillier
* Documentation: http://python-paillier.readthedocs.io/en/stable

This library requires bunch of dependencies that may be challenging to install specially if you're new to Linux. To save 
myself some time I end up packaging it as docker container image. This made it easy to work with this on MacOS, Linux 
and Windows (with nested virtualization enabled). Please do note that this is not an official docker image from the 
vendor and I don't claim any ownership or responsibility.

* Docker Image | PHE Python Library: https://hub.docker.com/r/rbinrais/python-paillier

**Example**

```
docker run --rm -it rbinrais/python-paillier:1.2.2 bash
```

