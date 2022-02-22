# IPFS-REST-API
![picture alt](https://i.pinimg.com/originals/e9/e3/13/e9e313b798bd29d5223e9e379cb52e80.png "IPFS logo")

This is a RESTful API interface for interacting with the IPFS network from any language with ease. Simply deploy the server running the IPFS daemon on either your local machine or one in the cloud and start making HTTP requests with any language for easy use. The current API supports the ability to:

* Upload files to IPFS
* Download files from IPFS
* Show files content from IPFS
* Show links for file from IPFS
* All MFS commands with limited args
    * ls
    * write
    * rm
    * read
    * stat
    * mkdir
    * mv
    * cp
  
All requests through the server are recorded on an SQL database for easy logging and monitoring of the API and a node on the network. Easy creation of private IPFS networks and full MFS command args is in the works, more information on the Inter-Planetary-File-System can be found here: [https://docs.ipfs.io/](https://docs.ipfs.io/ "https://docs.ipfs.io/")
