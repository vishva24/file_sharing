# file_sharing
p2p_file_sharing using python
Introduction
P2P is a file sharing technology, allowing the users to access mainly the files like
videos, music, e-books, games etc. The individual users in this network are referred
to as peers. The peers request for the files from other peers by establishing TCP or
UDP connections.
Abstract
The project is Python based Peer-to-Peer File Sharing System. The Peer-to-Peer or
the Point-to-Point (P2P) technology enables the sharing of computer resources such
as files by a direct exchange between the end user’s computers. The main objective
of this project is to create a Peer to Peer server that is capable of uploading files
and indexed searching of files from a peer that is able to be both a server and a
peer (client) at the same time using the TCP protocol. The motivation for the
implementation of this project is to familiarize with socket programming and TCP
communication channels. The approach towards this project is to first create and
implement a working server, then to create and implement a working client that will
be able to connect and send requests to the server.
The program expects the user (client) to first enter the port on which its socket will
be listening, the user also needs to mention the address of the server (i.e the port
on which the server is listening) it wants to make a connection with. Once the
connection is established the client can make requests to the server (peer) it is
connected to. The Server program mainly maintains a hash table which stores the
information regarding all the users present in the network and the files that each
user has. The hash table hashes all the files available on the server and specifies a
unique number for accessing each file.
Technical Details
The project consists of the Centralized Directory architecture of P2P File Sharing
technology. It is similar to the client-server architecture as it maintains a central
server to provide directory service. All the peers inform this central server of their
IP address and the files they are making available for sharing. The directory server
collects this information from each peer that becomes active, thereby creating a
centralized, dynamic hash table that maps each object, or removes an object, the
client(peer) informs the directory server, so that the directory server can update its
database.
In order to keep its database current, the directory server must be able to
determine when a peer becomes disconnected. A peer can become disconnected
by closing its P2P client application or simply by disconnecting from the Internet. If
the directory server determines that a peer is no longer connected, the directory
server removes the peer's IP addresses from the database.
Implementation
The server starts by assigning to it a socket and binding it to a port and then it waits
for the clients. Whenever a client arrives, the server asks the client for the files it
wants to transmit until the client refuses. Meanwhile, the server will create a list of
of files available i.e the files which the client is willing to transmit. When the client
further refuses to transmit files (by entering -1) then the server updates the hash
table by providing the list of files to the corresponding index of the client. The
server then asks the client if it wants to receive any files. If the client doesn’t wish to
receive any file, it can simply exit by entering -1. Whereas if the client wants to
receive any file from any of the peers then the client can send its request to the
centralized server. Here the connection is again setup with the peer holding the file.
The client will then enter the file name which it wishes to receive. Meanwhile, if the
peer holding the file has deleted the file or it doesn't hold the file any longer than it
will display an error at clients end and again it will prompt to enter another file
name or exit by entering -1. If the requested file is available with the peer than it will
send that particular file in encoded form which will apparently be decoded at
client’s end. After a peer has received a whole file then it will be automatically be
removed from the list of clients in the servers list. During this whole time the server
will maintain the list of all the peers i.e its IP addresses and the list of files it wants
to shares with the other users.

Conclusion
P2P File Sharing is used in large companies and even in universities, for the quick
transfer of files between the end systems in the same or different local networks.
The main advantage of P2P File Sharing is that it is easier to setup and is less
expensive. Also all the nodes can act as server as well as client.

Using a centralized directory in P2P File Sharing for locating content is conceptually
straightforward, but it does have a number of drawbacks:
● Single point of failure : If the directory server crashes, then the entire P2P
application crashes.
● Performance bottleneck : In a large P2P system, with hundreds of
thousands of connected users, a centralized server must maintain a huge
database and must respond to thousands of queries per second.
● Copyright infringement : P2P file-sharing systems allow users to easily
obtain copyright content for free.
The salient drawback of using a centralized directory server is that the P2P
application is only partially decentralized. The file transfer between peers is
decentralized, but the process of locating content is highly centralized--a reliability
and performance concern.
